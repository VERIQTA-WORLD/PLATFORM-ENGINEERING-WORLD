# Capstones and assessment

Choose one project and publish a sanitized, reproducible portfolio. Use synthetic teams and service names. Allow 12–20 hours for A, 20–40 for B, or 12–20 for C. Estimates exclude learning prerequisites and tooling setup. These projects are assessed through artifacts and behavior; they do not award an accredited certification.

## Capstone A: supported service path

**User:** a fictional application team needs a standard internal HTTP service. **Outcome:** one documented path from a request to a healthy local service or clearly labeled local state simulation, with failure and recovery.

1. Write a product brief identifying the task, eligible users, scope, support route and success measure.
2. Create a service contract through scaffolding. Validate it and explain the policy errors for a bad request.
3. Plan and apply a replica update. Show that a second plan is empty. Introduce drift and repair it.
4. If you can run the optional kind lab, deploy the HTTP service, capture a response and diagnose a readiness failure. Otherwise, label runtime deployment unverified and demonstrate the core simulator only.
5. Calculate the fixture SLO and cost allocation; explain the simplifying assumptions.
6. Back up and restore state, verify equality, then reject a corrupted backup.
7. Implement one extension: contract versioning, revision-guarded writes, or explicit authorized deletion. Test success and failure behavior. A prose proposal alone does not satisfy this implementation requirement.
8. Write a maintenance guide explaining supported inputs, upgrades and known failure modes. Record versions and commands.

**Reference reasoning:** a valid request and an empty plan prove contract acceptance and modeled convergence. They do not prove runtime health. The best submission keeps those claims separate and adds a real request observation if it ran the cluster lab. An extension should close one precise gap rather than adding a dashboard over unchanged behavior.

## Capstone B: multi-tenant platform control plane

**User:** several fictional teams need isolated self-service environments. **Outcome:** a design plus a working local prototype of at least one authoritative control.

Start with A’s contract and add a tenant identifier. Implement a policy that binds a caller’s allowed tenant to the target service, or a revision guard that rejects stale state. Use synthetic identities. Include tests for cross-tenant denial or concurrent conflicting writes. Explain why your prototype is not a complete identity system.

Design the remaining system: asynchronous operation API, persistence, reconciliation, quotas, network boundary, workload identity, release provenance and recovery order. Include a state machine with retries and cancellation. Identify partial failure when a provider creates a resource but the controller loses its response. Design idempotent lookup or adoption rather than blindly creating again.

Add a load-test plan, resource budget and incident tabletop. Demonstrate one failure and recovery in the prototype. Document which controls remain designs and which are running. Optional Kubernetes policy work should use the named disposable cluster and verify enforcement rather than only applying YAML.

**Reference reasoning:** tenancy must be enforced at the point of effect, not only by filtering portal results. Durable operation identity and revision checking prevent classes of duplicate and lost-update problems. Stronger tenant threats may justify separate accounts or clusters.

## Capstone C: platform product and migration strategy

**User:** a fictional engineering organization has multiple delivery paths and limited platform staffing. **Outcome:** an evidence-based platform investment and adoption proposal.

Use five simulated developer journeys with labeled synthetic data. Choose an MVP with a measurable user outcome. Compare maintaining existing paths, building a narrow supported path and adopting an external platform. Describe cost categories without inventing vendor prices. Include opportunity cost, integration, upgrades, on-call and exit costs.

Build the local quickstart and attach your own command evidence so the proposal is grounded in behavior. Produce a six-month adoption plan: pilot selection, eligible team counts, migration cohorts, exception process, compatibility window, support staffing and retirement criteria. Include a threat model, recovery tabletop and a decision record with triggers for revisiting the recommendation.

**Reference reasoning:** adoption is a product outcome with a denominator. A platform that speeds one task while increasing support queues can move work rather than remove it. Evaluate end-to-end task completion and operator load together.

## Scoring rubric

Score each dimension 0–3: 0 absent, 1 asserted, 2 demonstrated with some gaps, 3 reproducible with limits and failure evidence. Six dimensions produce a maximum of 18. A local pass requires at least 14 and no zero. This rubric is an educational convention, not a claim of industry accreditation.

| Dimension | Evidence for 3 |
| --- | --- |
| User outcome | Named user task, scope, baseline and observable acceptance |
| Technical correctness | Reproducible commands or prototype plus tests for the chosen implemented behavior |
| Failure handling | Deliberate rejection/failure, preserved state explained, repair demonstrated |
| Trust and operations | Enforcement boundaries, support ownership, telemetry and recovery procedure |
| Decisions and economics | Alternatives, assumptions, cost model and revisit triggers |
| Public portfolio quality | Clear navigation, original/sourced material, synthetic data, honest execution scope |

**Mandatory gates:** no credentials or private data; no fabricated execution results; a reproducible core walkthrough; a demonstrated failure and repair; source attribution. A cannot pass without the implemented extension. B cannot pass without a working authoritative control and its negative test. C cannot pass without executed local evidence and an adoption plan.

## Review protocol

Give the reviewer a fresh checkout and the exact entry command. Ask them to run the documented path, inspect one error and challenge one design assumption. Record their findings and your repair. If you review your own submission, say so; do not invent an external review. Keep a short limitations section with unfinished integrations and unsupported scenarios.
