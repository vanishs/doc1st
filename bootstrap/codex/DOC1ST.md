# doc1st — standalone Codex bootstrap protocol

This template is **self-contained for a target repository** and summarizes the canonical protocol in this project's `protocol/` directory. It is a manually invoked experiment, not an agent daemon.

## Meaning

- Human **commit messages** may express immediate commands; human **diffs** may express changes to longer-term desired state. Interpret both with current project files; a changed file/directory is not necessarily an implementation mandate.
- The agent is a **project coordinator**: move the project toward the desired state, delivering the smallest useful safe tested increment. Partial progress is fine; descriptions alone are not sufficient when unblocked implementation is feasible.
- Human-edited agent code and agent-edited human documents are normal. Do not erase user requirements or turn formal documents into execution diaries.
- A doc1st agent commit does **not** create new human intent. One manually invoked reconciliation is one cycle.

## One cycle

1. Check `git status --porcelain`, current branch/worktree and commit history. If dirty or unclear, do not absorb uncommitted work or switch branches; explain the blocker.
2. Find the latest first-parent commit with `Doc1st-Origin: agent` or `Doc1st-Origin: setup` trailer. That is the baseline/checkpoint. If none exists, do not guess.
3. Read all subsequent commit messages **and per-commit diffs**. For this manual single-branch experiment, interpret human-authorized input; **unmarked commits from third-party agents are ambiguous** and may require clarification. If nothing eligible is new, stop without a new commit.
4. Read relevant current documents, source and tests. Respect prior human decisions. When blocked by a material choice, refer to `.agents/skills/human-decision/SKILL.md`; use concise inline `[doc1st:<natural language>:<stable hex ID>]` markers in valid comments/prose.
5. Reconcile **by doing**: implement and test unblocked work rather than just writing plans. An unresolved choice blocks only dependent work. Don't claim testing not performed or credentials/services not actually used.
6. Inspect diff. When safe and permitted, commit **only changes from this cycle**, with English subject and these trailers:

```text
Doc1st-Origin: agent
Doc1st-Processed-Through: <full SHA of last handled human-intent commit>
```

   An **empty agent checkpoint commit** is allowed when there is no file diff to produce. Do not make more than one checkpoint per cycle.
7. Report delivered work, evidence, and unresolved gaps. Do not treat the agent commit as a trigger. If commit fails, explicitly report that processing was **not checkpointed**.

## Annotation deletion

Natural-language descriptions are **not** selected from a fixed list; semantic meaning comes from a stable English skill definition. Only explicit human-origin decisions/delegation can constitute human approval. **Removing the annotation alone is not approval**. Do not reflexively reinsert a deliberately removed annotation; keep uncertainty separate from the attention marker.

## Limits

Do not rewrite history, force push, destroy unrelated changes, copy secrets into Git, make dangerous tool calls without approval, or change other worktrees. The prototype doesn't automatically watch commits or guarantee exactly-once processing. Apply rule edits made during a cycle only from the next cycle onward.
