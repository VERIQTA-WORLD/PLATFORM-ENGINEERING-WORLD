import subprocess
import sys
commands = [
    [sys.executable, "06-tools/01-audit.py"],
    [sys.executable, "06-tools/04-walkthrough.py"],
]
for command in commands:
    print("RUN", " ".join(command), flush=True)
    subprocess.run(command, check=True)
print("required local checks passed")
