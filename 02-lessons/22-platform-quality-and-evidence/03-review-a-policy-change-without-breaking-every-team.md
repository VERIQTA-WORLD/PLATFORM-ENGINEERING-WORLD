# 22.03 · Review a policy change without breaking every team

**Prerequisites:** foundation phases and the preceding practitioner lessons. **Time:** 2–4 hours including the linked implementation work. **Tools:** Python 3.10+, SQLite support, and loopback networking for HTTP exercises.

## The mechanism

A stricter validator can break users without changing the API shape. Treat policy as a maintained contract. Inventory affected consumers, run a shadow or audit period, publish actionable repairs and bound exceptions. Critical controls still need authoritative enforcement when the protected action occurs.

## Follow the instructor

1. Open [project 03](../../05-project-labs/03-catalog-contract/00-LAB.md). Read the scenario and interface before running commands.
2. Implement project 03. Add a proposed requirement that every service has a tier. Write a two-stage migration: first warn and measure missing tiers, then enforce after users have a compatible generator. Create allowed, missing, invalid and exception-expired examples. Use the tenant rule from project 05 to distinguish a metadata check from a protected mutation decision.
3. Run the project's checker against your implementation or the complete integrated API. Keep the exact command and observation. A solution checker proves the instructor reference; it does not prove your starter is finished.
4. Compare your implementation with the supplied solution only after attempting the stages. Identify one alternative design and explain whether it preserves the same behavior.

## Worked reasoning

A template update repairs new services but not existing ones. An adoption plan needs an inventory and upgrade path. An exception needs a scoped owner, approver, justification and expiry. It must not become a silent global bypass.

## Failure drill

Introduce one controlled regression in a scratch copy, predict the assertion that should fail and run it. If it does not fail, improve the test before trusting that check. Preserve the original course code and use fresh temporary state when repeating database scenarios. Repair the regression and verify the final result.

## Operational transfer

Write down the authoritative enforcement point, the durable state, the concurrent actor and the partial-failure boundary for this mechanism. Then specify the next experiment required before using it for a real team. Separate behavior you observed locally from cloud, cluster or identity integrations that remain unrun. Name a user-visible recovery instruction and the operator who owns it.

## Independent challenge

Extend the linked project with one additional boundary test and one actionable error message. Explain what happens after process restart and after a repeated request. Where the lab deliberately omits an integration, design its interface and test strategy without inventing a successful result.

## Completion gate

Your implementation or integrated exercise runs; the required negative path rejects; your evidence explains the failure and repair; and you can defend the remaining limitations. Take the final capstone only after you can demonstrate these behaviors without relying on the worked answer.

[Course map](../../01-COURSE-MAP.md) · [Project map](../../05-project-labs/00-PROJECT-MAP.md) · [Python and SQLite reference](https://docs.python.org/3/library/sqlite3.html)

[← Previous lesson](02-use-telemetry-to-make-a-release-decision.md) · [Next lesson →](../23-senior-platform-practice/01-evolve-data-while-preserving-old-clients.md)
