# Decision 0001 — Document-first Git interaction

**Status:** Accepted in project design discussion

## Decision

Keep normal artifacts and Git at the center. **Human commits** may change desired state through file diffs, and **commit messages** may supply immediate instructions. The coordinating agent reviews both, acts on the repository, and commits effects without treating its own commit as a new human request.

## Rationale

Long-lived requirements should remain editable and reviewable outside chat history. Diff is a practical attention surface, and ordinary IDEs/Git should suffice. The project is a coordinator rather than a replacement IDE or new Agent model.

## Implications

- Empty commits may communicate instructions.
- Any text artifact can express human changes, including generated source code.
- The current prototype requires manual invocation; automatic wake-up is not accepted as an existing capability.
