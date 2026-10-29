import shutil
import sys
print('Python:', sys.version.split()[0])
try:
    import sqlite3
    print('SQLite:', sqlite3.sqlite_version)
except ImportError:
    sys.exit('SQLite support is required; install a Python distribution that includes sqlite3')
supported = sys.version_info >= (3, 10)
print('Core interpreter:', 'PASS' if supported else 'FAIL: install Python 3.10+')
for name in ('git', 'docker', 'kind', 'kubectl'):
    location = shutil.which(name)
    print(name + ': ' + ('available' if location else 'not found') + (' (optional cluster track)' if name != 'git' else ' (needed for Git exercises)'))
print('Tool presence does not prove that a runtime is running or a cluster is reachable.')
sys.exit(0 if supported else 1)
