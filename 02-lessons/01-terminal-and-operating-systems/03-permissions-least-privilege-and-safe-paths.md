# 01.03 · Permissions least privilege and safe paths

**Prerequisite:** the preceding foundation lesson. **Time:** 60–90 minutes. **Tools:** Python 3.10+; Git is additionally required in phase 03. Work from the repository root. This is a runnable lesson, not a request to design a system you have not learned yet.

## What the idea means

Permissions decide which identities may read, change or execute resources. A path supplied by a user can also cross an intended directory boundary. For example, `../` moves toward a parent directory. Before a platform writes generated files, it must ensure their destination remains inside the allowed root. This lab proves a path containment rule; it does not configure operating-system accounts or replace runtime authorization.

## Build it with the instructor

1. Open a plain-text editor. Create a file named `99-work/01-03-practice.py`. Ensure your editor does not add `.txt` after `.py`.
2. Type the following complete program. Preserve indentation: Python uses leading spaces to group statements. You can compare your work with [03-permissions-least-privilege-and-safe-paths.py](../../05-project-labs/02-foundations/03-permissions-least-privilege-and-safe-paths.py) after attempting it.

```python
from pathlib import Path
root = Path("99-work/03-safe-root").resolve()
root.mkdir(parents=True, exist_ok=True)
def destination(relative):
    candidate = (root / relative).resolve()
    if candidate != root and root not in candidate.parents:
        raise ValueError("destination leaves allowed root")
    return candidate
print(destination("01-note.txt").name)
try:
    destination("../04-outside.txt")
except ValueError as error:
    print(error)
```

3. Save the file. From the repository root run `python3 99-work/01-03-practice.py`. On Windows, substitute `py -3` if that is your interpreter command.
4. Read the output before editing anything else. Compare it with this expected result:

```text
01-note.txt
destination leaves allowed root
```

5. The program ends after printing its result. Any files it creates are listed in the code and remain under 99-work.

## Walk through the mechanism

`resolve` normalizes the location. Comparing actual path ancestry is stronger than testing whether a text string begins with the same letters. A sibling such as `03-safe-root-evil` could share a string prefix without being inside the root. In a hostile filesystem, race conditions and symlinks require stronger OS-level handling; this teaching check illustrates the basic boundary.

The file you typed is your implementation. The linked reference is the instructor's implementation. Use the difference between them to diagnose mistakes rather than replacing your work immediately. If you see SyntaxError or IndentationError, check punctuation and leading spaces on the line shown in the error. If a file cannot be found, first check the current directory and the numbered path.

## Guided failure and repair

Try an absolute path outside the root and verify rejection. Then explain why a process with unrestricted filesystem permissions can still bypass this helper if other code writes directly.

Write down the original observation, the changed input, the failure and the repair in `99-work/01-03-evidence.md`. Keep the original course fixtures unchanged. If a process is still running, stop it before repeating a conflicting listener or deleting its data.

## Independent practice

Make one additional small change that preserves the behavior you are trying to learn. Predict the result, run it and explain the observation. A useful explanation names the input, the mechanism and the output; “it works” is too vague. Add one example that your program does not handle and state whether it should reject that input or support it.

## Completion checkpoint

You have typed and run the program, explained the important statements, observed the deliberate failure, repaired it and recorded the result. If you copied the solution without understanding a line, pause and explain that line with a concrete value before moving on. The later platform labs reuse this exact skill.

[Python standard library reference](https://docs.python.org/3/library/) · [Foundation index](00-INDEX.md) · [Course map](../../01-COURSE-MAP.md)

[← Previous lesson](02-processes-environment-variables-and-ports.md) · [Next lesson →](../02-python-automation/01-variables-strings-numbers-and-booleans.md)
