# Future doc1st client: source, install, packaging

**Status: not implemented.** This is the reserved home for **everything belonging to a future standalone doc1st client**, including its code, tests, installation guidance/scripts, and releases. It is not a requirement to use doc1st-like manual coordination today.

- [`src/`](src/README.md): eventual client/coordinator source and adapters.
- [`tests/`](tests/README.md): client tests (not the unrelated Codex experiment tests).
- [`install/`](install/README.md): user installation, setup, upgrade and uninstall mechanisms.
- [`packaging/`](packaging/README.md): distributables, platform integration and versioning.

The implementation language, supported OS integration and lifecycle contract are **not selected yet**. Work should be guided by `../docs/formal/`, `../protocol/`, and evaluated proposals. Do not add an unnecessary replacement agent or IDE as a hidden architectural assumption.

Expected principles for any client: optional install, explicit control over when commits are processed, clean coexistence with other agents/worktrees, origin tracking, recoverable checkpoints, and no autonomous escalation of permissions.

For a usable no-client experiment today, see [`../bootstrap/codex/`](../bootstrap/codex/README.md).
