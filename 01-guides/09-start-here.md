# Start here

Your goal is a small working loop you can explain: inspect a contract, reject a bad request, plan a change, apply it, prove convergence and recover the data. Allow 45–60 minutes. You need Python 3.10+ and a terminal. Git is needed for the Git exercise, but no package installation, cloud credentials or Kubernetes cluster is needed for this walkthrough.

## 1. Open the repository root

Download the repository from its hosting page or clone its published URL. Open the folder containing `00-INDEX.md`, `03-reference-platform/` and `06-tools/`. Avoid running commands from inside `03-reference-platform/` because examples use paths relative to the repository root.

```sh
python3 06-tools/03-doctor.py
python3 06-tools/01-audit.py
python3 06-tools/05-check-all.py --unit-only
```

Use `py -3` instead of `python3` on Windows if appropriate. Use your file manager or editor to create a directory named `work`. The repository ignores this directory because learning outputs may contain machine-specific evidence.

## 2. Read the service contract

Open `04-fixtures/02-desired.json`. The service is called `checkout`, owned by the fictional commerce team, and requests two replicas. Read `04-fixtures/01-actual.json`: it models only one replica. These are local teaching catalogs, not observations of a running cluster.

```sh
python3 03-reference-platform/01-pe.py validate 04-fixtures/02-desired.json
python3 03-reference-platform/01-pe.py validate 04-fixtures/04-invalid.json
```

The first command prints `"valid": true` and exits 0. The second prints `"valid": false`, reports a missing owner and unauthenticated public exposure, and exits 1. Rejection is expected here. Malformed input or an inaccessible file exits 2.

## 3. Review and apply a change

```sh
python3 03-reference-platform/01-pe.py plan 04-fixtures/02-desired.json 04-fixtures/01-actual.json
python3 03-reference-platform/01-pe.py apply 04-fixtures/02-desired.json 04-fixtures/01-actual.json --out 99-work/01-applied.json
python3 03-reference-platform/01-pe.py plan 04-fixtures/02-desired.json 99-work/01-applied.json
```

The first plan contains `{"action": "update", "name": "checkout"}`. The final plan is `[]`, demonstrating convergence for the supplied desired services. Apply writes a JSON output file, and can overwrite that file. Inspect the chosen output path first. Resources absent from desired state are retained and reported as `retain-unmanaged`; this model has no deletion command.

## 4. Create another service contract

```sh
python3 03-reference-platform/01-pe.py scaffold inventory --owner commerce --out 99-work/01-inventory
python3 03-reference-platform/01-pe.py validate 99-work/01-inventory/01-service.json
```

Inspect the generated `01-service.json` and `01-docs/01-runbook.md`. A second scaffold to the same directory fails intentionally. The command creates files only: there is no running inventory service.

## 5. Make an operational decision

```sh
python3 03-reference-platform/01-pe.py slo 04-fixtures/03-events.json --target .99
python3 03-reference-platform/01-pe.py cost 04-fixtures/05-usage.json
```

Expected SLO: 100 total, 97 good, 3 bad, 0.97 availability, 1 allowed bad event, -2 remaining budget and 3x burn rate. The good-event rule is status below 500 and latency at most 300 ms. Expected fixture costs: commerce 2.88 and search 4.80. The fixture uses illustrative rates without a specified currency; it is not a cloud price quotation. Choose and label a currency for your own cost worksheet.

## 6. Prove recovery

```sh
python3 03-reference-platform/01-pe.py backup 99-work/01-applied.json --out 99-work/01-backup.json
python3 03-reference-platform/01-pe.py restore 99-work/01-backup.json --out 99-work/01-restored.json
python3 06-tools/02-compare.py 99-work/01-applied.json 99-work/01-restored.json
```

Expected comparison: `MATCH`. Backup and restore refuse existing output files. If rerunning, choose fresh output names. The backup envelope is plaintext with a checksum; use synthetic data only. It does not supply encryption or authenticity.

## 7. Keep the evidence and continue

Write `99-work/01-first-loop.md`: input, prediction, command, result, interpretation and limits. Include the rejected request. Record which steps you ran. To recheck the same lifecycle automatically in a fresh temporary directory, run `python3 06-tools/04-walkthrough.py`.

Continue to [first beginner lesson](../02-lessons/00-starting-from-zero/01-what-a-platform-engineer-actually-does.md), [choose a focused route](06-learning-paths.md), or open the [optional Kubernetes lab](../05-project-labs/01-kubernetes/00-INDEX.md). If a command fails, use [troubleshooting](11-troubleshooting.md) and keep the error as evidence.
