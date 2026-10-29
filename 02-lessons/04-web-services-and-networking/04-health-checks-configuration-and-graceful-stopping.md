# 04.04 · Health checks configuration and graceful stopping

**Prerequisite:** the preceding foundation lesson. **Time:** 60–90 minutes. **Tools:** Python 3.10+; Git is additionally required in phase 03. Work from the repository root. This is a runnable lesson, not a request to design a system you have not learned yet.

## What the idea means

Configuration separates a program's behavior from hard-coded assumptions. Health is a contract: a liveness check asks whether a process can make progress, while readiness asks whether it should receive traffic. A response at any path is not a useful routing contract. Add explicit routes and an unknown-path response before placing the program behind a Service.

## Build it with the instructor

1. Open a plain-text editor. Create a file named `99-work/04-04-practice.py`. Ensure your editor does not add `.txt` after `.py`.
2. Type the following complete program. Preserve indentation: Python uses leading spaces to group statements. You can compare your work with [14-health-checks-configuration-and-graceful-stopping.py](../../05-project-labs/02-foundations/14-health-checks-configuration-and-graceful-stopping.py) after attempting it.

```python
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            status, body = 200, b'{"status":"ok"}'
        elif self.path == "/":
            status, body = 200, b'{"service":"checkout"}'
        else:
            status, body = 404, b'{"error":"not found"}'
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
port = int(os.environ.get("PEW_PORT", "18082"))
server = HTTPServer(("127.0.0.1", port), Handler)
print("Listening on", port, flush=True)
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
```

3. Save the file. From the repository root run `python3 99-work/04-04-practice.py`. On Windows, substitute `py -3` if that is your interpreter command.
4. Read the output before editing anything else. Compare it with this expected result:

```text
Listening on 18082; /healthz returns 200, / returns 200, /missing returns 404.
```

5. Keep this program running in terminal A. Use terminal B for the next lesson, then stop it with Ctrl-C.

## Walk through the mechanism

The environment sets the port when present, otherwise 18082 is the default. `finally` closes the listener when you stop the process. Test all three routes with the client from lesson 04.02 by changing its URL. A 404 raises HTTPError in urllib; inspect its code rather than treating it as a broken connection.

The file you typed is your implementation. The linked reference is the instructor's implementation. Use the difference between them to diagnose mistakes rather than replacing your work immediately. If you see SyntaxError or IndentationError, check punctuation and leading spaces on the line shown in the error. If a file cannot be found, first check the current directory and the numbered path.

## Guided failure and repair

Use an invalid nonnumeric PEW_PORT and read the conversion error. Restore a valid port. Explain how an early configuration error differs from becoming unhealthy after startup.

Write down the original observation, the changed input, the failure and the repair in `99-work/04-04-evidence.md`. Keep the original course fixtures unchanged. If a process is still running, stop it before repeating a conflicting listener or deleting its data.

## Independent practice

Make one additional small change that preserves the behavior you are trying to learn. Predict the result, run it and explain the observation. A useful explanation names the input, the mechanism and the output; “it works” is too vague. Add one example that your program does not handle and state whether it should reject that input or support it.

## Completion checkpoint

You have typed and run the program, explained the important statements, observed the deliberate failure, repaired it and recorded the result. If you copied the solution without understanding a line, pause and explain that line with a concrete value before moving on. The later platform labs reuse this exact skill.

[Python standard library reference](https://docs.python.org/3/library/) · [Foundation index](00-INDEX.md) · [Course map](../../01-COURSE-MAP.md)

[← Previous lesson](03-dns-addresses-and-connection-failures.md) · [Next lesson →](../05-data-testing-and-ci/01-store-inventory-in-sqlite.md)
