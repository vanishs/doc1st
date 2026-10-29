# Knowledge from small bootstrap trials

**Status:** Evidence synthesis and proposed follow-ups; no new protocol requirement.
**Date:** 2026-10-29.

Sources: [minimal change and replay](codex-bootstrap-minimal/README.md), [boundary trials](codex-bootstrap-boundaries/README.md), and their independent Git/file checks. Inputs were synthetic, explicitly framed, and small. Human delegation authorized the experiments; agent-generated fixtures were not independently authored human decisions.

## Cycle outcomes need more than a success flag

The trials exhibited distinct outcomes:

| Outcome | Observed effect | Interpretation |
| --- | --- | --- |
| Requested change completed | Artifact changed; valid checkpoint recorded the input. | Concrete work completed and checkpointed. |
| Input handled without a file change | One empty checkpoint; uncertainty retained. | Input was processed without approving a proposal. |
| No eligible new input | HEAD and file tree unchanged; no checkpoint. | Nothing new to process. |
| Work blocked | Draft or authorization gap preserved; no checkpoint. | Execution must wait; processing has not been checkpointed. |

The CLI returned 0 for both completed and blocked invocations. **Inference:** a future integration should distinguish these outcomes rather than treating process success, file changes, or commit count alone as task success. This is a design implication, not an implemented result-status API.

## Verify state independently of the agent narrative

The agent once claimed that a requested change was already present; reading the file showed otherwise, and it corrected itself. Independent checks verified exact content, changed paths, worktree state, and checkpoint trailers.

**Inference:** assess three separate facts: what artifact state was reached, what input was checkpointed, and what remains unresolved. A plausible final report or an exit code cannot establish all three.

## Attention, decisions, and processing are separate

A deleted attention marker remained absent while the decision prose stayed unresolved. An empty checkpoint recorded processing of that deletion.

This supports the existing distinction between dismissing a prompt, deciding a requirement, and recording processed input. It does not establish persistence across future cycles, or approval from silence. See the existing [annotation-attention proposal](../docs/proposals/annotation-attention.md).

## Delegation has a scope

Authorization to run an experiment did not authorize the simulated external agent's proposed product change. The agent paused when that gap was explicit. Other fixtures were handled under explicit delegation, with their synthetic origin recorded.

This supports keeping test execution authority separate from product-decision authority. It does not solve provenance detection; the easy fixture stated the authorization gap directly. See the existing [attribution proposal](../docs/proposals/commit-origin-attribution.md).

## Small experiments can produce useful but narrow knowledge

A one-line change, a clean replay, one dirty tracked file, and one marker deletion were enough to exercise meaningful boundaries without building a larger application.

**Methodological inference:** choose one question, a minimal fixture, an expected observable state, and independent checks. Preserve failed observations, source attribution, and untested cases. Tests should be capable of revealing failure; explicit prompts that reveal the expected answer limit what success demonstrates.

## Small changes do not guarantee small token usage

The trials used low reasoning and short final responses, yet aggregate input counts remained much larger than the artifacts. Cached input was substantial.

**Observed:** small task size did not guarantee small reported usage. **Unresolved:** the contribution of instructions, tool responses, repeated reads, and session overhead was not isolated; no cheapest-model or monetary-cost claim follows.

## Proposed follow-ups

- Remove explanatory hints from an otherwise equivalent fixture and compare behavior.
- Verify that a dismissed marker remains absent after an unrelated later input.
- Check that a rule changed during a cycle takes effect only in the next cycle.
- Compare concise versus repeated context while holding the task and verification constant.

These are proposals, not completed experiments or new approved product requirements. Existing [requirements](../docs/formal/requirements.md) and [coordination protocol](../protocol/coordination.md) remain authoritative.
