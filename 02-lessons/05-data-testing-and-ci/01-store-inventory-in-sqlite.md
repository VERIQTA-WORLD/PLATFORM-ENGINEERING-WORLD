# 05.01 · Store inventory in SQLite

**Prerequisite:** the preceding foundation lesson. **Time:** 60–90 minutes. **Tools:** Python 3.10+; Git is additionally required in phase 03. Work from the repository root. This is a runnable lesson, not a request to design a system you have not learned yet.

## What the idea means

A database stores records with rules and query behavior. A primary key identifies a row and can prevent duplicates. SQL describes the data operation; parameters keep values separate from SQL text. SQLite stores a database in a local file and supports transactions, making it useful for learning durable control-plane behavior. It is not a substitute for reasoning about concurrency and failure.

## Build it with the instructor

1. Open a plain-text editor. Create a file named `99-work/05-01-practice.py`. Ensure your editor does not add `.txt` after `.py`.
2. Type the following complete program. Preserve indentation: Python uses leading spaces to group statements. You can compare your work with [15-store-inventory-in-sqlite.py](../../05-project-labs/02-foundations/15-store-inventory-in-sqlite.py) after attempting it.

```python
import sqlite3
from pathlib import Path
path = Path("99-work/16-inventory.sqlite")
path.parent.mkdir(parents=True, exist_ok=True)
with sqlite3.connect(path) as connection:
    connection.execute("CREATE TABLE IF NOT EXISTS services (name TEXT PRIMARY KEY, owner TEXT NOT NULL)")
    connection.execute("INSERT OR IGNORE INTO services VALUES (?, ?)", ("checkout", "commerce"))
    rows = connection.execute("SELECT name, owner FROM services ORDER BY name").fetchall()
    print(rows)
try:
    with sqlite3.connect(path) as connection:
        connection.execute("INSERT INTO services VALUES (?, ?)", ("checkout", "search"))
except sqlite3.IntegrityError:
    print("duplicate identity rejected")
```

3. Save the file. From the repository root run `python3 99-work/05-01-practice.py`. On Windows, substitute `py -3` if that is your interpreter command.
4. Read the output before editing anything else. Compare it with this expected result:

```text
[('checkout', 'commerce')]
duplicate identity rejected
```

5. The program ends after printing its result. Any files it creates are listed in the code and remain under 99-work.

## Walk through the mechanism

The table definition gives name a uniqueness constraint. `?` placeholders bind values without concatenating them into a SQL command. The connection context commits a successful transaction and rolls back an exception; the connection object itself should be explicitly closed in longer-running programs. A SELECT without ORDER BY has no guaranteed presentation order.

The file you typed is your implementation. The linked reference is the instructor's implementation. Use the difference between them to diagnose mistakes rather than replacing your work immediately. If you see SyntaxError or IndentationError, check punctuation and leading spaces on the line shown in the error. If a file cannot be found, first check the current directory and the numbered path.

## Guided failure and repair

Insert a different service, then query the rows in order. Explain why a pre-insert “does it exist?” check alone can race while the database uniqueness constraint remains authoritative.

Write down the original observation, the changed input, the failure and the repair in `99-work/05-01-evidence.md`. Keep the original course fixtures unchanged. If a process is still running, stop it before repeating a conflicting listener or deleting its data.

## Independent practice

Make one additional small change that preserves the behavior you are trying to learn. Predict the result, run it and explain the observation. A useful explanation names the input, the mechanism and the output; “it works” is too vague. Add one example that your program does not handle and state whether it should reject that input or support it.

## Completion checkpoint

You have typed and run the program, explained the important statements, observed the deliberate failure, repaired it and recorded the result. If you copied the solution without understanding a line, pause and explain that line with a concrete value before moving on. The later platform labs reuse this exact skill.

[Python standard library reference](https://docs.python.org/3/library/) · [Foundation index](00-INDEX.md) · [Course map](../../01-COURSE-MAP.md)

[← Previous lesson](../04-web-services-and-networking/04-health-checks-configuration-and-graceful-stopping.md) · [Next lesson →](02-write-a-test-suite-that-catches-a-regression.md)
