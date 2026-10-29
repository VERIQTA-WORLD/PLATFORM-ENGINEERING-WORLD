# 19.02 · Versioning, migrations and deprecation

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain versioning, migrations and deprecation, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

A platform contract includes APIs, templates, command behavior, policies and support commitments. Changing a required field can break consumers even if no HTTP endpoint changes. Publish a compatibility policy and observe usage before removing behavior. Deprecation needs a replacement, migration guide, owner, window and exception process. A platform team should budget for upgrades and retirement, because every supported path accumulates operational obligations.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Propose a v2 service contract replacing `owner` with `owner_team`. Write a compatibility adapter that accepts v1, emits v2 and rejects documents containing conflicting values. Describe a shadow-validation period before enforcement. Complete `08-templates/01-adr.md` with alternatives: immediate break, dual support and versioned endpoint. Define adoption evidence required before retiring v1 and an emergency rollback for the validator.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

The migration preserves meaning and reports ambiguous input. The plan includes consumer inventory and communication, not only a code change. Its retirement condition is measurable and its exception has an expiry.

Save an evidence file named `99-work/13-02-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

An old CLI generates v1 documents after the migration deadline. Identify how you would detect the caller version and provide an actionable repair without silently losing ownership data.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

Track client version where trustworthy and return a specific unsupported-version error with migration instructions. Keep a temporary adapter if risk justifies it, but monitor and bound its lifetime. Silent field dropping hides data loss.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** Is changing a validation rule a compatibility change?

<details>
<summary>Reveal the answer</summary>

Yes. Previously accepted input can become rejected even when the API shape remains the same.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[CNCF Platforms white paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](01-support-incidents-and-on-call.md) · [Next lesson →](../20-durable-self-service/01-from-a-command-to-an-http-control-plane.md)
