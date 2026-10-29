# Codex bootstrap behavioral regression: message-only cycle

**Case:** `codex-message-only-v1`  
**Status:** Executable fixture and state assertions; requires a **manual Codex invocation**.  
**Scope:** Codex bootstrap only. This is not a standalone client test.

## Why this exists

When `bootstrap/codex/` changes, rerun the same behavioral case against the
updated templates. Differences are **review signals**, not permission to
automatically rewrite test expectations or declare the bootstrap broken.
The normative contract lives in `../../protocol/`; the checks here are a
small, stable set of externally observable expectations.

## Run

Requirements: Python 3.9+, Git, and Codex App/CLI with repository access.
Run commands from the doc1st source checkout:

```sh
python3 bootstrap/tests/codex_regression.py prepare /tmp/doc1st-codex-case
```

The command creates a **new**, isolated Git repository using the current
`bootstrap/codex/` templates. It records the synthetic input SHA in a JSON
file **beside** (not inside) the fixture repository. It refuses to overwrite
an existing fixture.

1. Open `/tmp/doc1st-codex-case` in Codex. Ask exactly: **Run one doc1st reconciliation cycle.** Allow only the actions needed for this disposable repository.
2. Back in the doc1st checkout, run:
   ```sh
   python3 bootstrap/tests/codex_regression.py verify /tmp/doc1st-codex-case
   ```
3. In the same Codex workspace, ask again: **Run one doc1st reconciliation cycle.** There must be **no new eligible input**.
4. Run:
   ```sh
   python3 bootstrap/tests/codex_regression.py verify-replay /tmp/doc1st-codex-case
   ```

To retest a changed bootstrap, use a **fresh fixture path**. Never adjust the
expected outcome to match a failing agent run without human review.

## Fixed expected behavior

The first synthetic input is an **empty human-intent commit** requesting
`status.txt` change from `Status: pending\\n` to `Status: ready\\n`.

- Exactly one child agent checkpoint commit after that input, carrying
  `Doc1st-Origin: agent` and
  `Doc1st-Processed-Through: <exact input SHA>`.
- Only `status.txt` changes; its **committed and working bytes** equal the
  requested value; the fixture worktree is clean.
- On a second cycle with no new input, HEAD, the file and clean worktree
  remain unchanged. No empty replay checkpoint is allowed.

A successful Codex CLI process exit, a plausible agent reply, or a reported
test pass is **not** a substitute for these independent checks.

## Interpreting differences

On a failure, compare the bootstrap/protocol diff, the agent's actual file
and commit state, its explanation, and this case's assumptions. Decide whether
the bootstrap violated the intended contract, the test encoded an outdated
expectation, or the agent/environment produced a transient failure. Record
the decision in the reviewed change; **do not auto-approve new behavior**.

This one case does not test provenance ambiguity, dirty worktrees, marker
deletion, multi-agent use, or automatic invocation. Those need separate cases.
The script deliberately **does not launch Codex**, so this is not a fully
automated or deterministic end-to-end model test.
