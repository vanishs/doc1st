# Ideas: beyond chat-first interaction

**Status:** Brainstorming, not a protocol extension

- **Attention-centered diffs:** highlight only decisions and conflicts requiring human input when an agent adds hundreds of lines. Standard Git diff already helps with small edits, but new documents can still be overwhelming.
- **Annotations as attentional signals, not a database:** marker deletion may hide a prompt while leaving the underlying uncertainty. Experiment with whether attention and product state should be separate concepts.
- **Natural-language semantic skills:** different meanings (conflict, assumption, human decision) can be added as skills, not a central enum. Preserve a stable English definition of each skill's meaning.
- **Document-driven exploration:** let humans edit an open idea without turning every speculative line into an implementation order; commit messages/context can help distinguish exploration from instructions.
- **Other agents as native participants:** a third-party assistant may produce a commit at human request. Investigate how to carry intent authorization without assuming commit author or missing trailers are enough.
