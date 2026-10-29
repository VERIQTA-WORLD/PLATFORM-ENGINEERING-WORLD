import subprocess
from pathlib import Path
root = Path("99-work/08-git-practice")
root.mkdir(parents=True, exist_ok=True)
def git(*args):
    return subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True, text=True).stdout.strip()
git("init", "-b", "main")
git("config", "user.name", "Course Learner")
git("config", "user.email", "learner@example.com")
(root / "01-service.txt").write_text("service=checkout\n")
git("add", "01-service.txt")
git("commit", "-m", "Record the first service")
print(git("log", "-1", "--format=%s"))
print("clean", not git("status", "--porcelain"))
