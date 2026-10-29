# Recovery exercise plan and report

## Service and scenario
Name the fictional workload, outage scope and required user outcome.

## Objectives
RPO, RTO, data assumptions, consistency requirements and acceptable degraded operation.

## Dependencies and authority
Backup locations, tooling, keys, identities, DNS and external dependencies. Specify how to recover them if the main control plane is unavailable.

## Procedure
Number the restore steps. Include fencing old writers, restoring data, reconciling configuration, verifying application behavior and switching traffic.

## Abort and rollback
Define stop conditions, escalation and treatment of partially restored state.

## Evidence
Record start/end times, restored point, validation result and whether objectives were met. Distinguish local measurement from production expectations.

## Cleanup and improvement
Remove only exercise resources. Record gaps, owners and the next test date or trigger.
