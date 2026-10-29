# Minimal Codex bootstrap trial

**Status:** Observed experiment, not a new product requirement.
**Date:** 2026-10-29.
**Scope:** One authorized message-only input and one no-new-input replay.
**Agent configuration:** Codex CLI 0.165.0, gpt-6-luna, low reasoning.

## Procedure and observations

The bootstrap instructions and human-decision skill were copied unchanged into a small Git repository. The orchestrating agent created the synthetic input under explicit human delegation; its provenance was recorded rather than presented as independently authored human intent.

1. Setup checkpoint `a1ed4568a46c23b3c9691bb5c418875d6084a1ad` added `status.txt` containing exactly `Status: pending\n`.
2. Empty input commit `b290eb00807467466f9a0f5377773613011e109f` requested exactly `Status: ready\n` and no other project-file changes.
3. The first invocation could not execute local commands and reported that reconciliation had not occurred. Its CLI exit code was nevertheless 0. The file remained pending and no checkpoint was created.
4. A subsequent invocation completed the change and produced checkpoint `7d091b53aaad1de6e760653702473af3bd530a93`.
5. Independent Python/Git checks confirmed exact ready-file bytes, a clean worktree, only `status.txt` changed, `Doc1st-Origin: agent`, and the correct `Doc1st-Processed-Through` input SHA.
6. A fresh manual cycle with no new input left HEAD, the committed tree, and worktree cleanliness unchanged. No checkpoint was added.

During the successful invocation, the agent initially claimed the input had already set the file content. An actual file check showed pending; it corrected itself before completing the requested change.

## Reported usage

These are CLI-reported counters, not measured currency charges. Cached input is included within input; reasoning output is included within output.

| Invocation | Result | Input | Cached input | Output | Reasoning output |
| --- | --- | ---: | ---: | ---: | ---: |
| 1 | Execution blocked | 42,458 | 39,296 | 368 | 20 |
| 2 | One-line change and checkpoint | 124,691 | 104,064 | 1,366 | 356 |
| 3 | No-new-input stop | 46,564 | 40,960 | 598 | 173 |

A tiny artifact change and low reasoning did not imply a small aggregate input count. These measurements do not isolate the causes of overhead or establish a cheapest model.

## Knowledge and limits

- A delegated message-only instruction was processed correctly in this trial.
- No eligible new input resulted in no new checkpoint in one replay.
- Exit 0 did not establish successful reconciliation; inspect artifacts, Git state, trailers, and the final report.
- Intermediate agent statements can be wrong even when the final result is correct.

This is one simple manual trial, not evidence of automatic triggering, universal compatibility, exactly-once side effects, or reliable interpretation of complex intent. See the [cross-trial synthesis](../bootstrap-observations.md) and [boundary trials](../codex-bootstrap-boundaries/README.md).
