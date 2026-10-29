# 03.02 · Review a change on a branch

**Prerequisite:** the preceding foundation lesson. **Time:** 60–90 minutes. **Tools:** Python 3.10+; Git is additionally required in phase 03. Work from the repository root. This is a runnable lesson, not a request to design a system you have not learned yet.

## What the idea means

A branch names a moving position in history. It lets you prepare a change independently and compare it with a baseline. Review should focus on behavior: a one-line change can have a large operational effect. Before merging, inspect the actual diff and run relevant checks. Branches do not isolate runtime infrastructure unless a separate process provisions it.

## Build it with the instructor

1. Open a plain-text editor. Create a file named `99-work/03-02-practice.py`. Ensure your editor does not add `.txt` after `.py`.
2. Type the following complete program. Preserve indentation: Python uses leading spaces to group statements. You can compare your work with [09-review-a-change-on-a-branch.py](../../05-project-labs/02-foundations/09-review-a-change-on-a-branch.py) after attempting it.

```python
import subprocess
from pathlib import Path
root = Path("99-work/08-git-practice")
def git(*args):
    return subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True, text=True).stdout.strip()
git("switch", "-c", "lesson-add-owner")
(root / "01-service.txt").write_text("service=checkout\nowner=commerce\n")
print(git("diff", "--stat"))
print(git("diff", "--", "01-service.txt"))
```

3. Save the file. From the repository root run `python3 99-work/03-02-practice.py`. On Windows, substitute `py -3` if that is your interpreter command.
4. Read the output before editing anything else. Compare it with this expected result:

```text
A diff describing 01-service.txt and a new +owner=commerce line. Exact spacing and diff headers vary.
```

5. The program ends after printing its result. Any files it creates are listed in the code and remain under 99-work.

## Walk through the mechanism

This lesson depends on the previous Git repository. `switch -c` creates a new branch; use it once for this exercise. `diff` shows uncommitted changes. The plus-prefixed line is added content, not a command to type. Git history records what changed; a reviewer still needs the user reason and verification evidence.

The file you typed is your implementation. The linked reference is the instructor's implementation. Use the difference between them to diagnose mistakes rather than replacing your work immediately. If you see SyntaxError or IndentationError, check punctuation and leading spaces on the line shown in the error. If a file cannot be found, first check the current directory and the numbered path.

## Guided failure and repair

Change owner to an empty value and compare the diff. Explain which test would catch that invalid ownership even though the file is valid text.

Write down the original observation, the changed input, the failure and the repair in `99-work/03-02-evidence.md`. Keep the original course fixtures unchanged. If a process is still running, stop it before repeating a conflicting listener or deleting its data.

## Independent practice

Make one additional small change that preserves the behavior you are trying to learn. Predict the result, run it and explain the observation. A useful explanation names the input, the mechanism and the output; “it works” is too vague. Add one example that your program does not handle and state whether it should reject that input or support it.

## Completion checkpoint

You have typed and run the program, explained the important statements, observed the deliberate failure, repaired it and recorded the result. If you copied the solution without understanding a line, pause and explain that line with a concrete value before moving on. The later platform labs reuse this exact skill.

[Python standard library reference](https://docs.python.org/3/library/) · [Foundation index](00-INDEX.md) · [Course map](../../01-COURSE-MAP.md)

[← Previous lesson](01-create-a-repository-and-make-a-first-commit.md) · [Next lesson →](03-commit-compare-and-revert-safely.md)
