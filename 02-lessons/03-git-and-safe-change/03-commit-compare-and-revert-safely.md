# 03.03 · Commit compare and revert safely

**Prerequisite:** the preceding foundation lesson. **Time:** 60–90 minutes. **Tools:** Python 3.10+; Git is additionally required in phase 03. Work from the repository root. This is a runnable lesson, not a request to design a system you have not learned yet.

## What the idea means

A revert adds a new commit that reverses a prior change. It preserves history, which is useful when others may already depend on it. Editing files back by hand and changing history are different actions. A source revert also does not undo external effects such as a sent email or a dropped database column. Learn source recovery before using it in deployment workflows.

## Build it with the instructor

1. Open a plain-text editor. Create a file named `99-work/03-03-practice.py`. Ensure your editor does not add `.txt` after `.py`.
2. Type the following complete program. Preserve indentation: Python uses leading spaces to group statements. You can compare your work with [10-commit-compare-and-revert-safely.py](../../05-project-labs/02-foundations/10-commit-compare-and-revert-safely.py) after attempting it.

```python
import subprocess
from pathlib import Path
root = Path("99-work/08-git-practice")
def git(*args):
    return subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True, text=True).stdout.strip()
git("add", "01-service.txt")
git("commit", "-m", "Add service ownership")
print("before", "owner=" in (root / "01-service.txt").read_text())
git("revert", "--no-edit", "HEAD")
print("after", "owner=" in (root / "01-service.txt").read_text())
print(git("log", "-1", "--format=%s"))
```

3. Save the file. From the repository root run `python3 99-work/03-03-practice.py`. On Windows, substitute `py -3` if that is your interpreter command.
4. Read the output before editing anything else. Compare it with this expected result:

```text
before True
after False
Revert "Add service ownership"
```

5. The program ends after printing its result. Any files it creates are listed in the code and remain under 99-work.

## Walk through the mechanism

The last commit from lesson 03.02 becomes the target of `revert`. The new commit restores the prior file content without deleting the intervening history. If the working tree contains unrelated edits, stop and inspect them before attempting recovery. Do not use destructive reset commands to solve a situation you have not understood.

The file you typed is your implementation. The linked reference is the instructor's implementation. Use the difference between them to diagnose mistakes rather than replacing your work immediately. If you see SyntaxError or IndentationError, check punctuation and leading spaces on the line shown in the error. If a file cannot be found, first check the current directory and the numbered path.

## Guided failure and repair

Inspect the last three commit subjects. Explain why the ownership addition remains visible in history after the revert and why you would retain that audit trail.

Write down the original observation, the changed input, the failure and the repair in `99-work/03-03-evidence.md`. Keep the original course fixtures unchanged. If a process is still running, stop it before repeating a conflicting listener or deleting its data.

## Independent practice

Make one additional small change that preserves the behavior you are trying to learn. Predict the result, run it and explain the observation. A useful explanation names the input, the mechanism and the output; “it works” is too vague. Add one example that your program does not handle and state whether it should reject that input or support it.

## Completion checkpoint

You have typed and run the program, explained the important statements, observed the deliberate failure, repaired it and recorded the result. If you copied the solution without understanding a line, pause and explain that line with a concrete value before moving on. The later platform labs reuse this exact skill.

[Python standard library reference](https://docs.python.org/3/library/) · [Foundation index](00-INDEX.md) · [Course map](../../01-COURSE-MAP.md)

[← Previous lesson](02-review-a-change-on-a-branch.md) · [Next lesson →](../04-web-services-and-networking/01-run-a-real-http-service.md)
