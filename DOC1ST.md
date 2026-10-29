# doc1st: agent entry point

This file is the **short route** into doc1st mode for agents that load an `AGENTS.md` at the repository root. It does not duplicate the normative protocol.

When the user explicitly requests **one doc1st reconciliation cycle**:

1. Read `protocol/coordination.md`, `protocol/git-conventions.md`, and `protocol/annotations.md`.
2. Read `protocol/skills/human-decision/SKILL.md` when a decision needs human attention.
3. Verify a clean worktree and select the intended branch/worktree; find the most recent doc1st checkpoint and inspect subsequent commit messages and diffs. Treat third-party unmarked commits as **ambiguous provenance**, not certainly human.
4. Reconcile current project artifacts toward the intended state. Do useful unblocked work and validate it; avoid turning the session into a series of chat questions.
5. If authorized and safe, commit only your own changes with `Doc1st-Origin: agent` and `Doc1st-Processed-Through: <full SHA>` trailers; empty checkpoint commits are permitted. Never silently consume user changes.
6. Report what changed, was tested, and remains unresolved. One cycle ends here.

No automatic Git listener or runtime exists in this repository yet. An agent's new commit is **not** fresh human intent. See the protocol for limitations and recovery behavior.
