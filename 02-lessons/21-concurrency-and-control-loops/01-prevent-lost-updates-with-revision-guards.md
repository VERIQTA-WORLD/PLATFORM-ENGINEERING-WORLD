# 21.01 · Prevent lost updates with revision guards

**Prerequisites:** foundation phases and the preceding practitioner lessons. **Time:** 2–4 hours including the linked implementation work. **Tools:** Python 3.10+, SQLite support, and loopback networking for HTTP exercises.

## The mechanism

A stale decision can be invalid even when its syntax and authorization are correct. Revision checking makes that conflict visible. A read followed by an unconditional write is not sufficient; another writer can intervene. The comparison and mutation must occur together in a database statement or equivalent atomic operation.

## Follow the instructor

1. Open [project 07](../../05-project-labs/07-concurrent-updates/00-LAB.md). Read the scenario and interface before running commands.
2. Implement project 07. Complete project 11 stage 6 and preserve both responses. Draw two readers starting from revision 1. Let writer A commit, then show writer B failing. Re-read the service and explain whether B should still want its original value. Add a separate test for an unknown service name and decide whether your public API should distinguish not-found from stale.
3. Run the project's checker against your implementation or the complete integrated API. Keep the exact command and observation. A solution checker proves the instructor reference; it does not prove your starter is finished.
4. Compare your implementation with the supplied solution only after attempting the stages. Identify one alternative design and explain whether it preserves the same behavior.

## Worked reasoning

The failed write leaves A's replicas and revision unchanged. A client must not automatically replace its expected revision with the newest number, because that makes the guard meaningless. The user or a domain-specific merge policy must reconsider intent.

## Failure drill

Introduce one controlled regression in a scratch copy, predict the assertion that should fail and run it. If it does not fail, improve the test before trusting that check. Preserve the original course code and use fresh temporary state when repeating database scenarios. Repair the regression and verify the final result.

## Operational transfer

Write down the authoritative enforcement point, the durable state, the concurrent actor and the partial-failure boundary for this mechanism. Then specify the next experiment required before using it for a real team. Separate behavior you observed locally from cloud, cluster or identity integrations that remain unrun. Name a user-visible recovery instruction and the operator who owns it.

## Independent challenge

Extend the linked project with one additional boundary test and one actionable error message. Explain what happens after process restart and after a repeated request. Where the lab deliberately omits an integration, design its interface and test strategy without inventing a successful result.

## Completion gate

Your implementation or integrated exercise runs; the required negative path rejects; your evidence explains the failure and repair; and you can defend the remaining limitations. Take the final capstone only after you can demonstrate these behaviors without relying on the worked answer.

[Course map](../../01-COURSE-MAP.md) · [Project map](../../05-project-labs/00-PROJECT-MAP.md) · [Python and SQLite reference](https://docs.python.org/3/library/sqlite3.html)

[← Previous lesson](../20-durable-self-service/03-tenant-quotas-and-authorization-at-the-boundary.md) · [Next lesson →](02-converge-desired-state-without-duplicate-effects.md)
