# 20.01 · From a command to an HTTP control plane

**Prerequisites:** foundation phases and the preceding practitioner lessons. **Time:** 2–4 hours including the linked implementation work. **Tools:** Python 3.10+, SQLite support, and loopback networking for HTTP exercises.

## The mechanism

An API boundary separates the caller from the process doing the work. Unlike a local function call, a network call can fail after the server has accepted it. The caller may not know whether to retry. Solve the ambiguity with a durable operation identity, not an optimistic success message. Start with the running server and inspect actual status codes before designing a user interface.

## Follow the instructor

1. Open [project 11](../../05-project-labs/11-self-service-api/00-LAB.md). Read the scenario and interface before running commands.
2. Complete stages 1–3 of project 11. For each response, write the method, path, actor, status, operation ID and state. Compare reachability at /healthz with acceptance at POST /services. A 202 does not prove a deployment; in this teaching service it records intent for a later local registry operation. Open the server code and follow the route dispatch into Store.submit.
3. Run the project's checker against your implementation or the complete integrated API. Keep the exact command and observation. A solution checker proves the instructor reference; it does not prove your starter is finished.
4. Compare your implementation with the supplied solution only after attempting the stages. Identify one alternative design and explain whether it preserves the same behavior.

## Worked reasoning

Keep the same idempotency key while changing replicas. The 409 preserves the accepted request. Returning a new operation would hide the fact that the original work might already execute. A new user intention needs an explicit new operation or update contract.

## Failure drill

Introduce one controlled regression in a scratch copy, predict the assertion that should fail and run it. If it does not fail, improve the test before trusting that check. Preserve the original course code and use fresh temporary state when repeating database scenarios. Repair the regression and verify the final result.

## Operational transfer

Write down the authoritative enforcement point, the durable state, the concurrent actor and the partial-failure boundary for this mechanism. Then specify the next experiment required before using it for a real team. Separate behavior you observed locally from cloud, cluster or identity integrations that remain unrun. Name a user-visible recovery instruction and the operator who owns it.

## Independent challenge

Extend the linked project with one additional boundary test and one actionable error message. Explain what happens after process restart and after a repeated request. Where the lab deliberately omits an integration, design its interface and test strategy without inventing a successful result.

## Completion gate

Your implementation or integrated exercise runs; the required negative path rejects; your evidence explains the failure and repair; and you can defend the remaining limitations. Take the final capstone only after you can demonstrate these behaviors without relying on the worked answer.

[Course map](../../01-COURSE-MAP.md) · [Project map](../../05-project-labs/00-PROJECT-MAP.md) · [Python and SQLite reference](https://docs.python.org/3/library/sqlite3.html)

[← Previous lesson](../19-platform-operations-and-evolution/02-versioning-migrations-and-deprecation.md) · [Next lesson →](02-transactions-idempotency-and-duplicate-requests.md)
