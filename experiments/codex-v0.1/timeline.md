# Manual Codex experiment timeline

**Evidence scope:** Hashes and results were supplied in the design discussion; some rounds included actual `git show` output, others only user reports. Prefixes are included for useful linkage, not as a claim that the source repository was imported here.

| Round | Human commit | Codex result commit | Reported observation | Evidence level |
| --- | --- | --- | --- | --- |
| 1 | `8dedd10` | `cbaf000` | Agent added a planning increment and two unresolved markers; did not implement code. | Supplied result diff |
| 2 | `6a07b7b` | `793210f` | Human removed one marker and specified OpenAI-compatible API; agent updated plan, preserved separate task-scope issue. | Supplied result diff in discussion |
| 3 | `93aa200` | `c75b817` | Human changed coordination rules and requested implementation; agent generated Python Web UI launcher, README and tests. | Supplied result diff; 4 tests reported |
| 4 | `b9891f0` | `6091bd2` | Empty human commit message requested model configuration; agent added environment settings and `--check-model`. | User summary; 10 tests reported |
| 5 | `a67c52e` | `25b9779` | Human edited `--no-browser` to `--headless` directly in source with vague commit message; agent fixed code, README, tests. | Supplied result diff; 11 tests reported |
| 6 | `75716c5` | `40c414a` | Human deleted unresolved annotation without decision; agent made empty checkpoint, did not claim approval or restore marker. | Supplied result commit |
| 7 | `d69ae59` | `b40e396` | Empty human commit requested Web text tasks; agent built request/response UI and mock-backed HTTP route, preserved unresolved scope. | Supplied result diff; 14 tests reported |

## Cross-round observations

- Origin and checkpoint trailers appeared in submitted agent commits (`Doc1st-Origin: agent`, `Doc1st-Processed-Through: <SHA>`).
- A protocol amendment in round 3 coincided with the first actual code delivery after two doc-only cycles. This is **suggestive**, not a controlled causal comparison.
- A human's changed code could cause a coherent documentation/test update even with an uninformative commit message.
- A deleted marker could remain absent while ordinary prose still expressed uncertainty.
- The Web UI and model-related tests used local mock services; actual browser automation and native desktop tests were not shown.

## What we do not have

The complete original target project, its independent full test logs, and first-hand Windows/macOS validation. Do not convert the reported passes to verified cross-platform guarantees.
