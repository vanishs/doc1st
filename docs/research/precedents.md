# Prior art and conceptual inspiration

**Status:** Research starting points, not endorsements or claims of equivalence. Links are reading leads and should be rechecked when used for a design decision.

| Precedent | Useful mechanism | Caution for doc1st |
| --- | --- | --- |
| [GitOps](https://opengitops.dev/) | Reconcile actual toward declared desired state | Not every project diff is a complete declarative spec |
| [Git commit trailers](https://git-scm.com/docs/git-interpret-trailers) | Machine-readable origin and checkpoint metadata | Trailers are conventions, not proof of authorship or exactly-once behavior |
| [Git hooks](https://git-scm.com/docs/githooks) | Possible future commit-trigger entry point | Hooks are local and don't magically activate an agent in every environment |
| [Org-mode](https://orgmode.org/) | Task/attention states within editable plain text | Avoid forcing doc1st into a rigid TODO vocabulary |
| [Architecture Decision Records](https://adr.github.io/) | Decision rationale, proposal versus accepted state | A proposed design is not automatically human-approved |
| [OpenSpec](https://github.com/Fission-AI/OpenSpec) / [Spec Kit](https://github.com/github/spec-kit) | Specification-centered agent work | doc1st aims for arbitrary artifact edits and Git as the interaction boundary |
| [reviewdog](https://github.com/reviewdog/reviewdog) | Diff-aware review feedback | New/large documents still require attention prioritization |
| [Cucumber/Gherkin](https://cucumber.io/docs/gherkin/) | Executable specifications and behavior checks | Natural-language text is not a guarantee that tests match true human intent |

Open research questions: when does an annotation merit attention, what should cause action beyond a commit command, and how do we prevent document drift without increasing human reading burden?
