---
name: doc1st-human-decision
description: Interpret unresolved human choices in file- and Git-driven projects; use minimal natural-language inline annotations without turning the project into a chat questionnaire.
---

# Human Decision Required

**Stable semantic type:** `1`  
**Canonical English name:** `Human Decision Required`

**Canonical English definition:**

> An unresolved requirement, design choice, or proposed decision that requires explicit human input or approval. An agent must not treat an unconfirmed proposal as an established human requirement. Independent work may proceed, but genuinely blocked work must remain distinguishable from completed work. Only human-originated input can resolve or delegate the human decision; annotation deletion alone does not prove approval.

## Recognizing the type

The marker's natural-language phrase is free-form. Phrases such as "Needs confirmation", "Could you decide this?", or a comparable description written in another language may be associated with this type **through semantic understanding**, not a keyword or translation list. Do not force a canonical phrase into the file.

A suitable inline marker:

```markdown
## Task execution

[doc1st:Clarify whether the first version may run shell commands:7e1a9b20]

The first version's shell-command permissions are still undefined.
```

## Operational behavior

- Prefer an **actual tentative design paragraph** with one small unresolved point, not an A/B/C questionnaire.
- Introduce a marker only when human input materially affects the product or safe next steps. Continue safe independent implementation.
- Preserve stable IDs for the same issue; don't assign the same ID to unrelated questions.
- If a human commit explicitly answers or delegates the issue, reconcile docs and artifacts; don't confuse unedited agent proposals with human approval.
- If a human removes just the marker, **do not claim approval** and **do not reflexively reinsert the same marker**. Respect the removal as an attention preference; underlying uncertainty may still exist.
- Distinguish human decisions from technical defaults chosen by the agent. Record important agent assumptions as such, without flooding files.
- Use only valid comments or prose for annotations. Never invalidate strict JSON or binary artifacts.

This is a **semantic skill**. The doc1st core need only understand the marker envelope and Git provenance; it need not hardcode `Human Decision Required` or a translated vocabulary.
