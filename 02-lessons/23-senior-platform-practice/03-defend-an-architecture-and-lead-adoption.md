# 23.03 · Defend an architecture and lead adoption

**Prerequisites:** foundation phases and the preceding practitioner lessons. **Time:** 2–4 hours including the linked implementation work. **Tools:** Python 3.10+, SQLite support, and loopback networking for HTTP exercises.

## The mechanism

Senior platform work includes judgment under uncertainty: selecting boundaries, reducing user friction, planning migrations and owning operational consequences. Tool knowledge supports those decisions but does not replace them. Evaluate alternatives against user tasks, threat models, staffing, cost and exit strategy. Learning these skills prepares you for senior-level problems; seniority also requires experience and accountable practice.

## Follow the instructor

1. Open [project 11](../../05-project-labs/11-self-service-api/00-LAB.md). Read the scenario and interface before running commands.
2. Use your completed API and project evidence to write an architecture defense. Compare a local custom control plane, an integration with an existing developer portal and a managed offering. Name what would change the decision. Produce a pilot plan with eligible teams, task-success numerator and denominator, support capacity and retirement criteria. Present one failure drill and one recovery demonstration before the capstone review.
3. Run the project's checker against your implementation or the complete integrated API. Keep the exact command and observation. A solution checker proves the instructor reference; it does not prove your starter is finished.
4. Compare your implementation with the supplied solution only after attempting the stages. Identify one alternative design and explain whether it preserves the same behavior.

## Worked reasoning

A strong defense acknowledges unverified assumptions and proposes experiments to resolve them. It does not label a SQLite registry a production cloud platform. The final capstone must include runnable behavior, negative tests and operational evidence, not only a document or screenshot.

## Failure drill

Introduce one controlled regression in a scratch copy, predict the assertion that should fail and run it. If it does not fail, improve the test before trusting that check. Preserve the original course code and use fresh temporary state when repeating database scenarios. Repair the regression and verify the final result.

## Operational transfer

Write down the authoritative enforcement point, the durable state, the concurrent actor and the partial-failure boundary for this mechanism. Then specify the next experiment required before using it for a real team. Separate behavior you observed locally from cloud, cluster or identity integrations that remain unrun. Name a user-visible recovery instruction and the operator who owns it.

## Independent challenge

Extend the linked project with one additional boundary test and one actionable error message. Explain what happens after process restart and after a repeated request. Where the lab deliberately omits an integration, design its interface and test strategy without inventing a successful result.

## Completion gate

Your implementation or integrated exercise runs; the required negative path rejects; your evidence explains the failure and repair; and you can defend the remaining limitations. Take the final capstone only after you can demonstrate these behaviors without relying on the worked answer.

[Course map](../../01-COURSE-MAP.md) · [Project map](../../05-project-labs/00-PROJECT-MAP.md) · [Python and SQLite reference](https://docs.python.org/3/library/sqlite3.html)

[← Previous lesson](02-recover-a-control-plane-and-verify-user-work.md) · [Next lesson →](../24-capstones-and-organizational-adoption/01-capstone-a-supported-service-path.md)
