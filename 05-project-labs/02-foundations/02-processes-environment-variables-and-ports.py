import os
import subprocess
import sys
child_env = dict(os.environ)
child_env["PEW_SERVICE"] = "checkout"
result = subprocess.run(
    [sys.executable, "-c", "import os; print(os.environ['PEW_SERVICE'])"],
    env=child_env, capture_output=True, text=True, check=False)
print(result.stdout.strip())
print("exit", result.returncode)
print("parent changed", "PEW_SERVICE" in os.environ)
