# Troubleshooting

| Problem | Check | Repair |
| --- | --- | --- |
| `python3` is unavailable | Interpreter installation and PATH | Install Python 3.10+ from the official source; Windows can use `py -3` |
| Doctor reports old Python | `python3 --version` | Select the supported interpreter explicitly; do not assume the OS default is current |
| Cannot find `03-reference-platform/01-pe.py` | Current directory | Open the repository root containing 00-INDEX.md |
| Output path parent does not exist | Selected `--out` parent | Create `99-work/` in your editor or file manager |
| Scaffold says directory exists | Existing files | Inspect and keep the existing work; use a fresh directory for a new attempt |
| Restore or backup refuses output | Existing target | Choose a fresh name; refusal preserves earlier evidence |
| Validation exits 1 | JSON output `errors` | Repair the rejected contract fields and retry |
| A command exits 2 | Standard error | Fix unreadable/malformed input, invalid arguments or output collision |
| Plan still reports retained objects | `retain-unmanaged` actions | Expected: the teaching model does not delete resources |
| SLO says no events | Input list and telemetry assumptions | Treat reliability as unknown, not perfect |
| Runtime tools are absent | Doctor output | Continue core lessons or install the optional tools from official guides |
| YAML exists but no service runs | Cluster, context, rollout and ready endpoints | Follow the optional lab and capture actual observations |

When requesting help, include your tool version, command with secrets removed, expected behavior, actual behavior and a minimal synthetic fixture. Do not post real credentials, organization inventory or private logs. A public issue should be reproducible without access to your workplace.
