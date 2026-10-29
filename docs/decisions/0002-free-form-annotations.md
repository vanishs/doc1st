# Decision 0002 — Free-form inline annotation semantics

**Status:** Accepted direction, with unresolved edge cases

## Decision

Prefer in-context `[doc1st:<natural-language description>:<stable ID>]` markers. Natural language is unrestricted and may be multilingual; semantic skills provide a **stable English name and definition**, not an alias table. Keep annotations in valid comments/prose. Avoid default sidecar state databases.

## Rationale

Editing and deleting comments feels like normal editing. Notes near the affected passage reduce the need to inspect long new documents. Stable IDs help track an issue across commits.

## Important limitation

Deleting a marker does **not** necessarily answer a question. It may mean the user wants the attention marker removed. If no explicit decision appears, the agent should not claim approval or repeatedly restore it. See `../../protocol/annotations.md`.
