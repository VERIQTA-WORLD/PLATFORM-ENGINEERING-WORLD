# Project 07 · Concurrent Updates

**Level:** advanced implementation. **Time:** 2–4 hours. **Deliverable:** Compare-and-set update with a demonstrated stale-writer conflict. Work from the repository root. Use Python 3.10+ and synthetic data. No cloud account is needed.

## Understand what you are building

Two operators may read revision 1 and both prepare an update. If the second writer blindly overwrites the first, one decision is lost. Optimistic concurrency compares the expected revision at the same time as the write. A prior SELECT followed by an unconditional UPDATE is not enough. Use one conditional update and inspect its affected-row count.

## Stage 1 · Read the interface and see the missing behavior

Open [01-starter.py](01-starter.py). The function is named `update` and takes `connection, name, expected_revision, replicas`. `NotImplementedError` is intentional: this is the place where you supply the behavior. Read [03-grade.py](03-grade.py) before changing code so the examples and failure expectations are concrete.

Run:

```sh
python3 05-project-labs/07-concurrent-updates/03-grade.py
```

Expected: a nonzero exit with NotImplementedError. This is a starting point, not a broken installation. If the file itself cannot be found, correct your current directory before implementing anything.

## Stage 2 · Build the first passing behavior

Set up the table with one row at revision 1. Put both name and revision in the WHERE clause. Increment revision in the same SQL statement as the new value. If no row matched, report a conflict instead of success. A client encountering conflict should reread the resource and reconsider its decision; blindly replacing expected_revision with the newest value defeats the protection.

Create `99-work/07-project` using your editor or file manager, copy `01-starter.py` there as `01-implementation.py`, and edit your copy. Keep the supplied starter so you can repeat the exercise.

```sh
python3 05-project-labs/07-concurrent-updates/03-grade.py --implementation 99-work/07-project/01-implementation.py
```

An AssertionError names a behavior that is still wrong. Fix that behavior rather than removing the assertion. Read stack traces from the last line upward to locate the failed condition.

## Stage 3 · Test the boundary

The supplied grader includes positive and negative examples. Predict each result, then run it. Add one additional boundary case in `99-work/07-project/02-extra-check.py`. Use a temporary directory or in-memory database when possible so repeated tests cannot overwrite earlier evidence. Explain why the extra case matters.

## Stage 4 · Compare with a complete reference

Only after attempting your implementation, open [02-solution.py](02-solution.py). It contains a working reference, not an empty skeleton. Verify it independently:

```sh
python3 05-project-labs/07-concurrent-updates/03-grade.py --solution
```

Expected output:

```text
PASS: 07 concurrent-updates
```

Compare the order of validation, decision and mutation with your version. Two different implementations may both pass; explain the tradeoffs rather than assuming identical code is required. State which input shapes the exercise assumes and which malformed inputs would need additional validation in a public API.

## Stage 5 · Demonstrate failure, recovery and limitations

Remove one protective check in your scratch implementation. Identify which test fails and why that failure represents a real risk. Restore the check and rerun. Record the final command, result and one production limitation in `99-work/07-project/03-evidence.md`.

This exercise implements one mechanism, not a complete production platform. Explain the identity, concurrency, durability and operational assumptions that remain outside it. The later self-service API project combines several mechanisms into one running HTTP service.

## Completion gate

Your implementation passes the grader; your added boundary case passes; you can explain the mechanism using a concrete request; and your evidence contains an observed failure followed by a successful repair. A copied reference without an explanation does not satisfy the learning gate.

[All projects](../00-PROJECT-MAP.md) · [Course map](../../01-COURSE-MAP.md)
