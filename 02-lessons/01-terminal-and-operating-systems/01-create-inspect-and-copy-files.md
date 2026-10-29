# 01.01 · Create inspect and copy files

**Prerequisite:** the preceding foundation lesson. **Time:** 60–90 minutes. **Tools:** Python 3.10+; Git is additionally required in phase 03. Work from the repository root. This is a runnable lesson, not a request to design a system you have not learned yet.

## What the idea means

A filesystem stores bytes in named files organized into directories. Automation must know which directory it operates in. A file can contain text or binary data; changing an extension does not convert its contents. In this lab, you create a dedicated directory, save a text file, inspect its size and copy it. The copy is independent content, not another name pointing at the same file.

## Build it with the instructor

1. Open a plain-text editor. Create a file named `99-work/01-01-practice.py`. Ensure your editor does not add `.txt` after `.py`.
2. Type the following complete program. Preserve indentation: Python uses leading spaces to group statements. You can compare your work with [01-create-inspect-and-copy-files.py](../../05-project-labs/02-foundations/01-create-inspect-and-copy-files.py) after attempting it.

```python
from pathlib import Path
root = Path("99-work/01-files")
root.mkdir(parents=True, exist_ok=True)
source = root / "01-message.txt"
source.write_text("hello platform\n", encoding="utf-8")
copy = root / "02-copy.txt"
copy.write_bytes(source.read_bytes())
print(source.name)
print(source.stat().st_size)
print(source.read_bytes() == copy.read_bytes())
```

3. Save the file. From the repository root run `python3 99-work/01-01-practice.py`. On Windows, substitute `py -3` if that is your interpreter command.
4. Read the output before editing anything else. Compare it with this expected result:

```text
01-message.txt
15
True
```

5. The program ends after printing its result. Any files it creates are listed in the code and remain under 99-work.

## Walk through the mechanism

`Path` represents a location. `mkdir` creates the parent directory if needed. `write_text` saves characters encoded as bytes; the newline is one extra byte here. `read_bytes` and `write_bytes` preserve the actual bytes. The final comparison checks content rather than merely checking that a filename exists.

The file you typed is your implementation. The linked reference is the instructor's implementation. Use the difference between them to diagnose mistakes rather than replacing your work immediately. If you see SyntaxError or IndentationError, check punctuation and leading spaces on the line shown in the error. If a file cannot be found, first check the current directory and the numbered path.

## Guided failure and repair

Change only the copy to a different sentence and compare the two files again. Explain why different filenames do not guarantee different content and matching filenames in different directories do not guarantee equal content.

Write down the original observation, the changed input, the failure and the repair in `99-work/01-01-evidence.md`. Keep the original course fixtures unchanged. If a process is still running, stop it before repeating a conflicting listener or deleting its data.

## Independent practice

Make one additional small change that preserves the behavior you are trying to learn. Predict the result, run it and explain the observation. A useful explanation names the input, the mechanism and the output; “it works” is too vague. Add one example that your program does not handle and state whether it should reject that input or support it.

## Completion checkpoint

You have typed and run the program, explained the important statements, observed the deliberate failure, repaired it and recorded the result. If you copied the solution without understanding a line, pause and explain that line with a concrete value before moving on. The later platform labs reuse this exact skill.

[Python standard library reference](https://docs.python.org/3/library/) · [Foundation index](00-INDEX.md) · [Course map](../../01-COURSE-MAP.md)

[← Previous lesson](../00-starting-from-zero/03-read-commands-paths-and-error-messages.md) · [Next lesson →](02-processes-environment-variables-and-ports.md)
