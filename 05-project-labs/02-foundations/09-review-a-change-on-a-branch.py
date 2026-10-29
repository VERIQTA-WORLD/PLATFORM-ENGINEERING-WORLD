import subprocess
from pathlib import Path
root = Path("99-work/08-git-practice")
def git(*args):
    return subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True, text=True).stdout.strip()
git("switch", "-c", "lesson-add-owner")
(root / "01-service.txt").write_text("service=checkout\nowner=commerce\n")
print(git("diff", "--stat"))
print(git("diff", "--", "01-service.txt"))
