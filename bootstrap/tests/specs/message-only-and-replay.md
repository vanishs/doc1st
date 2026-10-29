# Behavioral spec: message-only intent and replay

**ID:** `message-only-and-replay`
**Basis:** [Minimal bootstrap trial](../../../experiments/codex-bootstrap-minimal/README.md).
**Contract:** [Requirements](../../../docs/formal/requirements.md), [coordination](../../../protocol/coordination.md).
**Status:** Proposed regression expectation derived from a small, human-delegated synthetic experiment.

## Setup and stimulus

Copy the current Codex bootstrap into a fresh local Git repository. Commit a
`Doc1st-Origin: setup` baseline containing exactly `Status: pending\n`.
Add an **empty** synthetic human-delegated input commit requesting
`Status: ready\n` in `status.txt` and no unrelated changes.
Request one manual doc1st reconciliation cycle.

## Expected behavior

One agent commit changes only `status.txt` to the requested bytes, with
the correct origin and processed-through trailers. The worktree is clean.
Invoke another cycle **without new input**: no new commit or file change.

## Machine-checkable contract

The JSON block is the **single machine-readable expected state**; the
surrounding prose explains its meaning and experimental provenance.

```json regression-case
{
  "id": "message-only-and-replay",
  "fixture": "message-only-and-replay",
  "expect": {
    "head": "one-agent-checkpoint",
    "tree": "changed",
    "changed_paths": ["status.txt"],
    "files": {"status.txt": "Status: ready\n"},
    "git_status": "",
    "replay": "unchanged"
  }
}
```

## Human review

Confirm that the agent interpreted the **message-only** commit as human-delegated
intent, not a change in the file diff. Independent checks determine Git and
file state, not the agent's internal reasons.
