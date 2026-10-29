# 06.01 · A reproducible learning environment

**Prerequisites:** Read the start guide; no platform experience assumed.  
**Time:** 60–120 minutes including the exercise and reflection.  
**Environment:** Synthetic local files for the core exercise. The container and Kubernetes lessons have an explicitly optional runtime track.

## What you will learn

By the end, you will explain a reproducible learning environment, produce reviewable evidence, and distinguish what your exercise proves from what requires production verification.

## Build the mental model

A platform reduces variability for its users. Start by doing the same for your learning environment. The core track requires Python 3.10 or newer and Git; it makes no network calls and does not require a cloud account. Optional container exercises need a working container runtime, kind and kubectl. Keep the core and cluster tracks separate so that an unavailable runtime does not prevent product, reliability or policy work. A successful command on one laptop is evidence about that laptop, not a supported operating-system matrix.

## Follow along

Work from the repository root. Use `99-work/` if it does not exist. Keep scratch outputs there; commit only a sanitized portfolio artifact when you choose to share your work. Commands use Python 3 and relative paths.

From the repository root, run `python3 06-tools/03-doctor.py` and read every result. Run `python3 06-tools/05-check-all.py --unit-only`. Create a directory called `work` for your outputs. Run `python3 03-reference-platform/01-pe.py validate 04-fixtures/02-desired.json`. Record your Python version, operating system, command and exit code in `99-work/01-environment.md`. If `python3` is unavailable, install a supported Python release using the official download instructions before continuing. Windows users can substitute `py -3` for `python3` and use PowerShell equivalents for shell-only examples.

Before running a command, predict its result. Afterward, record what actually happened. If the result differs, keep that observation and diagnose it; replacing evidence with the expected answer defeats the exercise.

## Acceptance criteria

The doctor reports the interpreter as supported; unit tests pass; validation prints `"valid": true` and exits zero. Your evidence states whether the optional cluster tools are available without claiming that they were exercised.

Save an evidence file named `99-work/00-01-evidence.md` with the command or procedure, inputs, observation, interpretation and any limitation. For a design exercise, include the completed decision table or template and explain how a reviewer could challenge its assumptions.

## Break it deliberately

Validate `04-fixtures/04-invalid.json`. Expect exit code 1 with both a missing owner and an authentication error. A JSON parsing error is a different failure and exits 2.

Use only the supplied fixtures, your own generated files, or the disposable learning cluster. Preserve the original fixtures so another learner can reproduce the baseline. Restore a valid state when finished and note the repair in your evidence.

## Worked reasoning

Successful parsing is weaker than a valid service contract. The invalid fixture is syntactically correct JSON but violates two semantic constraints. Keeping usage errors distinct from policy rejection lets automation give a useful recovery instruction.

Compare your explanation with this reasoning after attempting the drill. Different designs are acceptable when their assumptions, enforcement points and failure behavior are explicit. If you chose an alternative, add a short decision record explaining why it meets the same user need.

## Check your understanding

**Question:** Why should optional cloud tools not fail the core preflight?

<details>
<summary>Reveal the answer</summary>

A learner should be blocked only by dependencies required for the next action. Report later requirements separately.

</details>

## Transfer the lesson

Write three short notes: what the local exercise established, what would change with concurrent users or remote resources, and what evidence you would need before promising this behavior to a team. Choose one remaining uncertainty and describe an experiment that would resolve it. Do not present a design or unrun command as a tested implementation.

## Primary reference

[Python documentation](https://docs.python.org/3/). Read the sections relevant to the exercise and compare terminology with your artifact. External tools and documentation evolve; record versions when you run the optional integrations.

[Phase index](00-INDEX.md) · [Course contents](../../01-COURSE-MAP.md)


[← Previous lesson](../05-data-testing-and-ci/03-run-repeatable-checks-before-sharing-a-change.md) · [Next lesson →](02-evidence-git-and-reproducibility.md)
