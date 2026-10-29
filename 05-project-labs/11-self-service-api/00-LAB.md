# Project 11 · Build and operate a self-service API

**Prerequisites:** foundation phases 00–05 and projects 03–10. **Time:** 6–10 hours including implementation review and failure drills. You will run an actual HTTP server with persistent SQLite state, not merely draw an architecture. It binds only to your own computer. No cloud resources are created.

## What this platform promises

A developer may request one of up to three fictional service registrations in their tenant. Requests accept 1–4 replicas. A durable operation begins as requested. An operator reconciliation creates a registry entry and marks it ready. Here ready means the local registry entry exists; this API does not deploy an application or establish runtime health. The container lab separately runs an actual workload.

Fictional demo identities are public learning inputs: commerce, search and operator. They are mapped to scoped roles by the server. They are not real account credentials. A production version would need verified identity, TLS, secret handling, audit and a provider adapter.

## Stage 1 · Start with fresh state

Open two terminal windows in the repository root. In terminal A run:

```sh
python3 05-project-labs/11-self-service-api/01-server.py --db 99-work/11-api/01-state.sqlite
```

The program creates the numbered data directory if necessary. Expected: `Teaching API: http://127.0.0.1:18083`. It keeps running. If the port is busy, stop the earlier course server or choose another port using `--port`; pass the same port to every client command. Do not start over by deleting a database whose contents you have not inspected.

## Stage 2 · Observe reachability and identity

In terminal B:

```sh
python3 05-project-labs/11-self-service-api/03-client.py GET /healthz
python3 05-project-labs/11-self-service-api/03-client.py GET /services --identity invalid
python3 05-project-labs/11-self-service-api/03-client.py GET /services
```

Expected statuses: 200 with status ok; 401 with an identity explanation; 200 with an empty services list on a fresh database. The client returns exit 1 for an HTTP rejection. The first success proves reachability, while the second checks that a protected route rejects an unknown identity.

## Stage 3 · Submit and replay a request

```sh
python3 05-project-labs/11-self-service-api/03-client.py POST /services --body-file 04-fixtures/06-api-create.json --key create-checkout
python3 05-project-labs/11-self-service-api/03-client.py POST /services --body-file 04-fixtures/06-api-create.json --key create-checkout
```

Both return 202 and the same operation ID. The ID itself varies; copy it into your evidence. Read the state: it is requested, not ready. The same scoped key and same normalized request returns the existing operation. Reordering JSON fields does not create new work.

Now change the request while retaining the key:

```sh
python3 05-project-labs/11-self-service-api/03-client.py POST /services --body-file 04-fixtures/07-api-conflict.json --key create-checkout
```

Expect 409. Reusing a key must not silently alter already accepted work. A new key requesting the same name is also rejected in this deliberately narrow creation workflow.

## Stage 4 · Check tenant isolation

Use the copied operation ID in the path `/operations/YOUR_OPERATION_ID`, replacing the entire placeholder with the observed ID. Read it with commerce and then search:

```sh
python3 05-project-labs/11-self-service-api/03-client.py GET /operations/YOUR_OPERATION_ID
python3 05-project-labs/11-self-service-api/03-client.py GET /operations/YOUR_OPERATION_ID --identity search
```

Expect 200 and 404 respectively. The query includes tenant in the database lookup. A client cannot select a different tenant by adding a tenant field to its request; conflicting tenant claims are rejected.

## Stage 5 · Reconcile through the operator boundary

```sh
python3 05-project-labs/11-self-service-api/03-client.py POST /reconcile
python3 05-project-labs/11-self-service-api/03-client.py POST /reconcile --identity operator
python3 05-project-labs/11-self-service-api/03-client.py POST /reconcile --identity operator
python3 05-project-labs/11-self-service-api/03-client.py GET /services
```

Expect 403; then 200 with reconciled 1; then 200 with reconciled 0; then a checkout record with replicas 2 and revision 1. The database transaction stores both the registry entry and ready state. Repeated reconciliation does not duplicate the entry. This command-driven worker is not a continuously running GitOps controller.

## Stage 6 · Reject a stale write

```sh
python3 05-project-labs/11-self-service-api/03-client.py PUT /services/checkout --body-file 04-fixtures/08-api-update.json
python3 05-project-labs/11-self-service-api/03-client.py PUT /services/checkout --body-file 04-fixtures/08-api-update.json
python3 05-project-labs/11-self-service-api/03-client.py GET /services
```

Expect 200 with revision 2; then 409; then replicas 3 at revision 2. The second request still expects revision 1. The conditional UPDATE performs the version comparison and write together. On conflict, reread and reconsider intent rather than automatically forcing the new revision.

## Stage 7 · Restart and recover

Stop terminal A with Ctrl-C. Restart it with the same database path. Repeat the original POST with create-checkout. It returns the same operation ID, proving request history survived process restart. Stop the server before the recovery exercise for a simple, controlled scenario.

```sh
python3 05-project-labs/11-self-service-api/01-server.py --db 99-work/11-api/01-state.sqlite --backup-to 99-work/11-api/02-backup.sqlite
python3 05-project-labs/11-self-service-api/01-server.py --db 99-work/11-api/02-backup.sqlite
```

The first command creates a consistent SQLite snapshot and checks database integrity. It refuses an existing backup target. The second serves that backup as a separate exercise copy. GET /services and replay the original key: both service state and operation identity should be preserved. Keep the original database. This is a local recovery demonstration, not a measured regional RTO/RPO.

## Stage 8 · Read the complete implementation

Trace `Store.submit`: validation → write transaction → key lookup → quota check → insert → commit. Trace `Store.update`: a single conditional UPDATE. Trace handler authorization before operator or tenant actions. Identify where a remote provider adapter would introduce a new partial-failure boundary outside the SQLite transaction.

Implement one additional feature in a scratch copy: an explicit failed-operation state with a safe retry rule, a versioned request contract, or an owned deletion operation. Add positive, negative and recovery tests. Do not label a registry entry runtime-ready without implementing and observing a real provider.

## Stage 9 · Verify and clean up

```sh
python3 05-project-labs/11-self-service-api/02-http-smoke.py
```

This starts its own temporary server on an available loopback port, checks actual HTTP behavior and cleans up its temporary data. Stop any manually started server with Ctrl-C. Keep or remove only your numbered exercise files after reviewing them. Record the happy path, rejection, replay, stale update, restart and recovery in `99-work/11-api/03-evidence.md`.

**Completion:** you can explain why 202 differs from ready, why identity is derived from the authenticated actor, why a database constraint matters under concurrency, and what a transaction cannot undo in an external provider.
