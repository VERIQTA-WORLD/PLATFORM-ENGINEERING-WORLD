# Worked example: tenant boundary and recovery

This example describes a fictional service class. It is a design, not an executed isolation or failover test.

## Standard tenant

Each team receives a namespace, a scoped deployment identity, a quota and a catalog owner. Workloads run non-root with restricted security settings. An enforcing network implementation and tested policies restrict ingress and egress. The namespace has a CPU budget, memory budget and storage limit. Users cannot create privileged Pods, cluster-wide bindings or arbitrary service accounts.

Ten teams requesting two replicas at 500m CPU each reserve 10 CPU cores before system workloads, headroom and other resources. A cluster with exactly 10 allocatable CPU cores does not satisfy a node-loss requirement. Model the largest node loss, system overhead and expected burst before choosing capacity. Memory and storage may become limiting first.

## Restricted tenant

Sensitive data or mutually untrusted workloads may require a separate cluster or account. Namespace policy cannot eliminate all shared-node or control-plane risks. The stronger boundary increases management, upgrade and capacity cost. Require a documented threat and operating requirement before selecting it.

## Recovery scenario

A fictional regional database outage interrupts checkout. The design target is an RPO of 15 minutes and RTO of 60 minutes, contingent on supported replication and backups. These are targets to test, not demonstrated results.

Recovery order: declare the incident; prevent writes to the old primary using the database's supported fencing mechanism; inspect the latest recoverable point; restore or promote through the supported database procedure; validate schema and credentials; reconcile application configuration; execute a synthetic checkout transaction; then shift traffic and monitor data correctness and replication.

Do not shift DNS while both regions can independently accept writes. DNS propagation does not revoke existing connections or credentials. If fencing cannot be verified, escalate rather than claiming single-writer safety.

## Verification

Measure actual elapsed recovery and the newest recovered transaction. Compare both with RTO/RPO. Verify a user transaction, background jobs, queue replay and external side effects. Record any data reconciliation needed. A healthy database process or matching backup checksum alone does not prove application recovery.

A real exercise must capture commands, observations and versions. Until that happens, the objectives remain unverified assumptions. The course's local backup/restore demonstrates byte integrity and collision handling only.
