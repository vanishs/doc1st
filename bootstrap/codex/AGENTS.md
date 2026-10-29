# Agent instructions for a doc1st-enabled repository

This project optionally uses **doc1st**: document-first project coordination with Git commits as intent boundaries.

When the human explicitly asks to **run a doc1st reconciliation cycle**, read and follow `DOC1ST.md` and the relevant skill under `.agents/skills/human-decision/`. During normal chats/tasks, do **not** silently start a commit reconciliation.

The repository's own instructions take priority for project context. Do not bypass user approvals, safety constraints, Git worktree boundaries, or external-tool permissions. A doc1st agent commit is execution output, not a fresh human instruction.

Prefer English for repository artifacts. Converse in the user's language. The product name is `doc1st` (lowercase).
