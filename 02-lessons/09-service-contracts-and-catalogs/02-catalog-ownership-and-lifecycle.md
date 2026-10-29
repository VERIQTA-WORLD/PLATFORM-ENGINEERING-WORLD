# 09.02 · Catalog ownership and lifecycle

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain catalog ownership and lifecycle, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

A catalog is useful when people can find responsibility and act on it. Metadata that is never refreshed becomes misleading. Ownership needs a team lifecycle, an escalation route and a way to handle orphaned services. Catalog ingestion is usually eventually consistent: deleting an entity from a UI may not remove its source declaration. Separate lifecycle state from runtime health; a production service can be unhealthy, and a retired service can leave costly resources behind.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Add a second valid service to `99-work/01-service.json`. Give both services the same name and observe duplicate rejection, then repair the names. Build a fictional ownership table with primary team, backup team, support hours and last verification date. Define onboarding, transfer and retirement checklists. Map the teaching fields to a possible Backstage Component entity using the official catalog documentation; record fields that have no direct mapping.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

Duplicate names fail. Each fictional service has an accountable team and a transfer procedure. The retirement checklist covers traffic, data retention, credentials, recurring jobs and catalog removal without equating catalog deletion to resource deletion.

Save an evidence file named `99-work/03-02-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

A team is dissolved and its repository is archived. Write a temporary ownership decision and a verification process that prevents the service from silently becoming unowned.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

Assign a named receiving team with a time-bounded review and confirm its acceptance. Audit runtime inventory, data and paging routes. Mark unresolved ownership visibly; an empty string or archived repository does not transfer responsibility.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** Is a catalog the same thing as a portal?

<details>
<summary>Reveal the answer</summary>

No. A catalog models entities and relationships; a portal is one interface through which users can discover and act on that information.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[Backstage Software Catalog](https://backstage.io/docs/features/software-catalog/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](01-design-a-service-contract.md) · [Next lesson →](../10-containers-and-kubernetes/01-build-and-run-a-container.md)
