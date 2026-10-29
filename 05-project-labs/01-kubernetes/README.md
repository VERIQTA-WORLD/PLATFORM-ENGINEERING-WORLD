# Disposable container and Kubernetes lab

This optional lab runs a real HTTP service. The core curriculum works without it. Use a local machine with Python 3.10+, a Docker-compatible Docker CLI/runtime, curl, kind and kubectl. Allow roughly 4 CPU cores, 6 GB free memory and several GB of disk for the learning cluster; requirements vary with your runtime. Initial image downloads require network access. No cloud subscription is used.

Install tools from their official documentation: [Docker](https://docs.docker.com/get-started/get-docker/), [kind](https://kind.sigs.k8s.io/docs/user/quick-start/), [kubectl](https://kubernetes.io/docs/tasks/tools/). Check the current kind support matrix and use compatible runtime and Kubernetes versions. Record `docker version`, `kind version` and `kubectl version --client` in your evidence. The commands below are a walkthrough, not a claim that every host/runtime combination has been tested.

## 1. Read before building

Read `02-app.py`, `01-Dockerfile` and `03-deployment.yaml`. There are no application dependencies. The base image tag is mutable: for a repeatable release, resolve and pin an approved digest and record it. This lab intentionally uses a recognizable version tag for accessibility. The single-threaded HTTP server is a teaching service, not a production server.

From the repository root:

```sh
docker build -f 05-project-labs/01-kubernetes/01-Dockerfile -t pe-hello:local 05-project-labs/01-kubernetes
docker run --detach --name pe-hello-lab --read-only --cap-drop ALL --security-opt no-new-privileges -p 127.0.0.1:18080:8080 pe-hello:local
curl --fail http://127.0.0.1:18080/healthz
curl --fail http://127.0.0.1:18080/
docker inspect --format '{{.Config.User}}' pe-hello-lab
docker logs pe-hello-lab
docker rm --force pe-hello-lab
```

Expected: `{"status": "ok"}`, `{"service": "hello-platform", "version": "1"}` and user `10001:10001`. JSON spacing and log timestamps may vary. If the name already exists, inspect it first; do not remove an unrelated container. If port 18080 is busy, choose another unused loopback port and update curl accordingly.

## 2. Create an isolated learning cluster

The cluster name must be unused. Inspect `kind get clusters` first. All commands below explicitly target this cluster so an unrelated active kubectl context is not used.

```sh
kind create cluster --name pe-learning --wait 120s
kind load docker-image pe-hello:local --name pe-learning
kubectl --context kind-pe-learning apply -f 05-project-labs/01-kubernetes/04-namespace.yaml
kubectl --context kind-pe-learning apply -f 05-project-labs/01-kubernetes/03-deployment.yaml
kubectl --context kind-pe-learning -n pe-learning rollout status deployment/hello-platform --timeout=120s
kubectl --context kind-pe-learning -n pe-learning get pods
kubectl --context kind-pe-learning -n pe-learning get endpointslices
kubectl --context kind-pe-learning -n pe-learning port-forward --address 127.0.0.1 service/hello-platform 18080:8080
```

Leave port-forward running and use a second terminal for curl. Stop it with Ctrl-C when finished. A successful response proves one request through the forwarded Service; it does not prove external ingress, TLS, tenancy or high availability.

## 3. Introduce drift and repair it

```sh
kubectl --context kind-pe-learning -n pe-learning scale deployment/hello-platform --replicas=1
kubectl --context kind-pe-learning -n pe-learning get deployment hello-platform
kubectl --context kind-pe-learning apply -f 05-project-labs/01-kubernetes/03-deployment.yaml
kubectl --context kind-pe-learning -n pe-learning rollout status deployment/hello-platform --timeout=120s
kubectl --context kind-pe-learning -n pe-learning get deployment hello-platform
```

Expected final desired replicas: 2. This is manual reapplication, not an installed GitOps controller. Copy the manifest into your `99-work/` directory, change only the readiness path to `/missing`, apply the copy, and inspect Pod readiness and events. The old healthy ReplicaSet may remain available during the failed rollout. Inspect individual Pods rather than assuming the entire Service must go down. Repair by reapplying the original manifest.

## 4. Diagnose by symptom

| Symptom | First observation | Likely repair |
| --- | --- | --- |
| ImagePullBackOff or ErrImageNeverPull | `describe pod` events; check the image name and loaded images | Build and load the matching image into this named kind cluster |
| Pending | Pod events, node allocatable resources | Free local resources or adjust the lab requests with an explanation |
| Running but not ready | Probe events and `/healthz` path | Restore the documented probe path |
| Port-forward refuses connection | Command output, chosen local port, Service endpoints | Use a free port and verify at least one ready backend |
| Restricted policy rejection | Admission response and securityContext | Restore the non-root, seccomp and capability settings |

Use `kubectl --context kind-pe-learning -n pe-learning describe pod POD_NAME` and `kubectl --context kind-pe-learning -n pe-learning get events --sort-by=.metadata.creationTimestamp`, replacing `POD_NAME` with an observed name.

## 5. Clean up and report

Stop port-forward, then remove only the named disposable cluster:

```sh
kind delete cluster --name pe-learning
kind get clusters
```

Record versions, image ID, rollout observation, failure, repair and cleanup. If you could not run the lab, record the blocking dependency and leave execution unverified. Do not infer a successful rollout from manifest inspection.
