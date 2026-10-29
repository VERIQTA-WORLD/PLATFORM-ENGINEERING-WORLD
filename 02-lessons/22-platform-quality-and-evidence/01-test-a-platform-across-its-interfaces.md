# 22.01 · Test a platform across its interfaces

**Prerequisites:** foundation phases and the preceding practitioner lessons. **Time:** 2–4 hours including the linked implementation work. **Tools:** Python 3.10+, SQLite support, and loopback networking for HTTP exercises.

## The mechanism

Unit tests isolate a mechanism. Integration tests exercise boundaries such as HTTP parsing, identity, routing and storage. Neither replaces a user acceptance check. Keep tests deterministic with temporary databases and ephemeral ports, and verify denied paths rather than only successful responses.

## Follow the instructor

1. Open [project 11](../../05-project-labs/11-self-service-api/00-LAB.md). Read the scenario and interface before running commands.
2. Read project 11's HTTP smoke program. Run it and identify which assertion crosses a real network boundary. Compare it with the Store unit tests. In a scratch copy, bypass the operator role check and show which HTTP assertion fails. Restore it. Add a malformed JSON request check and define its expected 400 response.
3. Run the project's checker against your implementation or the complete integrated API. Keep the exact command and observation. A solution checker proves the instructor reference; it does not prove your starter is finished.
4. Compare your implementation with the supplied solution only after attempting the stages. Identify one alternative design and explain whether it preserves the same behavior.

## Worked reasoning

The Store tests cannot prove that the HTTP handler actually calls authorization. Conversely, an HTTP success alone may not cover concurrent idempotency. Choose a test layer according to the behavior and avoid claiming either layer proves production security.

## Failure drill

Introduce one controlled regression in a scratch copy, predict the assertion that should fail and run it. If it does not fail, improve the test before trusting that check. Preserve the original course code and use fresh temporary state when repeating database scenarios. Repair the regression and verify the final result.

## Operational transfer

Write down the authoritative enforcement point, the durable state, the concurrent actor and the partial-failure boundary for this mechanism. Then specify the next experiment required before using it for a real team. Separate behavior you observed locally from cloud, cluster or identity integrations that remain unrun. Name a user-visible recovery instruction and the operator who owns it.

## Independent challenge

Extend the linked project with one additional boundary test and one actionable error message. Explain what happens after process restart and after a repeated request. Where the lab deliberately omits an integration, design its interface and test strategy without inventing a successful result.

## Completion gate

Your implementation or integrated exercise runs; the required negative path rejects; your evidence explains the failure and repair; and you can defend the remaining limitations. Take the final capstone only after you can demonstrate these behaviors without relying on the worked answer.

[Course map](../../01-COURSE-MAP.md) · [Project map](../../05-project-labs/00-PROJECT-MAP.md) · [Python and SQLite reference](https://docs.python.org/3/library/sqlite3.html)

[← Previous lesson](../21-concurrency-and-control-loops/03-classify-retryable-failures-and-bound-work.md) · [Next lesson →](02-use-telemetry-to-make-a-release-decision.md)
