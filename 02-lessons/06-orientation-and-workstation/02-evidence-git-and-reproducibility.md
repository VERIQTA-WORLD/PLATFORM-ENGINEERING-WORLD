# 06.02 · Evidence, Git and reproducibility

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain evidence, git and reproducibility, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

Git records the inputs to a delivery decision. Runtime observations are separate evidence: a desired replica count does not prove two replicas are healthy. A reproducible exercise ties its inputs, tool version, command and observation together. Use synthetic data throughout this course. Do not commit terminal histories, credentials, real tenant names or screenshots of private systems. A public portfolio should explain what someone else can reproduce without access to your employer.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Read `09-ignore-patterns.txt`. Create `99-work/01-baseline.json` by copying `04-fixtures/01-actual.json` with your editor. Run `python3 03-reference-platform/01-pe.py plan 04-fixtures/02-desired.json 99-work/01-baseline.json` and save the output. Compare desired and observed replicas. Write `99-work/01-evidence.md` with the input file names, their relevant values, the command, exit code, expected result and actual result. Use `git diff --no-index 04-fixtures/01-actual.json 04-fixtures/02-desired.json` to inspect the difference; exit 1 means differences were found, not a failed comparison.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

Your evidence distinguishes a planned update from an applied update. Another learner can obtain the same plan from the checked-in fixtures. No private identifiers or local absolute paths appear in material you intend to publish.

Save an evidence file named `99-work/00-02-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

Change the copied baseline to already contain two replicas. Re-run the plan and explain why it is empty. Restore the fixture copy after the experiment.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

A plan is a comparison at a point in time. If observed state changes, the same desired state can produce a different plan. Store the observation used for the decision rather than presenting an old plan as a current fact.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** Is a Git commit sufficient proof of a successful deployment?

<details>
<summary>Reveal the answer</summary>

No. It proves a versioned input. Deployment health and user-facing behavior require separate observations.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[Git documentation](https://git-scm.com/docs). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](01-a-reproducible-learning-environment.md) · [Next lesson →](../07-platform-as-a-product/01-discover-developer-needs.md)
