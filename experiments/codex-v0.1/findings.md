# Findings from the first seven cycles

**Overall:** Promising feasibility evidence for **manual** doc1st coordination through Codex. Not a proof of reliable autonomous operation, general compatibility, or correctness of every generated artifact.

## Supported observations

1. **Document input became artifacts:** Codex used a short human planning commit to expand design, label unresolved questions, and record a checkpoint.
2. **Human confirmation was not inferred from silence:** a human-provided model API decision was incorporated while an unrelated product-scope question remained open.
3. **Action could outrun narration:** after a new “execute unblocked work” rule plus commit command, Codex implemented a locally runnable Python launcher and tests instead of only writing next steps.
4. **Message-only commits were meaningful:** a human empty commit prompted model configuration and subsequent Web task UI changes.
5. **Reverse coordination worked:** renaming a CLI option in generated code prompted fixes to related source, tests, and README in a subsequent agent commit.
6. **Marker deletion was not approval:** deleting an annotation alone led to an empty checkpoint and preserved uncertainty in project prose, according to the agent result.
7. **Cross-round context mattered:** the later Web UI increment used the earlier accepted model API convention and did not reinsert a dismissed marker.

## Problems worth designing around

- **Documentation bloat:** early `planning.md` became a mix of proposals, implementation status, test counts, and next-step narration. Formal documents should reflect durable project state, with Git providing execution history.
- **Attribution ambiguity:** experiment commits used the user's Git identity even when Codex produced them; trailers were the main distinction. External agent commits remain unresolved.
- **Environmental leakage:** the agent incorporated LXC-specific constraints from its available environment. Separate development context from product requirements.
- **Verification gaps:** 4/10/11/14 passing tests were reported by the experimental agent. Native macOS/Windows browser behavior, real model provider calls, and more complex agent-task capabilities were not demonstrated.
- **Agent-specificity:** only Codex in one manual workflow was observed. Portability is still a hypothesis to test.

## Proposed follow-up experiments

- A third-party Codex App commit without doc1st trailers, followed by doc1st reconciliation; test whether provenance is safely handled.
- A dirty worktree and multiple worktrees; ensure no data loss or accidental cross-branch commit.
- A large new document with only one in-context human decision: measure review load.
- A same-commit conflict between code diff and message; test interpretation conservatism.
- Re-running a previously processed checkpoint; ensure no unwanted duplicate changes (without claiming exactly-once external effects).
- A protocol self-modification trial with rules frozen for the current cycle and active in the next.
