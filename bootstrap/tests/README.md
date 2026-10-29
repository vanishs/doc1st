# Bootstrap behavioral regression specifications

**Scope:** Codex bootstrap adapter, manually invoked Git coordination.
**Purpose:** Notice behavioral drift after a bootstrap upgrade without
silently redefining what the project considers correct.

The Markdown files in [specs/](specs/) are the **source of expected behavior**.
Each names its historical experiment, applicable active protocol, setup,
stimulus, observable expectation, and separate human-review question.
The fenced JSON block in each Markdown file is the runner-readable contract;
there is no independently maintained golden-output file.

## Initial cases

| Case | Evidence | What it protects |
| --- | --- | --- |
| [Message-only and replay](specs/message-only-and-replay.md) | Minimal Codex trial | Empty human-intent commit is handled once, then not replayed |
| [Dirty worktree](specs/dirty-worktree-stop.md) | Boundary trials | Uncommitted user changes are preserved |
| [Third-party input](specs/unapproved-third-party-stop.md) | Boundary trials | Explicitly unapproved third-party request is not adopted |
| [Marker deletion](specs/marker-deletion-no-approval.md) | Boundary trials | Deleting attention is not approving a product decision |

Existing reports under [experiments/](../../experiments/) remain **historical
evidence**; they are never rewritten to match future behavior. These proposed
expectations have current-protocol support but remain reviewable, not automatic
new normative requirements. The tests reproduce the **narrow synthetic
conditions**, not universal agent correctness.

## Run with Codex App or another manual invocation

Requires Python 3.9+, Git, and an agent that can operate in a disposable
Git worktree. From the doc1st source checkout:

\`\`\`sh
python3 -m unittest discover -s bootstrap/tests -v
python3 bootstrap/tests/codex_regression.py cases
python3 bootstrap/tests/codex_regression.py prepare dirty-worktree-stop /tmp/doc1st-dirty
\`\`\`

Open \`/tmp/doc1st-dirty\` in Codex; ask exactly:

> Run one doc1st reconciliation cycle.

Then inspect the agent report and check the actual Git/file state:

\`\`\`sh
python3 bootstrap/tests/codex_regression.py verify /tmp/doc1st-dirty
\`\`\`

For \`message-only-and-replay\`, after a successful first verification, ask
Codex to run **one more cycle without any new input**, then run
\`verify-replay /path/to/fixture\`.

Use a **fresh fixture directory for each run**. Preparation refuses to
overwrite existing fixtures. Test metadata and optional execution logs stay
alongside the fixture, outside its Git worktree. A SHA-256 of the source
Markdown prevents silently changing a case between preparation and
verification.

## Optional: drive Codex CLI

If \`codex\` is installed and configured, one command can prepare, invoke
\`codex exec\`, and verify the observable results:

\`\`\`sh
python3 bootstrap/tests/codex_regression.py run-cli message-only-and-replay /tmp/doc1st-cli-1
\`\`\`

The CLI mode runs the second replay invocation automatically for the relevant
case. This is an **opt-in real agent call**, may incur model usage, depends on
local tool permissions, and has not been validated against a real Codex CLI
in this repository change. It does **not** bypass sandbox or approval settings.

## What PASS means

- \`STATE PASS\` means independent checks of Git history, checkpoint
  trailers, changed paths, working/committed file bytes, and worktree status
  matched the Markdown contract.
- **It does not prove the agent was invoked in manual mode.** A blocked case
  can exhibit the expected unchanged Git state even if no agent ran.
- It does not prove *why* the agent stopped, or that it never temporarily
  made and reverted changes. Review the actual invocation log/agent report
  using the case's **Human review** section.
- A CLI exit code of 0 is not a pass. A missing checkpoint, wrong result, or
  unintended changes should be investigated, not automatically accepted.
- The Python unit tests of the **runner** simulate Git outcomes and are
  not results of running the real Agent.

## Handling drift

When the observed behavior differs, compare: (1) the applicable
\`protocol/\` and accepted decisions, (2) the unchanged historical experiment
record, (3) the current bootstrap diff, and (4) independently checked
artifact/Git state plus the agent's explanation. Then explicitly decide
whether to correct the bootstrap, update an obsolete case, or classify an
environment/agent failure and rerun. **Never auto-rebaseline on failure.**

More cases (other agents, hidden provenance, concurrency, worktree variants,
protocol self-modification, etc.) require their own scoped specifications
and evidence rather than extrapolating guarantees from these four.
