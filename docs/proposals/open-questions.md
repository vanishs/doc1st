# Open questions

**Status:** Active, deliberately unresolved. A proposal is not an implementation directive by itself.

## P0 — Third-party agent commits

If a user asks Codex App (outside doc1st mode) to change files and Codex commits, should that commit be treated as human intent, agent output, or an ambiguous event? Commit author may be the same as the human. See `commit-origin-attribution.md`.

## P0 — Automatic wake-up and replay

What, if anything, should react immediately to human commits? Git hook, background service, OS integration, or explicit command? What happens with crashes, duplicate triggers, side-effecting tasks and history rewrites? The manual bootstrap does not guarantee exactly-once execution.

## P1 — Multi-branch/worktree

How should doc1st coordinate without clobbering files when Codex App or another tool operates in a different worktree? Which branch owns checkpoints? What happens on merge or cherry-pick?

## P1 — Annotation attention versus requirement state

Deleting a marker without changing prose can mean “stop highlighting this,” not “I approve.” How should that preference persist across later cycles without a sidecar database or reinsert loop? See `annotation-attention.md`.

## P1 — Client implementation

Should `setup/` begin as a minimal trigger/wrapper, a pluggable agent adapter, or something else? Select stack, OS support and install model only after validating requirements.

## P2 — Review fatigue and quality

How much human review remains for large added documents? What measures capture correctness, unnecessary agent edits, and actual user attention? Can smaller diffs and localized markers help without missing dangerous assumptions?
