# Principles

1. **Artifacts over transcript:** the current repository state is the durable collaborative surface; chat is optional and transient.
2. **Commit as intent boundary:** uncommitted edits are not doc1st signals. A human commit may contain edits, a message-only instruction, or both.
3. **Project coordination, not task-only completion:** reconcile toward the broader desired state without confusing local command completion with overall project completion.
4. **Human authority, agent initiative:** only human-origin input establishes human approval or delegates a decision. Agents make reviewable technical choices within those boundaries.
5. **Any relevant file can evolve:** humans may edit generated code; agents may update human-authored docs. No artificial file-ownership split.
6. **Reconcile by doing:** deliver safe, coherent, tested increments instead of describing future work alone. Permit honest partial success.
7. **Attention is scarce:** show minimal, in-context natural-language markers when human attention is truly needed; do not flood humans with questionnaires.
8. **Agent output does not re-trigger intent:** a doc1st agent commit records effects/checkpoints, not a new human request.
9. **Portability first:** existing Git + IDE + agent CLI/app should remain usable; doc1st must be optional and removable.
10. **Evidence and uncertainty:** distinguish experiments, hypotheses, proposals, adopted decisions, and deployed features.
11. **Self-evolution with a boundary:** the project may improve its own instructions and workflow; an agent cannot silently expand its own human-level authority.
12. **Minimal core, extensible meaning:** deterministic commit/marker handling in the core; semantic interpretation can live in reusable skills.
