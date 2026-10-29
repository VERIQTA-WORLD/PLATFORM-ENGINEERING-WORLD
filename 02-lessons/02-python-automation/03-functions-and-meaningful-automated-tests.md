# 02.03 · Functions and meaningful automated tests

**Prerequisite:** the preceding foundation lesson. **Time:** 60–90 minutes. **Tools:** Python 3.10+; Git is additionally required in phase 03. Work from the repository root. This is a runnable lesson, not a request to design a system you have not learned yet.

## What the idea means

A function names a reusable behavior. Its parameters are inputs and its return value is an output. A function that computes a result without writing files or changing global state is easier to test. Tests compare actual results with expected behavior and should include boundaries, not only one happy example. You will use this pattern later for policy, quotas and reconciliation.

## Build it with the instructor

1. Open a plain-text editor. Create a file named `99-work/02-03-practice.py`. Ensure your editor does not add `.txt` after `.py`.
2. Type the following complete program. Preserve indentation: Python uses leading spaces to group statements. You can compare your work with [06-functions-and-meaningful-automated-tests.py](../../05-project-labs/02-foundations/06-functions-and-meaningful-automated-tests.py) after attempting it.

```python
def required_cpu(replicas, per_replica):
    if type(replicas) is not int or replicas < 1:
        raise ValueError("replicas must be a positive integer")
    return replicas * per_replica
assert required_cpu(2, 0.5) == 1.0
assert required_cpu(4, 0.25) == 1.0
try:
    required_cpu(0, 0.5)
except ValueError:
    print("invalid input rejected")
else:
    raise AssertionError("zero replicas was accepted")
print("checks passed")
```

3. Save the file. From the repository root run `python3 99-work/02-03-practice.py`. On Windows, substitute `py -3` if that is your interpreter command.
4. Read the output before editing anything else. Compare it with this expected result:

```text
invalid input rejected
checks passed
```

5. The program ends after printing its result. Any files it creates are listed in the code and remain under 99-work.

## Walk through the mechanism

`def` introduces a function. Indentation defines its body. `return` sends a value back to the caller. `raise` stops normal execution with a specific error. The `else` on the try statement runs only if no error occurred, so the negative test cannot accidentally pass when invalid input is accepted. Assertions are useful in a learning checker; production validation should use explicit checks because optimized Python can disable assertions.

The file you typed is your implementation. The linked reference is the instructor's implementation. Use the difference between them to diagnose mistakes rather than replacing your work immediately. If you see SyntaxError or IndentationError, check punctuation and leading spaces on the line shown in the error. If a file cannot be found, first check the current directory and the numbered path.

## Guided failure and repair

Change the function to accept zero replicas. Observe that the negative test fails. Restore the rule, then add a test for a string replica count.

Write down the original observation, the changed input, the failure and the repair in `99-work/02-03-evidence.md`. Keep the original course fixtures unchanged. If a process is still running, stop it before repeating a conflicting listener or deleting its data.

## Independent practice

Make one additional small change that preserves the behavior you are trying to learn. Predict the result, run it and explain the observation. A useful explanation names the input, the mechanism and the output; “it works” is too vague. Add one example that your program does not handle and state whether it should reject that input or support it.

## Completion checkpoint

You have typed and run the program, explained the important statements, observed the deliberate failure, repaired it and recorded the result. If you copied the solution without understanding a line, pause and explain that line with a concrete value before moving on. The later platform labs reuse this exact skill.

[Python standard library reference](https://docs.python.org/3/library/) · [Foundation index](00-INDEX.md) · [Course map](../../01-COURSE-MAP.md)

[← Previous lesson](02-lists-dictionaries-loops-and-conditions.md) · [Next lesson →](04-read-json-write-files-and-handle-errors.md)
