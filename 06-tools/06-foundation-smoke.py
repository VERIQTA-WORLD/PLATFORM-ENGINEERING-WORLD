"""Execute all 17 foundation reference programs in a disposable course copy."""
from pathlib import Path
import os
import shutil
import subprocess
import sys
import tempfile
from urllib.request import urlopen
ROOT=Path(__file__).resolve().parents[1]
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
with tempfile.TemporaryDirectory() as directory:
    course=Path(directory)/'01-course'
    shutil.copytree(ROOT,course,ignore=shutil.ignore_patterns('.git','__pycache__','99-work'))
    (course/'99-work').mkdir()
    programs=sorted((course/'05-project-labs/02-foundations').glob('*.py'))
    def run(program):
        result=subprocess.run([sys.executable,str(program)],cwd=course,env=env,text=True,capture_output=True,timeout=20)
        if result.returncode:raise RuntimeError(program.name+'\n'+result.stdout+result.stderr)
        return result.stdout
    for program in programs:
        number=int(program.name[:2])
        if number in (11,14):
            server=subprocess.Popen([sys.executable,str(program)],cwd=course,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            try:
                line=server.stdout.readline()
                if not line:raise RuntimeError('server did not start: '+server.stderr.read())
                if number==11:
                    client=programs[11]
                    output=run(client)
                    if 'hello platform' not in output:raise RuntimeError('HTTP client received wrong body')
                else:
                    with urlopen('http://127.0.0.1:18082/healthz',timeout=3) as response:
                        if response.status!=200:raise RuntimeError('health endpoint failed')
            finally:
                server.terminate()
                try:server.communicate(timeout=3)
                except subprocess.TimeoutExpired:server.kill();server.communicate()
        elif number==12:continue # Executed while the prior server was alive.
        else:run(program)
print('PASS: all 17 foundation programs, Git sequence, HTTP server/client, health endpoint and SQLite')
