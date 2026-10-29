# Bootstrap: emulate doc1st with existing agents

These are **optional, portable adaptations** that let existing agent tools follow doc1st-like rules without installing a new runtime. The authoritative semantics live under `../protocol/`.

- [`codex/`](codex/README.md) — usable Codex App/CLI prototype based on manual experiments.
- [`claude-code/`](claude-code/README.md) — compatibility concept only; not tested or packaged.

These adapters do **not** provide automatic commit watching, true cross-tool provenance, replay guarantees, or agent independence. Avoid splitting semantic definitions into divergent copies; review adapters whenever `protocol/` changes.
