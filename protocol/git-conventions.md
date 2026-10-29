# Git conventions

Git is the shared event/history substrate; doc1st does not replace or require a fork of Git.

## Inputs

- **Human commit diff:** possible change in long-term intent. Read modified text *and* context, including deleted text.
- **Human commit message:** potential immediate instruction, question, or explanation. An intentionally empty commit with a meaningful message can be valid.
- **Current files:** evolving knowledge of the desired state and realized artifacts; not all files carry imperative instructions.
- **doc1st agent commit:** result/checkpoint; **does not trigger** another doc1st reconciliation.

Commit messages are not the only source of truth, and a change to file layout (`src/`, `dist/`) is not automatically a demand for a particular build artifact.

## Trailers

```text
<short English summary>

Doc1st-Origin: agent
Doc1st-Processed-Through: <full SHA>
```

A seed commit may use:

```text
Doc1st-Origin: setup
```

The `setup` commit is a baseline and not a user instruction. These are conventional Git message trailers, not a replacement for standard Git history. `Doc1st-Processed-Through` refers to the last processed **eligible human-intent commit** of that cycle; a checkpoint is only valid if it is on the relevant ancestry and represents the processed range.

## Minimal history algorithm (single-branch experiment)

1. Check that the intended worktree is clean and the active branch is correct.
2. Walk the selected branch's **first-parent** history back to the latest valid doc1st checkpoint (`agent` or `setup`).
3. Examine **every** subsequent commit in chronological order, with per-commit message and diff. Do not omit intervening commits or double-count ones already covered.
4. Treat commits known to be doc1st output as effects, not intent. For **unmarked third-party commits**, determine eligibility from explicit human invocation/evidence; do not claim that missing origin trailers prove human authorship.
5. Handle the eligible human range, make a coherent change, and record a new agent checkpoint or empty checkpoint. If provenance is ambiguous enough to affect execution, pause and request clarification.

The `Doc1st-Processed-Through` field is a useful checkpoint, **not an exactly-once guarantee** for side effects. Replays, crashes, forced branch rewrites, concurrent worktrees, and external services require additional design.

## Ownership and portability

- Commit `Author` is not a reliable human/agent classifier; Codex App and humans may share the same configured Git identity.
- Do not force-push, rewrite user commits, edit other worktrees, or push changes automatically.
- A doc1st checkout must remain usable through conventional IDEs, Git, and unrelated agent tools.
- If a third-party agent generates and commits changes, its relationship to human intent remains an open question; see `../docs/proposals/commit-origin-attribution.md`.
