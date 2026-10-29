---
name: doc1st-human-decision
description: Handle unresolved human decisions using short, free-language inline annotations during doc1st coordination.
---

# Human Decision Required

**Stable semantic type:** `1`  
**Canonical English name:** `Human Decision Required`

**Canonical English definition:**

> An unresolved requirement, design choice, or proposed decision that requires explicit human input or approval. An agent must not treat an unconfirmed proposal as an established human requirement. Independent work may proceed, but genuinely blocked work remains unresolved. Only human-originated input can resolve or delegate the decision; deleting an annotation alone does not prove approval.

A marker looks like `[doc1st:<any natural-language note>:<stable hex ID>]`, e.g. `[doc1st:Please decide whether shell commands are allowed:7e1a9b20]`. Natural-language text can be in **any language** and is **not** a keyword/alias table. Interpret it using the canonical definition and context.

Put as few markers as possible directly next to the relevant prose/code, using valid file comments. Do not turn a document into a multi-choice interview or corrupt a strict no-comment format. Preserve the ID of the same issue across edits.

When a human commit removes a marker and explicitly decides or delegates the issue, act on the content. When the marker is **only deleted**, do not claim approval and do not automatically reinsert it. Remaining uncertainty may live in ordinary project text; continue unrelated safe progress. An agent's own proposal is never human approval.
