# 02.04 · Read JSON write files and handle errors

**Prerequisite:** the preceding foundation lesson. **Time:** 60–90 minutes. **Tools:** Python 3.10+; Git is additionally required in phase 03. Work from the repository root. This is a runnable lesson, not a request to design a system you have not learned yet.

## What the idea means

JSON stores structured data using objects, arrays, strings, numbers, booleans and null. Python dictionaries resemble JSON objects but Python code and JSON are not the same language: Python uses True, while JSON uses true. Read bytes as text, parse the text into values, validate their meaning, then serialize deliberately. Parsing alone cannot prove a configuration is safe.

## Build it with the instructor

1. Open a plain-text editor. Create a file named `99-work/02-04-practice.py`. Ensure your editor does not add `.txt` after `.py`.
2. Type the following complete program. Preserve indentation: Python uses leading spaces to group statements. You can compare your work with [07-read-json-write-files-and-handle-errors.py](../../05-project-labs/02-foundations/07-read-json-write-files-and-handle-errors.py) after attempting it.

```python
import json
from pathlib import Path
path = Path("04-fixtures/02-desired.json")
catalog = json.loads(path.read_text())
service = catalog["services"][0]
print(service["name"])
print(service["replicas"])
try:
    json.loads('{"replicas": }')
except json.JSONDecodeError:
    print("malformed JSON rejected")
print(json.dumps({"auth": True}, sort_keys=True))
```

3. Save the file. From the repository root run `python3 99-work/02-04-practice.py`. On Windows, substitute `py -3` if that is your interpreter command.
4. Read the output before editing anything else. Compare it with this expected result:

```text
checkout
2
malformed JSON rejected
{"auth": true}
```

5. The program ends after printing its result. Any files it creates are listed in the code and remain under 99-work.

## Walk through the mechanism

`json.loads` parses a string; `json.dumps` creates a JSON string. The names do not read or write files by themselves. The deliberately malformed document is caught narrowly as a JSON decoding error. Catching every exception and printing success would hide both invalid input and programming bugs.

The file you typed is your implementation. The linked reference is the instructor's implementation. Use the difference between them to diagnose mistakes rather than replacing your work immediately. If you see SyntaxError or IndentationError, check punctuation and leading spaces on the line shown in the error. If a file cannot be found, first check the current directory and the numbered path.

## Guided failure and repair

Change the valid fixture only in a copy: make owner empty while keeping valid JSON syntax. Run the platform validator later in phase 09 and compare syntax failure with a semantic rejection.

Write down the original observation, the changed input, the failure and the repair in `99-work/02-04-evidence.md`. Keep the original course fixtures unchanged. If a process is still running, stop it before repeating a conflicting listener or deleting its data.

## Independent practice

Make one additional small change that preserves the behavior you are trying to learn. Predict the result, run it and explain the observation. A useful explanation names the input, the mechanism and the output; “it works” is too vague. Add one example that your program does not handle and state whether it should reject that input or support it.

## Completion checkpoint

You have typed and run the program, explained the important statements, observed the deliberate failure, repaired it and recorded the result. If you copied the solution without understanding a line, pause and explain that line with a concrete value before moving on. The later platform labs reuse this exact skill.

[Python standard library reference](https://docs.python.org/3/library/) · [Foundation index](00-INDEX.md) · [Course map](../../01-COURSE-MAP.md)

[← Previous lesson](03-functions-and-meaningful-automated-tests.md) · [Next lesson →](../03-git-and-safe-change/01-create-a-repository-and-make-a-first-commit.md)
