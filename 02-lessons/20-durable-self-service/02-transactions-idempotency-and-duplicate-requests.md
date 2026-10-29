# 20.02 · Transactions idempotency and duplicate requests

**Prerequisites:** foundation phases and the preceding practitioner lessons. **Time:** 2–4 hours including the linked implementation work. **Tools:** Python 3.10+, SQLite support, and loopback networking for HTTP exercises.

## The mechanism

A check-then-insert sequence outside a transaction can race. Two workers might both see no record and create duplicates. Store a unique scoped key and normalized request inside an authoritative transaction. Persist the acceptance record before claiming the request was accepted. A transaction in one database does not automatically include a queue or remote provider.

## Follow the instructor

1. Open [project 06](../../05-project-labs/06-durable-operations/00-LAB.md). Read the scenario and interface before running commands.
2. Implement project 06 and pass its grader. In the integrated API tests, find test_concurrent_request_has_one_operation. Run the check suite, then explain why eight concurrent equivalent requests should yield exactly one ID and one row. In a scratch version, remove request-body comparison and observe which conflict assertion catches the regression.
3. Run the project's checker against your implementation or the complete integrated API. Keep the exact command and observation. A solution checker proves the instructor reference; it does not prove your starter is finished.
4. Compare your implementation with the supplied solution only after attempting the stages. Identify one alternative design and explain whether it preserves the same behavior.

## Worked reasoning

A retry with equivalent content returns the old operation. Different content with the same key must reject. If a remote effect happens outside the transaction, use the operation ID to query or adopt that effect on recovery. Do not assume rollback can undo an external API call.

## Failure drill

Introduce one controlled regression in a scratch copy, predict the assertion that should fail and run it. If it does not fail, improve the test before trusting that check. Preserve the original course code and use fresh temporary state when repeating database scenarios. Repair the regression and verify the final result.

## Operational transfer

Write down the authoritative enforcement point, the durable state, the concurrent actor and the partial-failure boundary for this mechanism. Then specify the next experiment required before using it for a real team. Separate behavior you observed locally from cloud, cluster or identity integrations that remain unrun. Name a user-visible recovery instruction and the operator who owns it.

## Independent challenge

Extend the linked project with one additional boundary test and one actionable error message. Explain what happens after process restart and after a repeated request. Where the lab deliberately omits an integration, design its interface and test strategy without inventing a successful result.

## Completion gate

Your implementation or integrated exercise runs; the required negative path rejects; your evidence explains the failure and repair; and you can defend the remaining limitations. Take the final capstone only after you can demonstrate these behaviors without relying on the worked answer.

[Course map](../../01-COURSE-MAP.md) · [Project map](../../05-project-labs/00-PROJECT-MAP.md) · [Python and SQLite reference](https://docs.python.org/3/library/sqlite3.html)

[← Previous lesson](01-from-a-command-to-an-http-control-plane.md) · [Next lesson →](03-tenant-quotas-and-authorization-at-the-boundary.md)
