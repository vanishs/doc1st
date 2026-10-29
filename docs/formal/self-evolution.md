# Self-evolving workflow

The project aims to practice its own ideas: **doc1st is designed using doc1st-like coordination**. Both the future product and the workflow that builds it can evolve.

## Product evolution

Experiments and human intent lead to improvements in `setup/` (future client), bootstrap adapters, protocol features, installation, and validation.

## Workflow evolution

Problems observed during real work may lead the agent to propose, test, and revise document organization, annotation phrasing, commit interpretation, agent guidance, and knowledge maintenance.

## Guardrails

- An agent may edit `AGENTS.md`, protocol, and skills, **but** it must explain important changes in a proposal/decision or coherent commit and must not silently weaken human authority, approval requirements, provenance, or archaeology isolation.
- A coordination cycle uses the instructions applicable at its **start**; agent edits to those rules apply to the **next** cycle.
- Human-origin changes, including explicit delegation, govern the scope of authority. Silence, absence of a marker, or a previous agent-authored text is not approval.
- Run experiments before declaring protocol or adapter compatibility. Failed experiments remain useful evidence.
- Preserve normal-tool interoperability. An improvement that only works in one agent or IDE needs a documented trade-off.

A self-improving workflow is an **engineering hypothesis**, not a claim of autonomous self-development. It evolves through inspectable commits and human steering.
