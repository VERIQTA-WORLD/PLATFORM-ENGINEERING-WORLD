import subprocess
from pathlib import Path
root = Path("99-work/08-git-practice")
def git(*args):
    return subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True, text=True).stdout.strip()
git("add", "01-service.txt")
git("commit", "-m", "Add service ownership")
print("before", "owner=" in (root / "01-service.txt").read_text())
git("revert", "--no-edit", "HEAD")
print("after", "owner=" in (root / "01-service.txt").read_text())
print(git("log", "-1", "--format=%s"))
