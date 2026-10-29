# 20.03 · Tenant quotas and authorization at the boundary

**Prerequisites:** foundation phases and the preceding practitioner lessons. **Time:** 2–4 hours including the linked implementation work. **Tools:** Python 3.10+, SQLite support, and loopback networking for HTTP exercises.

## The mechanism

Tenant isolation must be applied to both data lookup and mutation. A client-supplied tenant field is a request, not proof of membership. Derive authority from a verified caller record and check the target. Quota admission must also serialize competing requests, otherwise several requests can each observe available capacity and collectively exceed it.

## Follow the instructor

1. Open [project 05](../../05-project-labs/05-tenant-authorization/00-LAB.md). Read the scenario and interface before running commands.
2. Implement project 05. Complete project 11 stages 4–5. Read the quota test and create three distinct synthetic services in a fresh database, using different names and keys. A fourth must reject before reconciliation because pending work consumes this demo quota. Compare cross-tenant 404, unknown-identity 401 and operator-required 403.
3. Run the project's checker against your implementation or the complete integrated API. Keep the exact command and observation. A solution checker proves the instructor reference; it does not prove your starter is finished.
4. Compare your implementation with the supplied solution only after attempting the stages. Identify one alternative design and explain whether it preserves the same behavior.

## Worked reasoning

Returning 404 for another tenant avoids confirming whether its operation exists. The SQL query includes tenant, preventing a globally valid operation ID from bypassing isolation. The quota is counted under the same write transaction as acceptance, not in the UI.

## Failure drill

Introduce one controlled regression in a scratch copy, predict the assertion that should fail and run it. If it does not fail, improve the test before trusting that check. Preserve the original course code and use fresh temporary state when repeating database scenarios. Repair the regression and verify the final result.

## Operational transfer

Write down the authoritative enforcement point, the durable state, the concurrent actor and the partial-failure boundary for this mechanism. Then specify the next experiment required before using it for a real team. Separate behavior you observed locally from cloud, cluster or identity integrations that remain unrun. Name a user-visible recovery instruction and the operator who owns it.

## Independent challenge

Extend the linked project with one additional boundary test and one actionable error message. Explain what happens after process restart and after a repeated request. Where the lab deliberately omits an integration, design its interface and test strategy without inventing a successful result.

## Completion gate

Your implementation or integrated exercise runs; the required negative path rejects; your evidence explains the failure and repair; and you can defend the remaining limitations. Take the final capstone only after you can demonstrate these behaviors without relying on the worked answer.

[Course map](../../01-COURSE-MAP.md) · [Project map](../../05-project-labs/00-PROJECT-MAP.md) · [Python and SQLite reference](https://docs.python.org/3/library/sqlite3.html)

[← Previous lesson](02-transactions-idempotency-and-duplicate-requests.md) · [Next lesson →](../21-concurrency-and-control-loops/01-prevent-lost-updates-with-revision-guards.md)
