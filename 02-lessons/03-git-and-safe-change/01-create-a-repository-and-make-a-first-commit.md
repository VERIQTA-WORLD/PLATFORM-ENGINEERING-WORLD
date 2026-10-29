# 03.01 · Create a repository and make a first commit

**Prerequisite:** the preceding foundation lesson. **Time:** 60–90 minutes. **Tools:** Python 3.10+; Git is additionally required in phase 03. Work from the repository root. This is a runnable lesson, not a request to design a system you have not learned yet.

## What the idea means

A repository records versions of content. The working tree is the files you edit; the staging area selects the next snapshot; a commit stores that snapshot with metadata and parent history. Git does not automatically upload your work. A local repository and a hosted repository are different things. The exercise uses a separate, disposable repository so you do not modify the course history.

## Build it with the instructor

1. Open a plain-text editor. Create a file named `99-work/03-01-practice.py`. Ensure your editor does not add `.txt` after `.py`.
2. Type the following complete program. Preserve indentation: Python uses leading spaces to group statements. You can compare your work with [08-create-a-repository-and-make-a-first-commit.py](../../05-project-labs/02-foundations/08-create-a-repository-and-make-a-first-commit.py) after attempting it.

```python
import subprocess
from pathlib import Path
root = Path("99-work/08-git-practice")
root.mkdir(parents=True, exist_ok=True)
def git(*args):
    return subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True, text=True).stdout.strip()
git("init", "-b", "main")
git("config", "user.name", "Course Learner")
git("config", "user.email", "learner@example.com")
(root / "01-service.txt").write_text("service=checkout\n")
git("add", "01-service.txt")
git("commit", "-m", "Record the first service")
print(git("log", "-1", "--format=%s"))
print("clean", not git("status", "--porcelain"))
```

3. Save the file. From the repository root run `python3 99-work/03-01-practice.py`. On Windows, substitute `py -3` if that is your interpreter command.
4. Read the output before editing anything else. Compare it with this expected result:

```text
Record the first service
clean True
```

5. The program ends after printing its result. Any files it creates are listed in the code and remain under 99-work.

## Walk through the mechanism

The script runs ordinary Git commands and checks their exit statuses. `-C` tells Git which directory to use. The name and email are local fictional exercise metadata, not account credentials. `add` selects content for the commit. A clean working tree means no uncommitted changes remain; it does not prove the application works. Run this exercise in a fresh directory if repeating to avoid an unnecessary second commit.

The file you typed is your implementation. The linked reference is the instructor's implementation. Use the difference between them to diagnose mistakes rather than replacing your work immediately. If you see SyntaxError or IndentationError, check punctuation and leading spaces on the line shown in the error. If a file cannot be found, first check the current directory and the numbered path.

## Guided failure and repair

Edit 01-service.txt without committing and inspect `git -C 99-work/08-git-practice diff`. Explain why log still shows the old committed snapshot.

Write down the original observation, the changed input, the failure and the repair in `99-work/03-01-evidence.md`. Keep the original course fixtures unchanged. If a process is still running, stop it before repeating a conflicting listener or deleting its data.

## Independent practice

Make one additional small change that preserves the behavior you are trying to learn. Predict the result, run it and explain the observation. A useful explanation names the input, the mechanism and the output; “it works” is too vague. Add one example that your program does not handle and state whether it should reject that input or support it.

## Completion checkpoint

You have typed and run the program, explained the important statements, observed the deliberate failure, repaired it and recorded the result. If you copied the solution without understanding a line, pause and explain that line with a concrete value before moving on. The later platform labs reuse this exact skill.

[Python standard library reference](https://docs.python.org/3/library/) · [Foundation index](00-INDEX.md) · [Course map](../../01-COURSE-MAP.md)

[← Previous lesson](../02-python-automation/04-read-json-write-files-and-handle-errors.md) · [Next lesson →](02-review-a-change-on-a-branch.md)
