# Architecture: current working model

## Layers (conceptual, not a promised implementation)

1. **Shared repository:** plain files and Git history, editable with ordinary tools.
2. **doc1st protocol:** commit intent semantics, origin/checkpoint conventions, inline annotations, coordination guidance and semantic skills.
3. **Existing agent:** Codex or another compatible agent reads the repository and executes a manually requested coordination cycle.
4. **Optional future client (`setup/`):** may detect eligible commits, invoke a selected agent CLI, handle retries and concurrency. No requirement to replace the agent itself.

```text
Human edits files / writes commit message
                  |
             Human commit
                  |
        Existing agent + doc1st rules
                  |
         Reconcile current project
          /        |          \
       Docs       Code        Tests
                  |
         Agent result/checkpoint commit
                  |
        Await another human intention
```

## Two time scales

- **Immediate instruction:** what the latest commit message requests now (it can be infeasible or partially fulfilled).
- **Desired project state:** the evolving interpretation of repository artifacts and past accepted decisions. The current state may remain short of that goal after a successful immediate task.

Example: a human commits tracked `src/` and `dist/` directories with `python hello world` as the message. The agent might generate `src/hello.py`, while recognizing that `dist/` **might** imply distributable output, not assuming that the user has requested a particular package format. Directory changes alone are clues, not conclusive requirements.

## Why the first prototype has no runtime

Codex can read instructions, Git history, and project artifacts when explicitly invoked. This suffices to test semantic coordination, without claiming it can wake itself on a Git commit. The coordination rules are in `protocol/` and the compatible template in `bootstrap/codex/`.

## Boundaries

Current manual prototype: one branch, clean worktree, one coordination cycle at a time. Branch/worktree concurrency, third-party origin attribution, automatic triggering, retry semantics, and safe external side effects are **open engineering problems**. See `../proposals/open-questions.md`.
