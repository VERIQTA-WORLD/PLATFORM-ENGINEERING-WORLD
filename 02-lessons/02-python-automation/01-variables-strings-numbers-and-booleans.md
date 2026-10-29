# 02.01 · Variables strings numbers and booleans

**Prerequisite:** the preceding foundation lesson. **Time:** 60–90 minutes. **Tools:** Python 3.10+; Git is additionally required in phase 03. Work from the repository root. This is a runnable lesson, not a request to design a system you have not learned yet.

## What the idea means

A variable is a name for a value. A string stores text, a number supports arithmetic and a boolean represents true or false. Configuration languages can blur these distinctions when values arrive as text. A replica count should be numeric; multiplying a string repeats its characters rather than performing capacity arithmetic. Learn the types before writing deployment automation.

## Build it with the instructor

1. Open a plain-text editor. Create a file named `99-work/02-01-practice.py`. Ensure your editor does not add `.txt` after `.py`.
2. Type the following complete program. Preserve indentation: Python uses leading spaces to group statements. You can compare your work with [04-variables-strings-numbers-and-booleans.py](../../05-project-labs/02-foundations/04-variables-strings-numbers-and-booleans.py) after attempting it.

```python
service = "checkout"
replicas = 2
cpu_per_replica = 0.5
public = False
print(service)
print(replicas * cpu_per_replica)
print(type(replicas).__name__)
print("2" * 3)
print(public)
```

3. Save the file. From the repository root run `python3 99-work/02-01-practice.py`. On Windows, substitute `py -3` if that is your interpreter command.
4. Read the output before editing anything else. Compare it with this expected result:

```text
checkout
1.0
int
222
False
```

5. The program ends after printing its result. Any files it creates are listed in the code and remain under 99-work.

## Walk through the mechanism

The equals sign assigns a value; it is not a mathematical claim that two names are identical forever. Quotes make `"2"` text. `type` lets you inspect what kind of value you actually have. A configuration parser should convert or reject unexpected types deliberately. A boolean such as False is a value, while the nonempty string `"False"` can behave as truthy in a condition.

The file you typed is your implementation. The linked reference is the instructor's implementation. Use the difference between them to diagnose mistakes rather than replacing your work immediately. If you see SyntaxError or IndentationError, check punctuation and leading spaces on the line shown in the error. If a file cannot be found, first check the current directory and the numbered path.

## Guided failure and repair

Change replicas to `"2"` and observe that multiplying by 0.5 fails. Repair the type and explain why a platform should validate input before it calculates capacity.

Write down the original observation, the changed input, the failure and the repair in `99-work/02-01-evidence.md`. Keep the original course fixtures unchanged. If a process is still running, stop it before repeating a conflicting listener or deleting its data.

## Independent practice

Make one additional small change that preserves the behavior you are trying to learn. Predict the result, run it and explain the observation. A useful explanation names the input, the mechanism and the output; “it works” is too vague. Add one example that your program does not handle and state whether it should reject that input or support it.

## Completion checkpoint

You have typed and run the program, explained the important statements, observed the deliberate failure, repaired it and recorded the result. If you copied the solution without understanding a line, pause and explain that line with a concrete value before moving on. The later platform labs reuse this exact skill.

[Python standard library reference](https://docs.python.org/3/library/) · [Foundation index](00-INDEX.md) · [Course map](../../01-COURSE-MAP.md)

[← Previous lesson](../01-terminal-and-operating-systems/03-permissions-least-privilege-and-safe-paths.md) · [Next lesson →](02-lists-dictionaries-loops-and-conditions.md)
