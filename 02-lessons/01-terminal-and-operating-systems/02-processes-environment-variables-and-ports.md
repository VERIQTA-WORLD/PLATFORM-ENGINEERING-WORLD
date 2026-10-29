# 01.02 · Processes environment variables and ports

**Prerequisite:** the preceding foundation lesson. **Time:** 60–90 minutes. **Tools:** Python 3.10+; Git is additionally required in phase 03. Work from the repository root. This is a runnable lesson, not a request to design a system you have not learned yet.

## What the idea means

A process is a running instance of a program. It has an identifier, arguments, environment variables and access to resources. A child process receives a copy of selected environment settings; changing its environment does not rewrite the parent's settings. Platform automation frequently starts other programs, so it must capture their exit codes instead of assuming that starting them means success.

## Build it with the instructor

1. Open a plain-text editor. Create a file named `99-work/01-02-practice.py`. Ensure your editor does not add `.txt` after `.py`.
2. Type the following complete program. Preserve indentation: Python uses leading spaces to group statements. You can compare your work with [02-processes-environment-variables-and-ports.py](../../05-project-labs/02-foundations/02-processes-environment-variables-and-ports.py) after attempting it.

```python
import os
import subprocess
import sys
child_env = dict(os.environ)
child_env["PEW_SERVICE"] = "checkout"
result = subprocess.run(
    [sys.executable, "-c", "import os; print(os.environ['PEW_SERVICE'])"],
    env=child_env, capture_output=True, text=True, check=False)
print(result.stdout.strip())
print("exit", result.returncode)
print("parent changed", "PEW_SERVICE" in os.environ)
```

3. Save the file. From the repository root run `python3 99-work/01-02-practice.py`. On Windows, substitute `py -3` if that is your interpreter command.
4. Read the output before editing anything else. Compare it with this expected result:

```text
checkout
exit 0
parent changed False
```

5. The program ends after printing its result. Any files it creates are listed in the code and remain under 99-work.

## Walk through the mechanism

`sys.executable` is the interpreter running this program, so the child uses the same interpreter. Arguments are passed as a list, avoiding shell parsing. `capture_output` keeps printed output in the result. `check=False` lets you inspect a failure yourself. The final result assumes your shell did not already define PEW_SERVICE; if it did, record that difference rather than claiming the program changed it.

The file you typed is your implementation. The linked reference is the instructor's implementation. Use the difference between them to diagnose mistakes rather than replacing your work immediately. If you see SyntaxError or IndentationError, check punctuation and leading spaces on the line shown in the error. If a file cannot be found, first check the current directory and the numbered path.

## Guided failure and repair

Change the child code to `import sys; sys.exit(4)`. Observe exit 4 and no service output. Add an explicit branch that reports child failure. Do not silently turn it into success.

Write down the original observation, the changed input, the failure and the repair in `99-work/01-02-evidence.md`. Keep the original course fixtures unchanged. If a process is still running, stop it before repeating a conflicting listener or deleting its data.

## Independent practice

Make one additional small change that preserves the behavior you are trying to learn. Predict the result, run it and explain the observation. A useful explanation names the input, the mechanism and the output; “it works” is too vague. Add one example that your program does not handle and state whether it should reject that input or support it.

## Completion checkpoint

You have typed and run the program, explained the important statements, observed the deliberate failure, repaired it and recorded the result. If you copied the solution without understanding a line, pause and explain that line with a concrete value before moving on. The later platform labs reuse this exact skill.

[Python standard library reference](https://docs.python.org/3/library/) · [Foundation index](00-INDEX.md) · [Course map](../../01-COURSE-MAP.md)

[← Previous lesson](01-create-inspect-and-copy-files.md) · [Next lesson →](03-permissions-least-privilege-and-safe-paths.md)
