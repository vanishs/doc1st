# Documentation map and authority

This repository separates **current instructions** from **exploration** and **historical evidence**. Classification helps agents discover information, but it does **not** constrain which files humans or agents may edit.

| Location | Meaning | Default authority |
| --- | --- | --- |
| `formal/` | Current project vision, requirements, principles, architecture, and self-evolution rules | Primary project guidance |
| `../protocol/` | Current doc1st coordination and annotation contract | Protocol authority |
| `decisions/` | Accepted choices, rationale, consequences, and dates | Authoritative context unless superseded |
| `proposals/` | Concrete approaches, open questions and trade-offs | Not adopted yet |
| `ideas/` | Brainstorms and speculative alternatives | Non-binding |
| `research/` | External references and comparative analysis | Evidence; check accuracy and freshness |
| `../experiments/` | Reproducible tests, results, and limitations | Observations only |
| `archive/` | Curated material that used to guide work but is superseded | Historical, not current |
| `../archaeology/` | Raw historical materials for explicit investigations only | **Do not consult by default** |

## Knowledge lifecycle

Idea/research → proposal → experiment and/or explicit human decision → formal/protocol update → bootstrap/client implementation. This is an **example trajectory, not a mandatory gate**: a human commit may directly revise formal requirements, and implementation can expose needed document changes.

- **Present state over narration:** formal docs should describe what is true, intended, and unresolved today—not append a diary after each agent commit. Git history is the diary.
- **Evidence matters:** separate observed behavior, interpretation, confidence, and not-yet-tested claims.
- **No silent promotion:** an agent-produced proposal cannot turn into a human-approved requirement simply because nobody edited it.
- **Avoid duplication:** link to the protocol rather than copying it into multiple agent templates; keep bootstrap adapters in sync.
- **Keep navigation discoverable:** update this index when new top-level categories are needed. More files are not automatically better.
