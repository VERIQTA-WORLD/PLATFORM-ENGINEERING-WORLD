# Validation and execution scope

From the repository root run:

```sh
python3 06-tools/05-check-all.py
python3 06-tools/06-foundation-smoke.py
```

The first command loads numbered test modules explicitly and refuses a zero-test result. Ordinary unittest filename discovery can silently skip names with numeric prefixes, so the course does not use that as its entry command. It then audits the course, runs the local lifecycle, verifies all eight project solutions and sends actual HTTP requests to a temporary loopback server.

The foundation smoke test copies the course into a disposable directory and executes all 17 foundation programs, including the dependent Git sequence, HTTP server/client, health endpoint and SQLite exercise. It leaves the public course fixtures unchanged.

## Initial validation of this edition

Executed with Python 3.12.14:

- 23 unit tests passed, including concurrent equivalent request admission, restart/replay, tenant isolation, pending-work quota, stale-write rejection and backup recovery.
- All eight project reference implementations passed their graders.
- The integrated API passed real loopback HTTP checks for success, 401, 403, 404, 409, request replay and repeated reconciliation.
- All 17 foundation programs passed their smoke run.
- The local lifecycle walkthrough and the numbering, link and syntax audit passed.

The learner starters are intentionally incomplete and are not claimed to pass. Passing a reference implementation is evidence about the reference, not a learner submission.

Docker, kind, kubectl and OpenTofu execution were unavailable during this edition's local verification. Their complete lab instructions and configuration are provided, but their runtime results remain unverified. Hosted CI has not been run. The numbered hosting workflow is an example, not an automatically discovered active workflow.

## Limits

The audit checks authored filenames, catalog entries, local Markdown targets, Python/JSON/SVG syntax and common private-content patterns. It does not prove technical correctness of prose, validate every external URL or guarantee absence of sensitive data. Review public changes. Local HTTP and database tests do not establish production security, performance or cloud integration behavior.

If loopback networking is restricted, `python3 06-tools/05-check-all.py --skip-http` runs offline checks and explicitly reports HTTP as unverified. The foundation smoke test also requires loopback access for its HTTP demonstrations.
