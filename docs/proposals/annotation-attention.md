# Proposal: annotations as attention rather than state

**Status:** Exploratory interpretation, supported by one limited observation.

An inline `[doc1st:...:id]` marker visibly asks for attention. Underlying uncertainty may remain even after the human deletes the marker. The marker's presence/absence should not be the only state database of product truth.

## Evidence

During the sixth Codex experiment, the human deleted a human-decision marker without resolving the product decision. The agent created an **empty checkpoint**, did not reinsert the marker, and did not claim the decision was approved. The user-provided commit message said the existing prose still represented the uncertainty. See `../../experiments/codex-v0.1/findings.md`.

## Design consequences

- A marker is an *interaction/attention affordance* in the file, not a full approval protocol.
- Existing prose, explicit human amendments, and project constraints determine whether a product decision is actually resolved.
- Markers should be few and contextual. Avoid creating a separate sidecar just to preserve an annotation's absence.

## Unresolved

How to distinguish deletion by mistake, dismissal, explicit delegation, and a decision expressed elsewhere? Can agents avoid reintroducing equivalent prompts without a separate suppression registry? This needs more experiments.
