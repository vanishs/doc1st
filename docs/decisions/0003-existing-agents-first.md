# Decision 0003 — Existing agents first

**Status:** Accepted direction

## Decision

Start by **teaching existing agent CLI/apps the doc1st method** with instructions and skills. Maintain a Codex bootstrap adapter. A future optional client may live in `setup/`, but it must not be a prerequisite for usable doc1st-like project collaboration.

## Rationale

Avoid locking a user out of Codex App, other agents, normal Git workflows, or any preferred IDE. Protocol knowledge is portable even if automatic triggering and strict guarantees later need a small runtime.

## Consequences

- Codex manual experiments are evidence, not proof that other agents behave identically.
- `protocol/` owns semantics; `bootstrap/` owns agent-specific packaging.
- Runtime design and third-party commit attribution remain open.
