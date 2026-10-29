# Worked example: an asynchronous creation API

This is a design contract, not an API implemented by `pe.py`.

## Request and acceptance

`POST /services` accepts a versioned service contract and an `Idempotency-Key` header. Authenticate the caller before accepting work. Authorize the caller for the requested tenant and service class. Normalize the request, then bind the idempotency key to caller, operation type and normalized request hash.

A new accepted request returns 202, a stable operation ID and `Location: /operations/op-example-001`. A repeated equivalent request with the same scoped key returns the existing operation. Reusing the key for different content returns 409. Invalid fields return 422 with field-level remediation. Unauthenticated requests return 401; authenticated but unauthorized requests return 403. Quota rejection returns a documented conflict with the relevant limit and support route.

## Persistence and execution

In one durable transaction, save the operation and an outbox event. A dispatcher publishes pending outbox events to the worker queue. This prevents accepted operations being lost between database commit and queue submission. Workers may receive duplicates; resource creation uses the operation ID as an external idempotency reference. Before retrying after an uncertain provider response, query by that reference and adopt the existing resource when appropriate.

The request record includes the actor, tenant, normalized intent, policy revision and correlation ID. Do not store access tokens or secret values. Store only authorized metadata and references needed for execution and audit.

## State transitions

| State | Allowed next state | User interpretation |
| --- | --- | --- |
| requested | validating, cancelling | Request accepted; work not yet authorized for execution |
| validating | provisioning, failed, cancelling | Contract and policy checks are in progress |
| provisioning | ready, failed, cancelling | Resources are being prepared and checked |
| cancelling | cancelled, failed | Stop requested; cleanup may still be in progress |
| ready | terminal for this operation | Promised readiness observation succeeded |
| failed | terminal for this operation | A specific attempt ended; retry policy is explained |
| cancelled | terminal for this operation | Cancellation and promised cleanup are verified |

A new operation handles retry after a permanent terminal failure, or the system explicitly supports a bounded retry endpoint. Do not silently change a terminal result after a client has relied on it.

## Failure example

A provider creates a namespace, then the controller crashes before recording success. The next worker checks the operation reference, finds the existing namespace and resumes. If it cannot establish ownership, it fails safely and asks an operator to investigate. It does not delete an unknown namespace or create another with a random suffix.

## Acceptance tests for an implementation

Test two simultaneous equivalent requests, conflicting key reuse, cross-tenant access, crash after provider success, queue redelivery, quota denial and cancellation during provisioning. Verify the response and remaining resources. The local scaffold collision test covers only a small related behavior; it does not establish these distributed-system guarantees.
