# Progression from first commands to senior-level platform study

The course uses demonstrated gates rather than assuming that reading a page establishes competence. Study time varies widely. A learner beginning with no technical experience should plan for months of part-time practice, not a weekend. A reasonable planning range is 150–250 hours including exercises and capstone; repeating difficult foundations or adding real cloud integrations can take longer.

## Gate 1 · Computing foundations, phases 00–05

Read commands and paths, create files, explain a running process, write basic Python, use functions and exceptions, parse JSON, make Git commits, run an HTTP server, query SQLite and write negative tests. You can explain a failed command and repair its cause. Complete all 17 foundation programs rather than only running the provided copies.

**Assessment:** demonstrate an HTTP request and a connection failure; make and revert a Git change; write one function and a test that catches a deliberate regression. Keep your code and observations.

## Gate 2 · Platform practitioner, phases 06–13

Explain developer needs and product scope, validate a service contract, locate ownership, package an application, inspect desired versus actual state, design an environment boundary, understand release evidence and build a self-service path. Complete projects 03 and 04 and the local lifecycle. Run the container/cluster project when your environment supports it; otherwise record that runtime work as pending rather than claiming completion.

**Assessment:** show a valid and rejected service request, a plan, an applied state and an empty second plan. Explain who supports the workflow and what remains unsupported.

## Gate 3 · Reliability and trust, phases 14–19

Explain actor/action/resource decisions, supply-chain evidence, tenancy, SLOs, telemetry, backup and restore, data migration, capacity, cost, on-call and compatibility. Complete projects 05, 09 and 10. Write a synthetic incident report and prove a local restore.

**Assessment:** deny a cross-tenant action, calculate a budget, preserve a new value through a repeated migration and reject a corrupted recovery payload. Explain which checks are declaration checks and which are authoritative enforcement.

## Gate 4 · Advanced implementation, phases 20–23

Complete projects 06–08 and the integrated HTTP API. Demonstrate concurrent request replay, stale-write rejection, bounded retries, pending-work quota, process restart and recovery. Design the additional boundary for a remote provider, durable queue, verified identity and telemetry timestamps.

**Assessment:** explain why a database transaction cannot undo an external effect; run the API's negative paths; defend a recovery procedure and migration plan. Show a meaningful extra test or implemented extension.

## Gate 5 · Capstone and architecture defense, phase 24

Choose a capstone. Deliver your own reproducible implementation and evidence. The rubric requires failure and repair, operational ownership, trust boundaries, economics and honest limitations. A passing reference solution does not count as your implementation. Include at least one change that you designed and tested.

**Assessment:** a reviewer follows the entry command from a fresh copy, challenges one assumption and observes one failure and recovery. Label self-review honestly if no peer is available.

## Beyond the course

To build professional seniority, work with experienced engineers on real user discovery, production incidents, migration programs and operational ownership. Use the integration guide to add real GitOps, catalogs, admission policy, telemetry and identity in a sandbox. Preserve the same discipline: explicit promises, authoritative controls, negative tests and measured outcomes.
