# doc1st protocol

This directory describes the working contract for document-first Git coordination. It is **portable**: an agent may follow these rules without a standalone doc1st client. The current scope is a **manual, single-branch prototype**; see the capability boundaries in `../docs/formal/architecture.md`.

- [`coordination.md`](coordination.md): one agent reconciliation cycle and evidence rules.
- [`git-conventions.md`](git-conventions.md): messages, origin, checkpoint trailers, and limitations.
- [`annotations.md`](annotations.md): inline natural-language annotations, syntax, and deletion semantics.
- [`skills/human-decision/SKILL.md`](skills/human-decision/SKILL.md): optional semantic skill with a stable English definition.

**Authority:** This directory defines the general protocol; `bootstrap/` contains adapted instructions for particular agents. Skill definitions extend semantics without requiring the coordination layer to hardcode every classification.

**Stability:** Rules can evolve; record significant changes with reasoning and human authority. Do not treat unfinished proposals as protocol requirements.
