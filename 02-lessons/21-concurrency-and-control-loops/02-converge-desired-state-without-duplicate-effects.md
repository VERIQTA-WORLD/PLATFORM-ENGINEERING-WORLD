# 21.02 · Converge desired state without duplicate effects

**Prerequisites:** foundation phases and the preceding practitioner lessons. **Time:** 2–4 hours including the linked implementation work. **Tools:** Python 3.10+, SQLite support, and loopback networking for HTTP exercises.

## The mechanism

Reconciliation needs a stable identity for each resource. If every loop creates a new randomly named object, repetition leaks resources instead of converging. Compare a goal with an observation, plan changes and apply them idempotently. Also decide who owns deletion and what remains unmanaged.

## Follow the instructor

1. Open [project 04](../../05-project-labs/04-desired-state-controller/00-LAB.md). Read the scenario and interface before running commands.
2. Implement project 04 and pass its grader. Take desired checkout=2 and actual checkout=1. Apply the returned action manually to a copied dictionary and plan again. Then remove checkout from desired state. Explain the retain result. In project 11, run operator reconciliation twice and inspect the zero-work second result.
3. Run the project's checker against your implementation or the complete integrated API. Keep the exact command and observation. A solution checker proves the instructor reference; it does not prove your starter is finished.
4. Compare your implementation with the supplied solution only after attempting the stages. Identify one alternative design and explain whether it preserves the same behavior.

## Worked reasoning

The second loop should not produce another create. The integrated registry operation and state transition share a SQLite transaction, so they commit together. A cloud resource will not share that database transaction; its provider adapter needs an additional recovery protocol.

## Failure drill

Introduce one controlled regression in a scratch copy, predict the assertion that should fail and run it. If it does not fail, improve the test before trusting that check. Preserve the original course code and use fresh temporary state when repeating database scenarios. Repair the regression and verify the final result.

## Operational transfer

Write down the authoritative enforcement point, the durable state, the concurrent actor and the partial-failure boundary for this mechanism. Then specify the next experiment required before using it for a real team. Separate behavior you observed locally from cloud, cluster or identity integrations that remain unrun. Name a user-visible recovery instruction and the operator who owns it.

## Independent challenge

Extend the linked project with one additional boundary test and one actionable error message. Explain what happens after process restart and after a repeated request. Where the lab deliberately omits an integration, design its interface and test strategy without inventing a successful result.

## Completion gate

Your implementation or integrated exercise runs; the required negative path rejects; your evidence explains the failure and repair; and you can defend the remaining limitations. Take the final capstone only after you can demonstrate these behaviors without relying on the worked answer.

[Course map](../../01-COURSE-MAP.md) · [Project map](../../05-project-labs/00-PROJECT-MAP.md) · [Python and SQLite reference](https://docs.python.org/3/library/sqlite3.html)

[← Previous lesson](01-prevent-lost-updates-with-revision-guards.md) · [Next lesson →](03-classify-retryable-failures-and-bound-work.md)
