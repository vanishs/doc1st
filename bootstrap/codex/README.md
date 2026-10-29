# Codex bootstrap adapter

**Purpose:** Simulate doc1st in an ordinary Git repository using Codex App/CLI. This is a **manual, opt-in** workflow, not a released doc1st client.

## Install into another project

1. Copy `AGENTS.md`, `DOC1ST.md`, and `.agents/skills/human-decision/SKILL.md` from this folder into the **root** of the target Git repository. **Merge** `AGENTS.md` with existing instructions rather than overwriting them. Keep the `.agents/` directory (including hidden files) intact.
2. Initialize Git if needed. Create an initial baseline commit with `Doc1st-Origin: setup` in the commit body; do this before beginning doc1st input commits. If the repository already has history, **do not rewrite it**: explicitly choose and record a baseline and review the protocol first.
3. Edit project artifacts and make a human commit (which may have a meaningful message-only empty diff).
4. Open the same branch/worktree in Codex App and ask: **`Run one doc1st reconciliation cycle.`** This is the single required conversation command for the prototype. It won't self-trigger from Git.
5. Review the agent's result commit and its `Doc1st-Origin` and `Doc1st-Processed-Through` trailers. Edit and commit again to continue.

If using the **doc1st project repository itself**, you do **not** need to install this adapter: root `AGENTS.md` and `DOC1ST.md` already refer to `protocol/`.

## Known limits

- A clean worktree and simple single-branch history are expected.
- Never assume every unmarked commit came from a human: external agents can also commit.
- Ordinary Codex chat does not automatically become doc1st mode.
- Copying templates gives instruction compatibility, **not** access to or verification of any new agent execution permissions.

This adapter was inspired by the tested v0.1 instructions, then revised for clarity. The revised packaging itself needs validation in future experiments.
