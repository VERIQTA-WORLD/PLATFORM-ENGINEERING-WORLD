# 17.01 · Backups, restore and integrity

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain backups, restore and integrity, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

A backup is useful only if you can restore the required state within an acceptable time. Recovery point objective limits tolerable data loss; recovery time objective limits tolerable outage duration. A checksum detects accidental corruption but does not authenticate an attacker-controlled backup. The local backup stores a JSON payload and SHA-256 checksum. It has no encryption, access control, remote storage or application-consistency protocol.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Run `python3 03-reference-platform/01-pe.py backup 04-fixtures/02-desired.json --out 99-work/01-catalog-backup.json`. Restore it using `python3 03-reference-platform/01-pe.py restore 99-work/01-catalog-backup.json --out 99-work/01-restored.json`. Validate the restored file and compare it byte-for-byte with the original using `python3 06-tools/02-compare.py 04-fixtures/02-desired.json 99-work/01-restored.json`. Measure elapsed restore time. Write a recovery report separating this local measurement from a production RTO.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

Restored bytes match and the service contract validates. The report lists dependencies required for recovery, including tooling, keys and location of backup copies. It explicitly states that the local envelope is unencrypted and intended only for synthetic fixtures.

Save an evidence file named `99-work/11-01-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

Edit one character inside the envelope payload without changing its checksum. Restore to a fresh path and observe rejection. Then explain why someone who can alter both payload and checksum can bypass this integrity check.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

An unkeyed digest protects against accidental damage. Authenticity requires an independent trust anchor such as a verified signature or authenticated storage. Restore exercises must validate application behavior as well as byte integrity.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** What is the difference between RPO and RTO?

<details>
<summary>Reveal the answer</summary>

RPO concerns tolerable lost data measured in time; RTO concerns time to restore the required service.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[Google SRE books](https://sre.google/books/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](../16-observability-and-reliability/02-slos-error-budgets-and-incident-decisions.md) · [Next lesson →](02-database-changes-and-disaster-recovery.md)
