# 04.02 · Send requests and inspect responses

**Prerequisite:** the preceding foundation lesson. **Time:** 60–90 minutes. **Tools:** Python 3.10+; Git is additionally required in phase 03. Work from the repository root. This is a runnable lesson, not a request to design a system you have not learned yet.

## What the idea means

A URL identifies a scheme, host, optional port and path. HTTP status and JSON body are separate parts of a response. A 200 response means the server handled the request according to its contract; correctness still depends on the body. A client must set timeouts so that a stalled dependency cannot hold work indefinitely. Retry only when the operation and error make retry safe.

## Build it with the instructor

1. Open a plain-text editor. Create a file named `99-work/04-02-practice.py`. Ensure your editor does not add `.txt` after `.py`.
2. Type the following complete program. Preserve indentation: Python uses leading spaces to group statements. You can compare your work with [12-send-requests-and-inspect-responses.py](../../05-project-labs/02-foundations/12-send-requests-and-inspect-responses.py) after attempting it.

```python
import json
from urllib.request import urlopen
with urlopen("http://127.0.0.1:18081/", timeout=3) as response:
    print(response.status)
    print(response.headers.get("Content-Type"))
    body = json.load(response)
    print(body["message"])
```

3. Save the file. From the repository root run `python3 99-work/04-02-practice.py`. On Windows, substitute `py -3` if that is your interpreter command.
4. Read the output before editing anything else. Compare it with this expected result:

```text
200
application/json
hello platform
```

5. The program ends after printing its result. Any files it creates are listed in the code and remain under 99-work.

## Walk through the mechanism

Keep the server from the previous lesson running in terminal A. Run the client in terminal B. `with` closes the response after reading. `json.load` parses the response stream. The timeout bounds waiting. Your server currently returns the same response for every path; that is a limitation to fix, not proof that every URL is meaningful.

The file you typed is your implementation. The linked reference is the instructor's implementation. Use the difference between them to diagnose mistakes rather than replacing your work immediately. If you see SyntaxError or IndentationError, check punctuation and leading spaces on the line shown in the error. If a file cannot be found, first check the current directory and the numbered path.

## Guided failure and repair

Stop the server, then run the client again. Observe connection refusal. Restart the server and verify recovery. Do not describe a refused connection as an authentication failure.

Write down the original observation, the changed input, the failure and the repair in `99-work/04-02-evidence.md`. Keep the original course fixtures unchanged. If a process is still running, stop it before repeating a conflicting listener or deleting its data.

## Independent practice

Make one additional small change that preserves the behavior you are trying to learn. Predict the result, run it and explain the observation. A useful explanation names the input, the mechanism and the output; “it works” is too vague. Add one example that your program does not handle and state whether it should reject that input or support it.

## Completion checkpoint

You have typed and run the program, explained the important statements, observed the deliberate failure, repaired it and recorded the result. If you copied the solution without understanding a line, pause and explain that line with a concrete value before moving on. The later platform labs reuse this exact skill.

[Python standard library reference](https://docs.python.org/3/library/) · [Foundation index](00-INDEX.md) · [Course map](../../01-COURSE-MAP.md)

[← Previous lesson](01-run-a-real-http-service.md) · [Next lesson →](03-dns-addresses-and-connection-failures.md)
