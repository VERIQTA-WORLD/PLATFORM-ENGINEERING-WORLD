# 23.01 · Evolve data while preserving old clients

**Prerequisites:** foundation phases and the preceding practitioner lessons. **Time:** 2–4 hours including the linked implementation work. **Tools:** Python 3.10+, SQLite support, and loopback networking for HTTP exercises.

## The mechanism

Schema compatibility crosses application and infrastructure boundaries. Expand-and-contract adds a new representation, migrates users and only later removes the old representation. Backfill must be restartable and preserve new writes. A rollback window ends when a destructive change removes a contract the old application needs.

## Follow the instructor

1. Open [project 09](../../05-project-labs/09-schema-migration/00-LAB.md). Read the scenario and interface before running commands.
2. Implement project 09. Run its solution twice and verify the old name still exists. Change display_name and rerun to show that the migration preserves the new value. Write the missing application rollout stages: compatible reader, dual-write strategy, backfill validation, reader migration and eventual contract removal. State how multiple migration workers would be serialized.
3. Run the project's checker against your implementation or the complete integrated API. Keep the exact command and observation. A solution checker proves the instructor reference; it does not prove your starter is finished.
4. Compare your implementation with the supplied solution only after attempting the stages. Identify one alternative design and explain whether it preserves the same behavior.

## Worked reasoning

The exercise teaches a single-migrator expand step. It does not establish that dual writes are correct or that all readers migrated. Removing the old column before those observations makes a source-code rollback unsafe.

## Failure drill

Introduce one controlled regression in a scratch copy, predict the assertion that should fail and run it. If it does not fail, improve the test before trusting that check. Preserve the original course code and use fresh temporary state when repeating database scenarios. Repair the regression and verify the final result.

## Operational transfer

Write down the authoritative enforcement point, the durable state, the concurrent actor and the partial-failure boundary for this mechanism. Then specify the next experiment required before using it for a real team. Separate behavior you observed locally from cloud, cluster or identity integrations that remain unrun. Name a user-visible recovery instruction and the operator who owns it.

## Independent challenge

Extend the linked project with one additional boundary test and one actionable error message. Explain what happens after process restart and after a repeated request. Where the lab deliberately omits an integration, design its interface and test strategy without inventing a successful result.

## Completion gate

Your implementation or integrated exercise runs; the required negative path rejects; your evidence explains the failure and repair; and you can defend the remaining limitations. Take the final capstone only after you can demonstrate these behaviors without relying on the worked answer.

[Course map](../../01-COURSE-MAP.md) · [Project map](../../05-project-labs/00-PROJECT-MAP.md) · [Python and SQLite reference](https://docs.python.org/3/library/sqlite3.html)

[← Previous lesson](../22-platform-quality-and-evidence/03-review-a-policy-change-without-breaking-every-team.md) · [Next lesson →](02-recover-a-control-plane-and-verify-user-work.md)
