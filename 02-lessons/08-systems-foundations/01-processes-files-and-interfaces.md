# 08.01 · Processes, files and interfaces

**Prerequisites:** Complete the preceding lesson or demonstrate its acceptance criteria.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain processes, files and interfaces, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

An automation tool has an interface just like a network service: accepted inputs, output format, failure codes and side effects. Separate planning from applying so a person or policy can inspect intent. The teaching CLI reads JSON and writes only explicitly named files. Its state is a local file, not a database or cloud control plane. Production implementations also need concurrency control, authenticated callers, durable operations and recovery after partial failure.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

Run `python3 03-reference-platform/01-pe.py --help`, then inspect `03-reference-platform/01-pe.py`. Trace how `plan` reads desired and actual state without writing either. Run `python3 03-reference-platform/01-pe.py apply 04-fixtures/02-desired.json 04-fixtures/01-actual.json --out 99-work/01-applied.json`. Validate that output. Write an interface contract describing inputs, output, exit codes and overwrite behavior. Identify which commands refuse existing output files and which can overwrite them.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

The applied catalog contains two replicas. Your contract accurately notes that apply can overwrite its output while scaffold, backup and restore refuse existing targets. It also states that the simulator changes file contents only.

Save an evidence file named `99-work/02-01-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

Run the CLI with a nonexistent input path and then malformed JSON. Explain why both are usage/input errors rather than ordinary policy rejections.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

Both errors prevent evaluation of the service contract. Exit 2 communicates that no valid decision was produced. A robust caller should display the error and stop, rather than treating it as an empty plan.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** Why separate a plan from apply?

<details>
<summary>Reveal the answer</summary>

It makes intended effects reviewable and enables checks before mutation, though a stale plan still needs revalidation.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[Python documentation](https://docs.python.org/3/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](../07-platform-as-a-product/02-define-an-mvp-and-product-measures.md) · [Next lesson →](02-networking-dns-and-trust-boundaries.md)
