# 22.02 · Use telemetry to make a release decision

**Prerequisites:** foundation phases and the preceding practitioner lessons. **Time:** 2–4 hours including the linked implementation work. **Tools:** Python 3.10+, SQLite support, and loopback networking for HTTP exercises.

## The mechanism

A queue can grow while an API responds successfully. Measure accepted work, in-flight age, terminal outcomes and completion time. Do not compute completion latency only for successful work and ignore stuck requests. A release decision needs user-impact evidence, data coverage and a defined objective.

## Follow the instructor

1. Open [project 11](../../05-project-labs/11-self-service-api/00-LAB.md). Read the scenario and interface before running commands.
2. Start project 11 fresh. Submit an operation without reconciling it. Call GET /metrics using the operator identity and observe requested=1, ready=0. Reconcile and observe requested=0, ready=1. Compare these state counts with the fixture SLO calculation. Design timestamps and an oldest-request-age signal as an extension; do not claim the current endpoint provides Prometheus instrumentation or duration histograms.
3. Run the project's checker against your implementation or the complete integrated API. Keep the exact command and observation. A solution checker proves the instructor reference; it does not prove your starter is finished.
4. Compare your implementation with the supplied solution only after attempting the stages. Identify one alternative design and explain whether it preserves the same behavior.

## Worked reasoning

Counts can reveal a backlog, but they cannot tell how long it has existed. Add persisted acceptance and terminal timestamps, define the window and account for incomplete work. Metrics with arbitrary operation IDs as labels can create unbounded cardinality.

## Failure drill

Introduce one controlled regression in a scratch copy, predict the assertion that should fail and run it. If it does not fail, improve the test before trusting that check. Preserve the original course code and use fresh temporary state when repeating database scenarios. Repair the regression and verify the final result.

## Operational transfer

Write down the authoritative enforcement point, the durable state, the concurrent actor and the partial-failure boundary for this mechanism. Then specify the next experiment required before using it for a real team. Separate behavior you observed locally from cloud, cluster or identity integrations that remain unrun. Name a user-visible recovery instruction and the operator who owns it.

## Independent challenge

Extend the linked project with one additional boundary test and one actionable error message. Explain what happens after process restart and after a repeated request. Where the lab deliberately omits an integration, design its interface and test strategy without inventing a successful result.

## Completion gate

Your implementation or integrated exercise runs; the required negative path rejects; your evidence explains the failure and repair; and you can defend the remaining limitations. Take the final capstone only after you can demonstrate these behaviors without relying on the worked answer.

[Course map](../../01-COURSE-MAP.md) · [Project map](../../05-project-labs/00-PROJECT-MAP.md) · [Python and SQLite reference](https://docs.python.org/3/library/sqlite3.html)

[← Previous lesson](01-test-a-platform-across-its-interfaces.md) · [Next lesson →](03-review-a-policy-change-without-breaking-every-team.md)
