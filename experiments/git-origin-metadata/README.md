# Git origin metadata trial

**Status:** Local observation, not an accepted protocol decision.
**Date:** 2026-10-29.

## Question

Do ordinary Git author/committer fields or a `Doc1st-Origin` commit-message
trailer establish who produced a commit or whether a human authorized it?

## Method

In an isolated temporary repository, configure one `user.name` and
`user.email`, create an ordinary commit without a `Doc1st-Origin` trailer, then
create a second commit with `Doc1st-Origin: agent`. Compare
`git log --format='%an <%ae> | %cn <%ce> | %s%n%b'` and inspect the second
commit with `git cat-file -p HEAD`.

No repository files or history in this project were modified by the trial.

## Observation

Both commits had the same author and committer identity. The second commit
contained `Doc1st-Origin: agent` in its commit message. Thus identical Git
identity fields can accompany different origin labels, and the origin label is
stored as commit-message text.

The Git documentation describes trailers as structured key-value metadata in
commit messages and provides tools to add and parse them. It also documents
`git commit --author` as an override for the author field. These are useful
conventions and metadata mechanisms, not evidence that the values are
authenticated.

References:

- [git-interpret-trailers](https://git-scm.com/docs/git-interpret-trailers)
- [git-commit](https://git-scm.com/docs/git-commit)

## Interpretation

Keep these questions separate:

- **Producer:** Who or what created the commit?
- **Authorization:** Has a human designated the commit or range as eligible
  doc1st input?

An explicit human instruction to process a commit or range can authorize that
input without proving who authored every line or approving every generated
requirement. A missing origin trailer or matching Git identity does not prove
human authorship. Conversely, an origin trailer is still useful as a workflow
convention for identifying known doc1st output.

This trial does not test cryptographic signatures, hosting-provider identity,
specific agent integrations, or how an agent should infer authorization.

## Follow-up

The broader bootstrap behavior is covered separately by the
[third-party authorization trial](../codex-bootstrap-boundaries/README.md).
The remaining design choices are tracked in the
[intent attribution proposal](../../docs/proposals/commit-origin-attribution.md).
