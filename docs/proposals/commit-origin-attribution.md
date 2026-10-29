# Proposal: intent attribution across tools

**Status:** Open — do not implement as an accepted rule yet.

## Problem

An ordinary Codex App chat may produce commits using the user's Git identity. A commit lacking `Doc1st-Origin: agent` could be written by a human, another agent under human instruction, or an automation. Neither `Author` nor missing trailers proves human intent.

## Candidate approaches

1. **Opt-in intent trailer:** require `Doc1st-Intent: human` or a dedicated commit convention for cross-tool commits. Explicit but adds friction and is not an authentication mechanism.
2. **Invocation boundary:** when the human explicitly requests one doc1st cycle, treat a specified range as authorized input; still distinguish externally-generated content from human-approved specifications.
3. **Trusted source integration:** a future client might receive structured provenance from editors/agents that support it. Not generally available or guaranteed portable.
4. **Conservative ambiguity handling:** pause and request human direction when provenance affects consequential action. Simple but reduces automation.

## Test scenarios

- A human manually edits source and commits.
- An outside agent commits code without a doc1st trailer after a user's chat request.
- An outside agent commits speculative tests without user review.
- One worktree receives both manual and automatic commits.

Success means not looping on agent outputs, not silently granting human authority to arbitrary generated files, and retaining compatibility with ordinary Git.

See the [`git-origin-metadata` trial](../../experiments/git-origin-metadata/README.md)
for a narrow local observation about commit identity fields and origin
trailers. It does not resolve the authorization policy or establish provenance
for third-party tools.
