# 07.01 · Discover developer needs

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain discover developer needs, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

Treat developers as users with jobs to complete. “Install a portal” is a proposed solution; “release a small service without three handoffs” is a problem worth investigating. Interview for recent behavior, not hypothetical enthusiasm. Ask a developer to reconstruct the last release: waiting, failed steps, help channels and workarounds. A platform team can improve a workflow without owning every infrastructure component. The first product boundary should be smaller than the complete technology landscape.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Use `08-templates/02-discovery.md` to conduct a simulated interview for the fictional commerce team. Write the release journey from repository creation to the first healthy request. Mark active work, waiting and rework separately. Choose one friction point and write a problem statement naming the user, task, obstacle and impact. Propose a manual experiment before choosing software. Estimate a baseline using five fictional observations and label all numbers as simulated.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

The artifact includes a current journey, at least three assumptions, a narrow problem statement and an experiment with a success threshold. The threshold describes a user outcome such as time to first successful deployment, not the number of installed tools.

Save an evidence file named `99-work/01-01-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

A stakeholder asks for a Kubernetes cluster although the journey shows most delay is approval routing. Explain what evidence would justify the cluster and what you would test first.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

If approval routing dominates elapsed time, automate ownership discovery or make the approval path clearer first. A new cluster may be useful later, but it does not directly test the observed bottleneck. Re-interview after the experiment; a faster sub-step may not change total lead time.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** What is a useful discovery question?

<details>
<summary>Reveal the answer</summary>

Ask the user to walk through a recent real task and identify where they waited or requested help.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[CNCF Platforms white paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](../06-orientation-and-workstation/02-evidence-git-and-reproducibility.md) · [Next lesson →](02-define-an-mvp-and-product-measures.md)
