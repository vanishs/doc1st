# Agent guidance for the doc1st repository

This repository is developing **doc1st**, using its own document-first ideas wherever practical. Read `README.md` and `docs/README.md` to locate the current authority before substantial work.

## Language

- **Write all repository artifacts in English**: Markdown, source comments, test names/descriptions, commit subjects/bodies, newly created paths, and docs. Preserve external quotations as evidence when necessary; explain them in English.
- **Speak to the user in the user's language** unless they request otherwise. The language of conversation does not change repository language.
- Keep the product and protocol name exactly **`doc1st`** (lowercase).

## Operating modes

- **Ordinary agent work:** follow the user's current request. Do not silently scan and reconcile unprocessed commits.
- **doc1st reconciliation (opt-in):** when explicitly asked to run a doc1st cycle, read `DOC1ST.md`, `protocol/coordination.md`, `protocol/git-conventions.md`, and relevant skills. Execute **one** cycle; do not assume automatic wake-up.
- Use the repo's current applicable protocol at cycle start. Rule edits created during that cycle take effect **next cycle**, not retroactively.

## Knowledge and evidence

- Preferred reading order: `docs/formal/` + `protocol/` → relevant `docs/decisions/` → active `docs/proposals/`, `experiments/`, `docs/research/`, `docs/ideas/` as needed.
- `bootstrap/` adapts the protocol to existing agents; it is **not** an independent source of normative truth.
- `docs/archive/` contains superseded curated knowledge, not active requirements.
- **Archaeology quarantine:** Do not read, search, summarize, cite, or mine `archaeology/` during ordinary tasks or ordinary doc1st coordination. Enter it **only when the human explicitly asks for archaeology / historical investigation**, or explicitly names material there for inspection. It contains non-authoritative historical artifacts. See `archaeology/README.md`.
- Label proposed design vs accepted decision vs tested observation. Never promote an agent guess or an unverified experiment into a user-approved requirement.

## Keep moving, but don't overreach

- Reconcile by **doing**, not merely describing: implement and validate the smallest coherent safe increment when feasible; unresolved choices block only dependent work.
- Edit any relevant repository file, including human-created documents, while preserving user requirements and source attribution. Avoid duplicate sources of truth and accumulating activity logs in formal documents.
- Document-first does not mean documents-only; code, tests, and packaging are also artifacts.
- Never present proposed future behavior as implemented or tests as run unless they were actually run.
- Reuse existing Git, IDEs, and agent CLI/apps; avoid inventing a competing agent platform without evidence.
- Do not use `archaeology/` as a shortcut when active knowledge is missing; explain the gap or create a proposal instead.

## Evolving the rules

- Agents **may propose and modify** `AGENTS.md`, protocol documents, skills and workflow material, with legible rationale and a reviewable diff.
- Do **not** silently weaken the human-intent boundary, provenance, consent, safety, or archaeological quarantine. Changes to those governance invariants require an explicit human-origin decision.
- Changes to protocol and agent behavior are visible in Git and apply to subsequent cycles.
- For substantial behavior changes, update formal docs, the relevant decision/proposal, and derivative bootstrap instructions when appropriate, without copying the whole protocol into multiple places.
