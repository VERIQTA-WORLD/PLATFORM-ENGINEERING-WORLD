# 21.03 · Classify retryable failures and bound work

**Prerequisites:** foundation phases and the preceding practitioner lessons. **Time:** 2–4 hours including the linked implementation work. **Tools:** Python 3.10+, SQLite support, and loopback networking for HTTP exercises.

## The mechanism

A retry policy is a decision about failure semantics. A transient timeout may be worth retrying; authorization denial usually needs a changed identity or policy. Retrying every error wastes capacity and hides user action. Bound attempts, total elapsed time and queue growth. Add backoff and jitter in a production worker to avoid synchronized retry storms.

## Follow the instructor

1. Open [project 08](../../05-project-labs/08-retry-classification/00-LAB.md). Read the scenario and interface before running commands.
2. Implement project 08. Trace the first timeout, second timeout and third success. Then trace a permission failure that executes only once. Add a fake clock design for testing a total deadline without sleeping. Document a failed-operation state and a user-facing next action for exhausted retries in the integrated API.
3. Run the project's checker against your implementation or the complete integrated API. Keep the exact command and observation. A solution checker proves the instructor reference; it does not prove your starter is finished.
4. Compare your implementation with the supplied solution only after attempting the stages. Identify one alternative design and explain whether it preserves the same behavior.

## Worked reasoning

Timeout means the caller lacks an answer; it does not prove the remote effect did not happen. A safe retry needs an idempotent operation or a queryable external request identity. A maximum attempt count alone cannot prevent duplicate remote resources.

## Failure drill

Introduce one controlled regression in a scratch copy, predict the assertion that should fail and run it. If it does not fail, improve the test before trusting that check. Preserve the original course code and use fresh temporary state when repeating database scenarios. Repair the regression and verify the final result.

## Operational transfer

Write down the authoritative enforcement point, the durable state, the concurrent actor and the partial-failure boundary for this mechanism. Then specify the next experiment required before using it for a real team. Separate behavior you observed locally from cloud, cluster or identity integrations that remain unrun. Name a user-visible recovery instruction and the operator who owns it.

## Independent challenge

Extend the linked project with one additional boundary test and one actionable error message. Explain what happens after process restart and after a repeated request. Where the lab deliberately omits an integration, design its interface and test strategy without inventing a successful result.

## Completion gate

Your implementation or integrated exercise runs; the required negative path rejects; your evidence explains the failure and repair; and you can defend the remaining limitations. Take the final capstone only after you can demonstrate these behaviors without relying on the worked answer.

[Course map](../../01-COURSE-MAP.md) · [Project map](../../05-project-labs/00-PROJECT-MAP.md) · [Python and SQLite reference](https://docs.python.org/3/library/sqlite3.html)

[← Previous lesson](02-converge-desired-state-without-duplicate-effects.md) · [Next lesson →](../22-platform-quality-and-evidence/01-test-a-platform-across-its-interfaces.md)
