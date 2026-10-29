# Advanced integration projects

These are extension specifications with acceptance checks, not preinstalled integrations. Complete the local course first. Install a chosen tool using its official documentation, record its version, and run against your own disposable environment. Keep an integration’s resources under one clear owner.

## 1. GitOps with a real controller

Choose [Flux](https://fluxcd.io/flux/get-started/) or [Argo CD](https://argo-cd.readthedocs.io/en/stable/getting_started/). Install the controller in a disposable cluster following the current official guide. Store the learning Deployment in a repository you control. Restrict the controller’s source and destination to the learning scope. Make a reviewed commit changing replicas, wait for reconciliation and observe the runtime.

Then scale the Deployment manually and observe whether the configured reconciliation/self-heal behavior repairs drift. Record the configured interval or trigger. Revert a source change and verify the new runtime state. Temporarily break source access and inspect status without deleting healthy workloads.

Acceptance: source revision and observed deployment are linked; drift behavior is demonstrated rather than assumed; a source outage is visible; credentials are scoped; cleanup removes controller resources and revokes its access. Explain why the local `pe.py` loop is not this integration.

## 2. Backstage catalog and template

Use [Backstage’s getting started guide](https://backstage.io/docs/getting-started/) for a disposable instance. Translate a fictional service to a Component entity, including owner and lifecycle. Register it from a repository you control and confirm the resolved owner relationship. Create a small software template that validates user input and generates a service contract. Use a test repository destination and scoped credentials.

Introduce an invalid owner reference and observe the catalog’s response. Describe ingestion delay and source ownership. Add an operation status or link that tells a user whether creation completed; successful template rendering alone is not runtime readiness.

Acceptance: the entity can be discovered, ownership resolves, a generated repository contains the expected files and failure feedback is actionable. Document authentication/permission gaps in a local development instance before suggesting organizational use.

## 3. Policy enforcement in Kubernetes

Choose native [ValidatingAdmissionPolicy](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/) where supported by your cluster, or a policy engine such as [Kyverno](https://kyverno.io/docs/). Define a narrow invariant for the learning namespace, such as mandatory ownership labels. First test in audit mode if available, inspect violations, then enforce only in the disposable scope.

Submit an allowed manifest and a denied manifest using the same authenticated actor. Show that a direct kubectl request cannot bypass the authoritative rule. Add a narrowly scoped exception design and discuss its expiry and audit needs.

Acceptance: allowed and denied requests have captured admission results; scope excludes unrelated namespaces; rule rollback is documented; metadata checks are not misrepresented as complete runtime security. Verify current API availability before writing manifests.

## 4. OpenTofu local resource module

Use [OpenTofu](https://opentofu.org/docs/intro/) and a provider suitable for local files. Pin a compatible provider version, review the provider source and commit the dependency lock file. Build a module that renders a synthetic service configuration with name and owner inputs. Run format, validate and plan; inspect the file paths before apply.

Change an input and inspect the next plan. Compare manual file changes with the provider’s refresh behavior. Destroy only the local resources created by the exercise. Explain backend locking and state sensitivity even though this module uses no cloud.

Acceptance: the learner records exact versions, a reviewed plan, observed output, an update and cleanup. Test invalid inputs and keep provider state out of the public portfolio. Do not imply that a local-file provider validates cloud architecture.

## 5. OpenTelemetry and a real user journey

Follow [OpenTelemetry’s language-specific instrumentation guides](https://opentelemetry.io/docs/languages/) for your chosen service language. Instrument request latency, errors and a correlation trace. Use a local collector/exporter configuration from official examples and inspect its output before adding a hosted backend.

Generate successful, slow and failed synthetic requests. Define the SLI from those observations and compare it with the fixture calculator. Remove one telemetry signal deliberately and observe data freshness. Audit label cardinality and emitted attributes for sensitive material.

Acceptance: an observed request maps to a trace and metric/log evidence; missing data is distinct from healthy behavior; units and boundaries match the SLO definition; collector and backend cleanup are recorded.

## 6. Workload identity and artifact trust

This project requires a sandbox identity system you control. Use the current official documentation for your CI provider, identity provider, registry and verification tool. Write the trust policy first: permitted issuer, audience, repository, revision context and deployment environment. Design separate build and deployment roles.

Build an artifact, generate provenance with a trusted builder, verify the subject digest and expected claims, and deploy the verified digest. Run a negative test using a wrong source context or untrusted signer. Use short-lived identities where supported and preserve verification results without exporting tokens.

Acceptance: the legitimate path works and an invalid identity or provenance is rejected at the point of effect. A signature file existing in a directory does not satisfy this requirement. State which trust root and enforcement component made the decision.

## Review every extension

Attach a version inventory, happy path, negative path, recovery, cleanup and honest limitations. An integration that is only designed must remain labeled as a design. [Capstone B](02-capstones.md#capstone-b-multi-tenant-platform-control-plane) provides a broader assessment rubric.
