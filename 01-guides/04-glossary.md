# Glossary

Definitions here are teaching summaries. Consult the primary references for tool-specific semantics.

**Admission.** The decision point that accepts or rejects a requested API change before it is persisted or executed.

**Artifact.** A versioned output such as an image, package or generated configuration.

**Availability.** The fraction of defined eligible events that satisfy the good-event rule over a window.

**Burn rate.** Observed bad-event fraction divided by the allowed bad-event fraction.

**Catalog.** A model of software entities, ownership and relationships.

**Chargeback.** Assigning actual financial charges to consumers according to an allocation policy.

**Control plane.** The system that accepts intent and manages resource lifecycle.

**Data plane.** The workloads or request path that perform application work.

**Declarative configuration.** A description of intended state rather than an ordered sequence of manual actions.

**Developer experience.** How effectively users can understand and complete engineering work, including feedback and recovery.

**Drift.** A difference between desired configuration and observed state.

**Error budget.** The amount of bad behavior tolerated by a defined SLO over a window.

**GitOps.** Declarative, versioned desired state automatically pulled and continuously reconciled by agents.

**Golden path.** A maintained, supported route for a defined developer task.

**Idempotency.** Repeated equivalent requests have the same intended effect as one request within a defined scope.

**Internal developer platform.** A set of capabilities curated to help internal users build, deliver and operate software.

**Least privilege.** Granting only the actions and resource scope required for a task.

**Limit.** A runtime resource bound; behavior depends on the resource and runtime.

**Namespace.** A Kubernetes scope for names and selected policies; not a complete security boundary by itself.

**Observability.** The ability to infer system behavior from available signals and context.

**Policy as code.** Machine-evaluated rules with versioned logic, tests and explainable decisions.

**Portal.** A user interface over platform capabilities; not the entire platform.

**Provenance.** Verifiable information about how an artifact or source revision was produced.

**RPO.** Recovery point objective: tolerable lost data expressed as a time interval.

**RTO.** Recovery time objective: target time to restore the required service.

**Reconciliation.** Repeated comparison and action to reduce differences between desired and observed state.

**Request.** In Kubernetes resource management, the amount used for scheduling/reservation decisions.

**SBOM.** Software bill of materials: an inventory of software components.

**SLI.** Service level indicator: a defined measurement of service behavior.

**SLO.** Service level objective: a target for an SLI over a defined window.

**Showback.** Reporting allocated costs to users without transferring financial charges.

**Tenancy.** The boundaries that separate users or teams in identity, resources, data and operations.

**Toil.** Repetitive operational work that scales with service growth and provides little enduring improvement.

**Workload identity.** An identity assigned to software execution rather than a human user.
