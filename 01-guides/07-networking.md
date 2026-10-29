# Networking diagnostic worksheet

Diagnose one boundary at a time. Use only endpoints you own or the local lab. A failed request is an observation; “the network is down” is a hypothesis.

| Observation | Boundary | Next useful check |
| --- | --- | --- |
| Name does not resolve | DNS | Requested name, resolver and search domain |
| Connection refused | Transport/listener | Address, port and whether a process is listening |
| Connection times out | Routing/filtering or stalled peer | Route, policy, dependency health and server-side observation |
| Certificate name mismatch | TLS identity | Requested hostname and certificate names |
| 401 | Authentication | Whether an accepted identity was presented; do not print the token |
| 403 | Authorization | Actor, action, resource and policy decision |
| 503 | Backend availability or overload | Ready endpoints, queue/capacity and dependency state |
| 200 with wrong result | Application correctness | Contract, input, data and application trace |

For Kubernetes, inspect Pod readiness, Service selectors and EndpointSlices. A Service with no ready backends can exist and resolve in DNS. Confirm labels match before changing ingress. Port-forward bypasses parts of an external ingress path, so success through port-forward does not prove TLS or public routing.

Create your own request sequence using fictional identities and `example.com` names. Mark TLS termination, caller authentication, authorization, network policy and the data access boundary. For each hop, state the evidence available to the developer and to the operator.
