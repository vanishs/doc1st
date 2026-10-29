# Codex manual coordination experiment v0.1

**Status:** Seven user-reported coordination cycles, Oct 28–29, 2026 (America/Los_Angeles). The original executable Git repository and complete browser sessions are **not bundled** in this doc1st project. This folder contains a curated record derived from the user's supplied commit summaries and selected diffs, not an independently replayed test suite.

## Initial target project

A generic AI agent CLI for macOS/Windows, with a browser-based Web UI automatically opened at launch. The human first committed a short planning file, then used Codex App with a small `AGENTS.md` + `DOC1ST.md` + human-decision skill to manually request each reconciliation.

## Recipe for reproduction

1. Set up an ordinary Git repo and adopt `../../bootstrap/codex/` as the initial adapter; record an explicit baseline (`Doc1st-Origin: setup`).
2. Create/edit a planning file and commit it. Ask Codex: **`Run one doc1st reconciliation cycle.`**
3. Review the result commit, trailer, files and tests. Make another human commit that changes either docs, code, or only the commit message, and run another cycle.
4. Observe whether Codex distinguishes human decisions, agent choices, missing implementation, and unconfirmed requirements.
5. Capture Git diffs and actual test commands/results; compare across agents/worktrees before extrapolating.

The supplied pilot used a local LXC environment for tests. LXC results **do not** establish native macOS/Windows desktop behavior.

See [timeline](timeline.md) and [findings](findings.md).
