# Project 06 · Durable Operations

**Level:** advanced implementation. **Time:** 2–4 hours. **Deliverable:** Durable scoped request identity, conflict rejection and preserved row count. Work from the repository root. Use Python 3.10+ and synthetic data. No cloud account is needed.

## Understand what you are building

A client can time out after a server accepts work. An idempotency key lets a repeated equivalent request return the same operation. Scope the key to the tenant and bind it to normalized request content. The database uniqueness constraint is authoritative. An in-memory dictionary loses its history on process restart and can race between workers. This exercise uses a transaction and a unique key in SQLite.

## Stage 1 · Read the interface and see the missing behavior

Open [01-starter.py](01-starter.py). The function is named `accept` and takes `connection, tenant, key, request`. `NotImplementedError` is intentional: this is the place where you supply the behavior. Read [03-grade.py](03-grade.py) before changing code so the examples and failure expectations are concrete.

Run:

```sh
python3 05-project-labs/06-durable-operations/03-grade.py
```

Expected: a nonzero exit with NotImplementedError. This is a starting point, not a broken installation. If the file itself cannot be found, correct your current directory before implementing anything.

## Stage 2 · Build the first passing behavior

Create the table and commit schema initialization before beginning the operation transaction. Normalize JSON with sorted keys so field order does not change identity. Acquire a write transaction before looking up the key. If found, compare the body and return the existing ID only for equivalent content. If absent, insert a new ID and commit. Roll back on every exception, then re-raise: the caller needs to see rejection. This function owns its transaction and should not be called inside another active transaction.

Create `99-work/06-project` using your editor or file manager, copy `01-starter.py` there as `01-implementation.py`, and edit your copy. Keep the supplied starter so you can repeat the exercise.

```sh
python3 05-project-labs/06-durable-operations/03-grade.py --implementation 99-work/06-project/01-implementation.py
```

An AssertionError names a behavior that is still wrong. Fix that behavior rather than removing the assertion. Read stack traces from the last line upward to locate the failed condition.

## Stage 3 · Test the boundary

The supplied grader includes positive and negative examples. Predict each result, then run it. Add one additional boundary case in `99-work/06-project/02-extra-check.py`. Use a temporary directory or in-memory database when possible so repeated tests cannot overwrite earlier evidence. Explain why the extra case matters.

## Stage 4 · Compare with a complete reference

Only after attempting your implementation, open [02-solution.py](02-solution.py). It contains a working reference, not an empty skeleton. Verify it independently:

```sh
python3 05-project-labs/06-durable-operations/03-grade.py --solution
```

Expected output:

```text
PASS: 06 durable-operations
```

Compare the order of validation, decision and mutation with your version. Two different implementations may both pass; explain the tradeoffs rather than assuming identical code is required. State which input shapes the exercise assumes and which malformed inputs would need additional validation in a public API.

## Stage 5 · Demonstrate failure, recovery and limitations

Remove one protective check in your scratch implementation. Identify which test fails and why that failure represents a real risk. Restore the check and rerun. Record the final command, result and one production limitation in `99-work/06-project/03-evidence.md`.

This exercise implements one mechanism, not a complete production platform. Explain the identity, concurrency, durability and operational assumptions that remain outside it. The later self-service API project combines several mechanisms into one running HTTP service.

## Completion gate

Your implementation passes the grader; your added boundary case passes; you can explain the mechanism using a concrete request; and your evidence contains an observed failure followed by a successful repair. A copied reference without an explanation does not satisfy the learning gate.

[All projects](../00-PROJECT-MAP.md) · [Course map](../../01-COURSE-MAP.md)
