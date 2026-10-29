# Project 12 · Infrastructure state with OpenTofu

**Prerequisites:** foundation phases, the local state project and phase 11. **Time:** 90–150 minutes. Install OpenTofu using its [official installation guide](https://opentofu.org/docs/intro/install/). Record `tofu version`. This lab has no cloud provider, credentials or paid resources. Its tool execution is separate from the Python test suite.

## Understand the resource

Open `01-main.tf`. HCL is a configuration language. A variable supplies an input, validation constrains its accepted values, a resource declares managed state, and an output exposes a result. The builtin terraform_data resource participates in the resource lifecycle but does not create a remote server. This is an actual OpenTofu exercise about planning and state, with that boundary made explicit.

Numbered `.tf` filenames are supported because the tool reads configuration files by extension. Its own generated state, lock files and internal directories use tool-required names; those are not authored course files and should not be published as portfolio content.

## Stage 1 · Initialize and read a plan

From the repository root:

```sh
tofu -chdir=05-project-labs/12-infrastructure-state init
tofu -chdir=05-project-labs/12-infrastructure-state validate
tofu -chdir=05-project-labs/12-infrastructure-state plan
```

On fresh state, expect one terraform_data resource to be created. Read the resource address and its input values. An initialized directory is not an applied deployment. If initialization fails, inspect the version and working path before changing resource definitions.

## Stage 2 · Save, inspect and apply

```sh
tofu -chdir=05-project-labs/12-infrastructure-state plan -out=../../99-work/12-reviewed.plan
tofu -chdir=05-project-labs/12-infrastructure-state show ../../99-work/12-reviewed.plan
tofu -chdir=05-project-labs/12-infrastructure-state apply ../../99-work/12-reviewed.plan
tofu -chdir=05-project-labs/12-infrastructure-state output -json
tofu -chdir=05-project-labs/12-infrastructure-state plan
```

Applying a saved plan executes that plan; review it before applying. The output should contain checkout, commerce and replicas 2. The final plan should report no changes. Preserve the observation and the tool version. Do not claim that a container or cloud service exists: the resource stores lifecycle-managed data only.

## Stage 3 · Change and reject inputs

```sh
tofu -chdir=05-project-labs/12-infrastructure-state plan -var=replicas=3
tofu -chdir=05-project-labs/12-infrastructure-state plan -var=replicas=0
```

The first plan proposes an input change. The second must reject before apply because zero violates the contract. Explain why a valid type is weaker than a valid value. Do not apply the invalid request. If you apply replicas 3, a later plan using the default 2 will propose changing it back: inputs are part of the decision and must be recorded.

## Stage 4 · Inspect ownership and clean up

```sh
tofu -chdir=05-project-labs/12-infrastructure-state state list
tofu -chdir=05-project-labs/12-infrastructure-state plan -destroy
tofu -chdir=05-project-labs/12-infrastructure-state destroy
```

Review the destroy plan and approve only the exercise resource when prompted. The state list should become empty. Do not delete state as a substitute for destroying real provider resources; losing the mapping does not necessarily remove external objects.

## Completion gate

Explain configuration versus state, plan versus apply, invalid input versus an ordinary change, and why saved plans require review. Your evidence includes one create, no-change result, rejected request and cleanup. Production backends additionally need access control, locking, encryption where appropriate and recovery procedures.

[OpenTofu builtin resource reference](https://opentofu.org/docs/language/resources/tf-data/) · [State reference](https://opentofu.org/docs/language/state/).
