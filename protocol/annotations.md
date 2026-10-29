# Inline annotations

## Design

Use annotations **in ordinary file content** to direct attention where the problem occurs. Prefer small inline notes over central questionnaire documents or a sidecar state database.

```text
[doc1st:<free natural-language description>:<stable unique ID>]
```

Example, in Markdown:

```markdown
## API configuration

[doc1st:Please clarify whether the first version needs offline models:8f3a2c91]

The first version supports a configurable OpenAI-compatible API.
```

Example, in TypeScript:

```ts
// [doc1st:Confirm whether anonymous local requests are allowed:52d194ea]
const allowAnonymous = false;
```

## Parsing versus meaning

- The **literal prefix** `doc1st:` and trailing **stable ID** are machine-friendly anchors. Use a locally unique 8–12 digit hexadecimal ID in the experimental convention; retain it across edits/moves of the *same* issue, never reuse it for a different issue.
- The middle text is **arbitrary natural language**, not an enum and not a multilingual alias list. Interpret it with context and semantic skills; do not translate or normalize the user's words merely to match a keyword.
- Semantic skills may publish a **stable English name and English definition** to help the agent recognize an intended type in any language. The original marker text remains free-form.
- Syntax parsing can be deterministic; deciding whether a description matches a semantic type is probabilistic and may require context.

## Deletion and lifecycle

- **Present:** the annotation explicitly requests attention or flags an unresolved issue; it does not automatically freeze the entire document.
- **Removed with an explicit decision:** act on the changed content; only human-origin intent can supply human approval or delegation.
- **Removed alone:** **not** evidence of confirmation. Do not silently approve, but do not mechanically reinsert the same unwanted marker. The underlying uncertainty may remain in prose or be tracked as an open design gap.
- There is no requirement to create `[doc1st:approved:...]` markers. Ordinary edit/delete behavior is intentional.
- Different questions may need different natural-language phrasing. Use a small number of high-value markers, not a badge on every agent design choice.

## Format safety

Only insert into syntactically valid **prose or comment locations**. Strict JSON and other formats without comments **must not be broken** by inline markers. For those formats, document the issue in an existing nearby human-readable artifact when necessary; this is a limitation of the current no-sidecar preference, not permission to corrupt files.

See `skills/human-decision/SKILL.md` for one optional semantic behavior. More meanings can be added as skills without growing the core protocol into a fixed state-machine vocabulary.
