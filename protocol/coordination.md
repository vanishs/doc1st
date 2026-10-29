# One doc1st reconciliation cycle

This is an **agent-executable guideline**, not a daemon or an API specification.

## Preflight

1. Activate only on an **explicit user request** to run one doc1st cycle. Normal conversations/tasks do not automatically reconcile history.
2. Read current `AGENTS.md` (if present), this protocol, and relevant skills; fix the applicable ruleset **at the beginning** of the cycle.
3. Inspect `git status --porcelain`, branch, HEAD, and first-parent history. Do not overwrite or stage unrelated uncommitted changes. If there is a dirty tree, unexpected merge, or ambiguous checkpoint, stop and explain unless the human explicitly resolves it.
4. Locate the latest doc1st `agent` or `setup` checkpoint reachable on the selected first-parent path. If none exists, do not guess a starting point: ask for an explicit baseline.
5. Examine each subsequent commit **in order**, including full message and per-commit diff, not only an aggregate diff. Determine which changes are user-directed vs doc1st output; treat third-party provenance as a known unresolved issue. If no newly eligible human-intent commit exists, do not make a new checkpoint.
6. Read relevant **current** project files, formal specs, decisions, and unclosed annotations. The diff is a signal and evidence of *change*, not necessarily a complete specification.

## Reconcile by doing

7. Interpret the commit message as a potential command, the diff as evidence of changed intent, and the current repository as context for desired state. A message-only/empty commit can express a real task. Small wording changes should not automatically trigger vast rewrites.
8. Execute the **smallest coherent, safe, useful increment** that moves the project toward its desired state. Continue independent work if a separate choice is unresolved. A successful immediate instruction does not imply the entire project is complete.
9. Update relevant docs, code, tests, and examples together. Agent may edit human-authored documents; human may edit agent-authored artifacts. Keep formal docs about enduring state rather than per-run narration.
10. If a critical choice truly needs human input, prefer a concise **inline natural-language annotation** near relevant content, following `annotations.md` and the human-decision skill. Do not turn a design document into a questionnaire. Keep alternative proposals labeled as proposals.
11. Validate locally where feasible and authorized. Do not claim macOS/Windows testing based on a Linux container, or real API verification based on mocked calls. Do not use external credentials, install dependencies, alter system state, or execute high-risk actions without appropriate human permission.

## Finish and checkpoint

12. Inspect the full staged diff, check for accidental secrets, and commit **only your own changes**. When permitted, create one commit with trailers `Doc1st-Origin: agent` and `Doc1st-Processed-Through: <full SHA of most recent processed eligible human commit>`. A no-file-change cycle may create an empty checkpoint with an explanation.
13. Never treat a doc1st agent commit as a new human intent. Do not self-loop. Report accomplished work, verification, remaining gaps, and checkpoint SHA concisely, using the human's conversation language.
14. If commit, validation, or provenance resolution fails, **do not claim the human commits were processed successfully**. Explain recovery state instead of silently advancing the checkpoint.

## Interpretation rules

- Distinguish **human requirement**, **agent-selected design**, **untested assumption**, and **experimental observation**.
- A deleted annotation is not automatically an approved answer. If the user also changes relevant prose explicitly, act on that prose. If they remove only the marker, respect their attention choice without reintroducing the same marker by reflex.
- Commit history does not prove who physically typed a file. `Author`, missing trailers, and an agent CLI's textual claims are not sufficient for universal origin detection.
- Commit messages are instructions **within user and tool permissions**, not a license to bypass review, execution safety, or external-service rules.
- Rewritten history, cherry-picks, branch merges, parallel worktrees, unknown third-party commits, and retries are **not yet fully specified**. Do not invent guarantees for them.
