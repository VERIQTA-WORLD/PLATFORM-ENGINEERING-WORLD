# 17.02 · Database changes and disaster recovery

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain database changes and disaster recovery, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

Application state makes release recovery harder than redeploying an old image. Use an expand-and-contract migration when old and new application versions must coexist: add a compatible representation, migrate reads and writes, backfill, verify, then remove the old representation after the rollback window. Backups must be consistent with the application recovery procedure. A restore may replay old schema, credentials and external references that no longer match the live system.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Write an expand-and-contract plan for renaming customer field `name` to `display_name`. Include compatibility with old readers, dual-write or translation behavior, backfill idempotency, validation and the point where rollback becomes unsafe. Complete `08-templates/09-recovery.md` for a regional outage with a fictional database. Specify RPO, RTO, restore order, traffic switching, data reconciliation and who declares recovery complete.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

Every stage has an observable acceptance condition and an abort path. You identify the destructive contract step and delay it until old clients are gone. The recovery plan tests a user transaction instead of stopping at database process health.

Save an evidence file named `99-work/11-02-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

A failover region accepts writes while the old region remains writable. Describe split-brain risk and the fencing step required before promoting a writer.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

Two writers can diverge and make later reconciliation destructive. Use the database’s supported failover and fencing mechanisms, establish a single authority and verify replication state. DNS switching alone does not revoke writes in the old region.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** Why can an old application image fail after a schema change?

<details>
<summary>Reveal the answer</summary>

The database may no longer satisfy the old application contract, even if the old binary itself starts successfully.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[Google SRE books](https://sre.google/books/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](01-backups-restore-and-integrity.md) · [Next lesson →](../18-cost-and-capacity/01-cost-allocation-and-unit-economics.md)
