# 04.01 · Run a real HTTP service

**Prerequisite:** the preceding foundation lesson. **Time:** 60–90 minutes. **Tools:** Python 3.10+; Git is additionally required in phase 03. Work from the repository root. This is a runnable lesson, not a request to design a system you have not learned yet.

## What the idea means

HTTP is a request/response protocol. A client sends a method and path to a server; the server returns a status, headers and body. A port identifies a listener on a host. Loopback, 127.0.0.1, refers to the same computer. Binding to loopback keeps this lab local. A server normally keeps running until you stop it, so you need a second terminal to send requests while the first is occupied.

## Build it with the instructor

1. Open a plain-text editor. Create a file named `99-work/04-01-practice.py`. Ensure your editor does not add `.txt` after `.py`.
2. Type the following complete program. Preserve indentation: Python uses leading spaces to group statements. You can compare your work with [11-run-a-real-http-service.py](../../05-project-labs/02-foundations/11-run-a-real-http-service.py) after attempting it.

```python
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        payload = json.dumps({"message": "hello platform"}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)
print("Listening at http://127.0.0.1:18081", flush=True)
HTTPServer(("127.0.0.1", 18081), Handler).serve_forever()
```

3. Save the file. From the repository root run `python3 99-work/04-01-practice.py`. On Windows, substitute `py -3` if that is your interpreter command.
4. Read the output before editing anything else. Compare it with this expected result:

```text
Listening at http://127.0.0.1:18081; then the process waits for requests.
```

5. Keep this program running in terminal A. Use terminal B for the next lesson, then stop it with Ctrl-C.

## Walk through the mechanism

A class groups the request-handling behavior. `do_GET` is invoked for each GET request. Encoding turns JSON text into response bytes. Content-Length describes the byte count. The server loop waits for work rather than ending immediately. This single-threaded learning server is intentionally small and has no production TLS or authentication configuration.

The file you typed is your implementation. The linked reference is the instructor's implementation. Use the difference between them to diagnose mistakes rather than replacing your work immediately. If you see SyntaxError or IndentationError, check punctuation and leading spaces on the line shown in the error. If a file cannot be found, first check the current directory and the numbered path.

## Guided failure and repair

While it is running, try starting it again in another terminal. Expect an address-in-use error. Stop the first process with Ctrl-C and explain why two listeners cannot normally own the same address/port pair.

Write down the original observation, the changed input, the failure and the repair in `99-work/04-01-evidence.md`. Keep the original course fixtures unchanged. If a process is still running, stop it before repeating a conflicting listener or deleting its data.

## Independent practice

Make one additional small change that preserves the behavior you are trying to learn. Predict the result, run it and explain the observation. A useful explanation names the input, the mechanism and the output; “it works” is too vague. Add one example that your program does not handle and state whether it should reject that input or support it.

## Completion checkpoint

You have typed and run the program, explained the important statements, observed the deliberate failure, repaired it and recorded the result. If you copied the solution without understanding a line, pause and explain that line with a concrete value before moving on. The later platform labs reuse this exact skill.

[Python standard library reference](https://docs.python.org/3/library/) · [Foundation index](00-INDEX.md) · [Course map](../../01-COURSE-MAP.md)

[← Previous lesson](../03-git-and-safe-change/03-commit-compare-and-revert-safely.md) · [Next lesson →](02-send-requests-and-inspect-responses.md)
