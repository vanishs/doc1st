"""Deterministic tests for the regression harness, not tests of Codex itself."""

import subprocess
import tempfile
import unittest
from pathlib import Path

from codex_regression import CASES, RegressionFailure, prepare, spec, verify, verify_replay


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args], text=True).strip()


class BootstrapHarnessTests(unittest.TestCase):
    def test_specs_parse_and_fixtures_prepare(self):
        with tempfile.TemporaryDirectory() as directory:
            for case in sorted(CASES):
                with self.subTest(case=case):
                    root = Path(directory) / case
                    contract, _ = spec(case)
                    self.assertEqual(contract["id"], case)
                    prepare(case, root)
                    self.assertTrue((root / "AGENTS.md").is_file())
                    self.assertTrue((root / "DOC1ST.md").is_file())
                    self.assertTrue((root / "status.txt").is_file())
                    self.assertTrue((root.with_name(root.name + ".doc1st-test.json")).is_file())
                    with self.assertRaises(RegressionFailure):
                        prepare(case, root)  # Never overwrite fixture.

    def test_positive_and_negative_state_assertions(self):
        with tempfile.TemporaryDirectory() as directory:
            for case in sorted(CASES):
                with self.subTest(case=case):
                    root = Path(directory) / case
                    prepare(case, root)
                    if case in ("message-only-and-replay", "marker-deletion-no-approval"):
                        with self.assertRaises(RegressionFailure):
                            verify(root)  # No invented checkpoint on uninvoked fixture.
                        if case == "message-only-and-replay":
                            (root / "status.txt").write_bytes(b"Status: ready\n")
                            git(root, "add", "status.txt")
                        before = git(root, "rev-parse", "HEAD")
                        git(root, "commit", "--allow-empty", "-m", "Agent result",
                            "-m", "Doc1st-Origin: agent",
                            "-m", "Doc1st-Processed-Through: " + before)
                    verify(root)  # Simulated Git outcome only; no Codex was invoked.
                    if case == "message-only-and-replay":
                        verify_replay(root)
                        (root / "status.txt").write_bytes(b"Status: unexpected\n")
                        with self.assertRaises(RegressionFailure):
                            verify_replay(root)


if __name__ == "__main__":
    unittest.main()
