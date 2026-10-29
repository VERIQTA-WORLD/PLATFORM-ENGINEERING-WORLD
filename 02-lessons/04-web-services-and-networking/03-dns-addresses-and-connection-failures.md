# 04.03 · DNS addresses and connection failures

**Prerequisite:** the preceding foundation lesson. **Time:** 60–90 minutes. **Tools:** Python 3.10+; Git is additionally required in phase 03. Work from the repository root. This is a runnable lesson, not a request to design a system you have not learned yet.

## What the idea means

DNS translates names into records that clients use to locate services. Name resolution is not an authorization decision. The special hostname localhost usually resolves to loopback addresses configured by the operating system. It may produce IPv4, IPv6 or both. A service listening on IPv4 loopback may not accept connections to an IPv6-only result. Diagnose the exact address and listener rather than changing application credentials.

## Build it with the instructor

1. Open a plain-text editor. Create a file named `99-work/04-03-practice.py`. Ensure your editor does not add `.txt` after `.py`.
2. Type the following complete program. Preserve indentation: Python uses leading spaces to group statements. You can compare your work with [13-dns-addresses-and-connection-failures.py](../../05-project-labs/02-foundations/13-dns-addresses-and-connection-failures.py) after attempting it.

```python
import socket
addresses = socket.getaddrinfo("localhost", 18081, type=socket.SOCK_STREAM)
print("loopback results", len(addresses) > 0)
print("IPv4 loopback", socket.inet_aton("127.0.0.1").hex())
try:
    with socket.create_connection(("127.0.0.1", 18089), timeout=1):
        print("unexpected listener on test port")
except OSError:
    print("unused test port is not reachable")
```

3. Save the file. From the repository root run `python3 99-work/04-03-practice.py`. On Windows, substitute `py -3` if that is your interpreter command.
4. Read the output before editing anything else. Compare it with this expected result:

```text
loopback results True
IPv4 loopback 7f000001
unused test port is not reachable (unless you already have a listener on 18089)
```

5. The program ends after printing its result. Any files it creates are listed in the code and remain under 99-work.

## Walk through the mechanism

`getaddrinfo` returns connection candidates rather than a single universal answer. `create_connection` attempts a transport connection. The unused port deliberately isolates listener failure from DNS because its destination is already numeric. If a process actually uses that port, select another unused port and record the difference.

The file you typed is your implementation. The linked reference is the instructor's implementation. Use the difference between them to diagnose mistakes rather than replacing your work immediately. If you see SyntaxError or IndentationError, check punctuation and leading spaces on the line shown in the error. If a file cannot be found, first check the current directory and the numbered path.

## Guided failure and repair

Compare the server URL using localhost and 127.0.0.1. Record the result and explain that a successful DNS lookup does not prove there is a listening process.

Write down the original observation, the changed input, the failure and the repair in `99-work/04-03-evidence.md`. Keep the original course fixtures unchanged. If a process is still running, stop it before repeating a conflicting listener or deleting its data.

## Independent practice

Make one additional small change that preserves the behavior you are trying to learn. Predict the result, run it and explain the observation. A useful explanation names the input, the mechanism and the output; “it works” is too vague. Add one example that your program does not handle and state whether it should reject that input or support it.

## Completion checkpoint

You have typed and run the program, explained the important statements, observed the deliberate failure, repaired it and recorded the result. If you copied the solution without understanding a line, pause and explain that line with a concrete value before moving on. The later platform labs reuse this exact skill.

[Python standard library reference](https://docs.python.org/3/library/) · [Foundation index](00-INDEX.md) · [Course map](../../01-COURSE-MAP.md)

[← Previous lesson](02-send-requests-and-inspect-responses.md) · [Next lesson →](04-health-checks-configuration-and-graceful-stopping.md)
