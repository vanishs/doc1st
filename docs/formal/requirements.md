# Current requirements and constraints

This is the **project-level requirements baseline**, not an assertion that the future standalone client is complete.

## Interaction

- Use **Git commits**, not file saves, as coordination signals.
- Interpret the human commit **message** as a possible immediate instruction and the **diff + current project** as evidence of desired state. Both may be ambiguous and must be interpreted together.
- Support intentional **empty commits** with meaningful messages.
- Allow the human to edit any text artifact; an agent may reconcile any relevant document, code, or test.
- Agent-produced commits are checkpointed results and must not themselves trigger another cycle.
- Permit partial implementation and continue work independent of unresolved choices.
- Track processed commits to avoid blind replay; commit author name alone does not prove provenance.

## Content and annotations

- Repository content is written in English; conversations can use the user's language.
- Use minimal in-place annotations shaped like `[doc1st:<free natural language>:<stable id>]`, wherever the file format permits prose/comments.
- The meaning of a human-decision annotation comes from a stable English skill definition, **not** a fixed multilingual alias list.
- Removing a marker alone is **not** approval; do not repeatedly restore a marker that the user deliberately removed.
- Avoid a sidecar annotation database as the default solution. Some strict formats cannot contain comments: do not invalidate them to satisfy a marking convention.

## Runtime and compatibility

- The **bootstrap path** should work through existing agents with project instructions and skills and manual invocation.
- A future **standalone client** may be developed under `setup/`, including source, tests, install mechanisms, and packaging; its API/language/architecture are not decided.
- Remain compatible with normal IDEs, Git operations, and multiple agent CLI/apps. Do not require exclusive control of the working tree.
- Do not assume external-agent commits are human simply because they lack doc1st trailers. See unresolved attribution design.
- Do not claim automatic wake-up, true multi-agent concurrency, or broad OS validation before measured evidence exists.

## Quality and governance

- Use Git for history rather than accumulating per-run logs in formal documents.
- Never assume an agent-generated suggestion became an approved requirement merely because it was not edited.
- Keep archaeology isolated from normal work; human must explicitly request historical investigation.
- The human/agent authority boundary must not change silently through agent self-modification.
