# Idea: a workflow that improves how it works

**Status:** Exploratory vision (not a shipped capability)

doc1st can be designed using its own rules: humans commit changes to project knowledge, an existing agent reconciles docs/code, and observations cause improvements to the method. The rules themselves (agent guidance, protocol, skills, document structure) can be among the artifacts that evolve.

Potential feedback loop:

1. Use current doc1st-like workflow on a real task.
2. Notice a recurring failure, friction, or ambiguity.
3. Record an observation, proposal, or targeted experiment.
4. Human edits/commits intent; agent revises protocol, examples, or implementation.
5. Apply revised rules only in **later** reconciliation cycles.

Possible research directions: annotation discoverability in Git diff, review fatigue, automatic triggers, long-term knowledge pruning, measuring rework, and flexible cross-agent adapters.

**Guardrail:** self-evolution must not silently change the human/agent authority boundary or assert that unreviewed agent preferences are human requirements. See `../formal/self-evolution.md`.
