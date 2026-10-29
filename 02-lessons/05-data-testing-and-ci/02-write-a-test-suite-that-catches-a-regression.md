# 05.02 · Write a test suite that catches a regression

**Prerequisite:** the preceding foundation lesson. **Time:** 60–90 minutes. **Tools:** Python 3.10+; Git is additionally required in phase 03. Work from the repository root. This is a runnable lesson, not a request to design a system you have not learned yet.

## What the idea means

A test suite is executable evidence for a defined behavior. It cannot prove every possible property. Start with a small function and check ordinary, boundary and invalid input. A test that merely calls a function without inspecting the result may stay green after a meaningful regression. Learn to make a test fail deliberately so you know it is connected to the behavior.

## Build it with the instructor

1. Open a plain-text editor. Create a file named `99-work/05-02-practice.py`. Ensure your editor does not add `.txt` after `.py`.
2. Type the following complete program. Preserve indentation: Python uses leading spaces to group statements. You can compare your work with [16-write-a-test-suite-that-catches-a-regression.py](../../05-project-labs/02-foundations/16-write-a-test-suite-that-catches-a-regression.py) after attempting it.

```python
import unittest
def allow_public(public, auth):
    return not public or auth
class PolicyTests(unittest.TestCase):
    def test_private_service(self):
        self.assertTrue(allow_public(False, False))
    def test_authenticated_public_service(self):
        self.assertTrue(allow_public(True, True))
    def test_unauthenticated_public_service(self):
        self.assertFalse(allow_public(True, False))
if __name__ == "__main__":
    unittest.main()
```

3. Save the file. From the repository root run `python3 99-work/05-02-practice.py`. On Windows, substitute `py -3` if that is your interpreter command.
4. Read the output before editing anything else. Compare it with this expected result:

```text
Ran 3 tests ... OK (timing and formatting vary).
```

5. The program ends after printing its result. Any files it creates are listed in the code and remain under 99-work.

## Walk through the mechanism

Each method beginning with test is an independent check. assertFalse verifies the denied case rather than only counting that code executed. The function is a simplified rule over claimed booleans. It does not authenticate network traffic. Later labs bind authorization to a caller and enforce it at the data mutation boundary.

The file you typed is your implementation. The linked reference is the instructor's implementation. Use the difference between them to diagnose mistakes rather than replacing your work immediately. If you see SyntaxError or IndentationError, check punctuation and leading spaces on the line shown in the error. If a file cannot be found, first check the current directory and the numbered path.

## Guided failure and repair

Change the function to always return True. Confirm the denied-case test fails. Repair it, then explain why a green suite with no negative case would have missed this regression.

Write down the original observation, the changed input, the failure and the repair in `99-work/05-02-evidence.md`. Keep the original course fixtures unchanged. If a process is still running, stop it before repeating a conflicting listener or deleting its data.

## Independent practice

Make one additional small change that preserves the behavior you are trying to learn. Predict the result, run it and explain the observation. A useful explanation names the input, the mechanism and the output; “it works” is too vague. Add one example that your program does not handle and state whether it should reject that input or support it.

## Completion checkpoint

You have typed and run the program, explained the important statements, observed the deliberate failure, repaired it and recorded the result. If you copied the solution without understanding a line, pause and explain that line with a concrete value before moving on. The later platform labs reuse this exact skill.

[Python standard library reference](https://docs.python.org/3/library/) · [Foundation index](00-INDEX.md) · [Course map](../../01-COURSE-MAP.md)

[← Previous lesson](01-store-inventory-in-sqlite.md) · [Next lesson →](03-run-repeatable-checks-before-sharing-a-change.md)
