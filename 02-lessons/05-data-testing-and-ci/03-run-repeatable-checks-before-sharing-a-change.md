# 05.03 · Run repeatable checks before sharing a change

**Prerequisite:** the preceding foundation lesson. **Time:** 60–90 minutes. **Tools:** Python 3.10+; Git is additionally required in phase 03. Work from the repository root. This is a runnable lesson, not a request to design a system you have not learned yet.

## What the idea means

Continuous integration runs agreed checks for a revision in a repeatable environment. You can begin by running the same commands locally. One command should return nonzero if any required check fails. Documentation checks, unit tests and runtime tests cover different evidence; a file existing is not proof that a server starts. Hosting-specific discovery uses reserved paths, so this fully numbered distribution provides an example rather than claiming hosted automation has run.

## Build it with the instructor

1. Open a plain-text editor. Create a file named `99-work/05-03-practice.py`. Ensure your editor does not add `.txt` after `.py`.
2. Type the following complete program. Preserve indentation: Python uses leading spaces to group statements. You can compare your work with [17-run-repeatable-checks-before-sharing-a-change.py](../../05-project-labs/02-foundations/17-run-repeatable-checks-before-sharing-a-change.py) after attempting it.

```python
import subprocess
import sys
commands = [
    [sys.executable, "06-tools/01-audit.py"],
    [sys.executable, "06-tools/04-walkthrough.py"],
]
for command in commands:
    print("RUN", " ".join(command), flush=True)
    subprocess.run(command, check=True)
print("required local checks passed")
```

3. Save the file. From the repository root run `python3 99-work/05-03-practice.py`. On Windows, substitute `py -3` if that is your interpreter command.
4. Read the output before editing anything else. Compare it with this expected result:

```text
Both validation programs pass, followed by required local checks passed.
```

5. The program ends after printing its result. Any files it creates are listed in the code and remain under 99-work.

## Walk through the mechanism

The subprocess call waits for completion. `check=True` raises an error on a nonzero exit, preventing the final success line from hiding an earlier failure. The full course checker also runs the project graders and unit tests. A workflow file in a numbered example directory is a design artifact until a maintainer configures the host's required reserved path.

The file you typed is your implementation. The linked reference is the instructor's implementation. Use the difference between them to diagnose mistakes rather than replacing your work immediately. If you see SyntaxError or IndentationError, check punctuation and leading spaces on the line shown in the error. If a file cannot be found, first check the current directory and the numbered path.

## Guided failure and repair

Change a command in your scratch copy to reference a missing script. Verify that the success line is not printed. Restore the command and rerun.

Write down the original observation, the changed input, the failure and the repair in `99-work/05-03-evidence.md`. Keep the original course fixtures unchanged. If a process is still running, stop it before repeating a conflicting listener or deleting its data.

## Independent practice

Make one additional small change that preserves the behavior you are trying to learn. Predict the result, run it and explain the observation. A useful explanation names the input, the mechanism and the output; “it works” is too vague. Add one example that your program does not handle and state whether it should reject that input or support it.

## Completion checkpoint

You have typed and run the program, explained the important statements, observed the deliberate failure, repaired it and recorded the result. If you copied the solution without understanding a line, pause and explain that line with a concrete value before moving on. The later platform labs reuse this exact skill.

[Python standard library reference](https://docs.python.org/3/library/) · [Foundation index](00-INDEX.md) · [Course map](../../01-COURSE-MAP.md)

[← Previous lesson](02-write-a-test-suite-that-catches-a-regression.md) · [Next lesson →](../06-orientation-and-workstation/01-a-reproducible-learning-environment.md)
