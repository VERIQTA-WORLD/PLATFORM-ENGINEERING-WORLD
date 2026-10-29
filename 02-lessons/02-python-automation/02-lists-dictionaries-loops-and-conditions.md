# 02.02 · Lists dictionaries loops and conditions

**Prerequisite:** the preceding foundation lesson. **Time:** 60–90 minutes. **Tools:** Python 3.10+; Git is additionally required in phase 03. Work from the repository root. This is a runnable lesson, not a request to design a system you have not learned yet.

## What the idea means

A list holds an ordered sequence of values. A dictionary associates keys with values. A service catalog can be a list of dictionaries: each dictionary is one service. A loop visits each service, and a condition chooses what to do. This is the beginning of inventory automation. Avoid copying a separate check for each service; encode one rule and apply it to every item.

## Build it with the instructor

1. Open a plain-text editor. Create a file named `99-work/02-02-practice.py`. Ensure your editor does not add `.txt` after `.py`.
2. Type the following complete program. Preserve indentation: Python uses leading spaces to group statements. You can compare your work with [05-lists-dictionaries-loops-and-conditions.py](../../05-project-labs/02-foundations/05-lists-dictionaries-loops-and-conditions.py) after attempting it.

```python
services = [
    {"name": "checkout", "owner": "commerce"},
    {"name": "search", "owner": ""},
]
missing = []
for service in services:
    if not service["owner"]:
        missing.append(service["name"])
print("services", len(services))
print("missing owners", missing)
```

3. Save the file. From the repository root run `python3 99-work/02-02-practice.py`. On Windows, substitute `py -3` if that is your interpreter command.
4. Read the output before editing anything else. Compare it with this expected result:

```text
services 2
missing owners ['search']
```

5. The program ends after printing its result. Any files it creates are listed in the code and remain under 99-work.

## Walk through the mechanism

Square brackets access a key or list item. The condition checks whether owner is empty. `append` adds a result to the collection. The code gathers all missing owners instead of stopping after the first one, giving a user more useful feedback. A production contract should also reject missing keys and wrong value types; this first program assumes both keys exist.

The file you typed is your implementation. The linked reference is the instructor's implementation. Use the difference between them to diagnose mistakes rather than replacing your work immediately. If you see SyntaxError or IndentationError, check punctuation and leading spaces on the line shown in the error. If a file cannot be found, first check the current directory and the numbered path.

## Guided failure and repair

Remove the owner key entirely and read the KeyError. Replace direct lookup with `service.get("owner", "")` and explain the difference between a missing value and a deliberate empty value.

Write down the original observation, the changed input, the failure and the repair in `99-work/02-02-evidence.md`. Keep the original course fixtures unchanged. If a process is still running, stop it before repeating a conflicting listener or deleting its data.

## Independent practice

Make one additional small change that preserves the behavior you are trying to learn. Predict the result, run it and explain the observation. A useful explanation names the input, the mechanism and the output; “it works” is too vague. Add one example that your program does not handle and state whether it should reject that input or support it.

## Completion checkpoint

You have typed and run the program, explained the important statements, observed the deliberate failure, repaired it and recorded the result. If you copied the solution without understanding a line, pause and explain that line with a concrete value before moving on. The later platform labs reuse this exact skill.

[Python standard library reference](https://docs.python.org/3/library/) · [Foundation index](00-INDEX.md) · [Course map](../../01-COURSE-MAP.md)

[← Previous lesson](01-variables-strings-numbers-and-booleans.md) · [Next lesson →](03-functions-and-meaningful-automated-tests.md)
