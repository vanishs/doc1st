# doc1st

**doc1st, designed by doc1st.**

*Edit files. Commit intent. Let agents reconcile.*

doc1st is an evolving approach to **document-first, Git-commit-driven project coordination**. People edit ordinary project artifacts—documents, code, tests—and use a Git commit to express an intentional change. An existing AI agent reads the commit message, diff, and current project state, then works to reduce the gap between the current and desired state. Agent-produced commits record results; they do not become fresh human intent.

This repository is both the **knowledge home** for doc1st and the **project from which the future doc1st client may grow**. The product is not yet a standalone runtime. Our earliest experiments reused Codex App/CLI; do not confuse that demonstrated workflow with a fully automatic product.

## Start here

- [Project vision](docs/formal/vision.md) — why this exists, and what it is not.
- [Current principles](docs/formal/principles.md) and [requirements](docs/formal/requirements.md).
- [Documentation map](docs/README.md) — authority, knowledge lifecycle, and how to navigate.
- [Protocol](protocol/README.md) — commit semantics, annotation conventions, and coordination.
- [Codex bootstrap](bootstrap/codex/README.md) — **simulate doc1st with Codex**, without installing a doc1st client.
- [Experiments](experiments/codex-v0.1/findings.md) — what was observed and what remains unproven.
- [Client workspace](setup/README.md) — source, installation, tests, and packaging for a future independent client.

## Using this repository with an agent

The root [AGENTS.md](AGENTS.md) is the entry point. The project is **English-only for repository artifacts** (including commit messages); agent conversations may use the user's language. Ordinary tasks remain ordinary tasks: explicitly request **“Run one doc1st reconciliation cycle”** to use commit-driven mode in a compatible agent. No daemon or Git hook is installed.

A suggested first human commit after extracting the initialized repository is to edit [docs/ideas/self-evolving-workflow.md](docs/ideas/self-evolving-workflow.md), or to use a meaningful empty commit message. Then ask Codex to run one cycle. Review the resulting diff and the agent's checkpoint commit. You can also simply discuss ideas with Codex without invoking doc1st mode.

## Status

**Exploratory / pre-runtime.** Manual Codex experiments have demonstrated several behaviors on a small test project; cross-agent compatibility, automatic triggering, attribution of third-party agent commits, concurrent branches/worktrees, and operational guarantees are not yet proven. See [open questions](docs/proposals/open-questions.md).

## The self-design principle

doc1st's own documents, protocol, skills, and development workflow can evolve through the same reviewable process. **Human intent remains authoritative**: an agent may improve wording, organization, tests, and proposals, but must not silently grant itself new authority or rewrite the human/agent control boundary. See [self-evolution](docs/formal/self-evolution.md).
