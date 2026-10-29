# Platform threat model

## Assets and actors
List protected data, credentials, artifacts and control authority. Include developer, CI, controller, operator and external service identities.

## Boundaries
For every request hop, identify transport, authentication, authorization and audit.

## Threat table
| Threat | Preconditions | Effect | Control | Enforcement point | Negative test | Residual risk |
| --- | --- | --- | --- | --- | --- | --- |
| Cross-tenant request | Define | Define | Define | Define | Define | Define |
| Untrusted artifact | Define | Define | Define | Define | Define | Define |
| Stale or duplicate request | Define | Define | Define | Define | Define | Define |

## Response
Detection, containment, credential rotation, recovery and evidence preservation.

## Review triggers
New tenant class, public exposure, privileged integration, data classification or architecture change.
