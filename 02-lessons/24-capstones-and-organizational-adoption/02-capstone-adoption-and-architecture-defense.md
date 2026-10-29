# 24.02 · Capstone: adoption and architecture defense

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 6–12 hours for the written defense; implementation time is additional.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain capstone: adoption and architecture defense, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

A technically elegant platform can fail if teams cannot adopt it or its support cost exceeds its benefit. Defend architecture choices using user needs, threat boundaries, operating capacity and evidence. Treat build-versus-buy as a recurring decision: ownership and integration costs exist in either case. A senior-level platform proposal explains which complexity it absorbs for users and which complexity remains deliberately visible.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Complete capstone B or C in `01-guides/02-capstones.md`. Write a six-month fictional adoption plan with pilot criteria, support capacity, migration cohorts and retirement of old paths. Compare a custom controller, a portal integration and a managed offering without inventing vendor capabilities or prices. Prepare an architecture decision record, a threat model, cost assumptions and a disaster-recovery tabletop. Conduct a self-review or peer review and label which you performed.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

The defense includes at least three rejected alternatives, evidence that would change the decision and an exit strategy. Adoption targets have denominators and time windows. The final public portfolio contains only original diagrams, synthetic examples and appropriately linked sources.

Save an evidence file named `99-work/14-02-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

The pilot is successful for one team but two new teams need unsupported stateful workloads. Explain whether to broaden scope, create another path or decline the request, and what evidence informs the choice.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

Revisit demand, risk and support capacity. A separate path may preserve the simple workflow while addressing stateful requirements explicitly. Broadening one template without new recovery and ownership guarantees creates hidden obligations.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** When should an architecture decision be revisited?

<details>
<summary>Reveal the answer</summary>

When its assumptions change or new evidence crosses a documented review trigger, such as workload type, scale, risk or support cost.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[CNCF Platforms white paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](01-capstone-a-supported-service-path.md)
