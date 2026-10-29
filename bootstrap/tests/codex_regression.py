#!/usr/bin/env python3
"""Prepare and verify a black-box regression case for the Codex bootstrap.

This harness verifies observable Git and file state. It never invokes an agent.
Requires Python 3.9+ and Git; no third-party Python packages.
"""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

BOOTSTRAP = Path(__file__).resolve().parents[1] / "codex"
PENDING = b"Status: pending\n"
READY = b"Status: ready\n"


class RegressionFailure(Exception):
    pass


def git(repo, *arguments):
    result = subprocess.run(
        ["git", *arguments],
        cwd=repo,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode:
        raise RegressionFailure(
            f"git {' '.join(arguments)} failed: {result.stderr.strip()}"
        )
    return result.stdout.strip()


def git_bytes(repo, *arguments):
    result = subprocess.run(
        ["git", *arguments], cwd=repo, capture_output=True
    )
    if result.returncode:
        raise RegressionFailure(
            f"git {' '.join(arguments)} failed: "
            + result.stderr.decode("utf-8", errors="replace")
        )
    return result.stdout


def require(condition, message):
    if not condition:
        raise RegressionFailure(message)


def metadata_path(repo):
    # Store regression bookkeeping outside the Git fixture.
    return repo.with_name(repo.name + ".doc1st-test.json")


def load_case(repo):
    require(repo.is_dir(), f"Fixture is missing: {repo}")
    path = metadata_path(repo)
    require(path.is_file(), f"Test metadata is missing: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    require(data.get("case") == "codex-message-only-v1", "Unknown test case")
    return data


def save_case(repo, data):
    metadata_path(repo).write_text(
        json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def prepare(repo):
    require(not repo.exists(), f"Refusing to overwrite existing path: {repo}")
    require(
        not metadata_path(repo).exists(),
        f"Refusing to overwrite existing test metadata: {metadata_path(repo)}",
    )
    for relative in (
        "AGENTS.md",
        "DOC1ST.md",
        ".agents/skills/human-decision/SKILL.md",
    ):
        require((BOOTSTRAP / relative).is_file(), f"Missing template: {relative}")

    repo.mkdir(parents=True)
    for relative in (
        "AGENTS.md",
        "DOC1ST.md",
        ".agents/skills/human-decision/SKILL.md",
    ):
        destination = repo / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(BOOTSTRAP / relative, destination)

    (repo / "status.txt").write_bytes(PENDING)
    git(repo, "init", "-b", "main")
    git(repo, "config", "user.name", "doc1st fixture")
    git(repo, "config", "user.email", "fixture@example.invalid")
    git(repo, "config", "core.autocrlf", "false")
    git(repo, "add", "--all")
    git(repo, "commit", "-m", "Initialize bootstrap regression fixture",
        "-m", "Doc1st-Origin: setup")
    git(repo, "commit", "--allow-empty",
        "-m", "Set status.txt to exactly 'Status: ready' followed by one newline. "
              "Do not change any other project file.")
    input_sha = git(repo, "rev-parse", "HEAD")
    save_case(repo, {
        "case": "codex-message-only-v1",
        "input_sha": input_sha,
        "verified_head": None,
    })
    print(f"PREPARED: {repo}")
    print(f"Synthetic input commit: {input_sha}")
    print("Next: open this fixture in Codex and request one doc1st reconciliation cycle.")


def assert_clean(repo):
    require(git(repo, "status", "--porcelain") == "",
            "Working tree is not clean")


def assert_ready(repo):
    actual = (repo / "status.txt").read_bytes()
    require(actual == READY,
            f"status.txt differs: expected {READY!r}, got {actual!r}")


def verify(repo):
    data = load_case(repo)
    input_sha = data["input_sha"]
    head = git(repo, "rev-parse", "HEAD")
    require(head != input_sha, "No agent checkpoint was created")
    require(git(repo, "rev-parse", "HEAD^") == input_sha,
            "Expected one direct agent checkpoint after the input commit")
    require(git(repo, "rev-list", "--count", f"{input_sha}..HEAD") == "1",
            "Expected exactly one new commit")
    body = git(repo, "log", "-1", "--format=%B")
    trailers = [line.strip() for line in body.splitlines()]
    require("Doc1st-Origin: agent" in trailers,
            "Agent origin trailer is missing")
    require(f"Doc1st-Processed-Through: {input_sha}" in trailers,
            "Processed-through trailer does not match input")
    changed_paths = git(repo, "diff", "--name-only", input_sha, "HEAD")
    require(changed_paths.splitlines() == ["status.txt"],
            f"Unexpected changed files: {changed_paths!r}")
    require(git_bytes(repo, "show", "HEAD:status.txt") == READY,
            "Committed status.txt does not match expected content")
    assert_ready(repo)
    assert_clean(repo)
    data["verified_head"] = head
    save_case(repo, data)
    print(f"PASS: correct change and one checkpoint ({head})")
    print("Next: run another cycle with no new human commit, then verify-replay.")


def verify_replay(repo):
    data = load_case(repo)
    require(data.get("verified_head"), "Run verify before verify-replay")
    require(git(repo, "rev-parse", "HEAD") == data["verified_head"],
            "Replay changed HEAD despite no new eligible input")
    assert_ready(repo)
    assert_clean(repo)
    print("PASS: no new checkpoint, file change, or uncommitted work on replay")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("prepare", "verify", "verify-replay"))
    parser.add_argument("fixture", type=Path,
                        help="Dedicated test directory (must not exist for prepare)")
    args = parser.parse_args()
    repo = args.fixture.resolve()
    try:
        {"prepare": prepare, "verify": verify,
         "verify-replay": verify_replay}[args.action](repo)
    except (RegressionFailure, OSError, ValueError, KeyError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
