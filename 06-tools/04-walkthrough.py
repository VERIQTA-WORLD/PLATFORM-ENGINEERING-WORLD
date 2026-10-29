"""Exercise the public quickstart in a fresh temporary directory."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
ROOT = Path(__file__).resolve().parents[1]
def run(*args, expected=0):
    result = subprocess.run([sys.executable, str(ROOT/'03-reference-platform/01-pe.py'), *map(str,args)], cwd=ROOT, text=True, capture_output=True)
    if result.returncode != expected:
        raise RuntimeError(result.stderr or result.stdout)
    return result.stdout
with tempfile.TemporaryDirectory() as directory:
    d = Path(directory)
    run('validate','04-fixtures/02-desired.json')
    run('validate','04-fixtures/04-invalid.json',expected=1)
    assert json.loads(run('plan','04-fixtures/02-desired.json','04-fixtures/01-actual.json')) == [{'action':'update','name':'checkout'}]
    run('apply','04-fixtures/02-desired.json','04-fixtures/01-actual.json','--out',d/'state.json')
    assert json.loads(run('plan','04-fixtures/02-desired.json',d/'state.json')) == []
    run('scaffold','inventory','--owner','commerce','--out',d/'inventory')
    run('validate',d/'inventory/01-service.json')
    assert json.loads(run('slo','04-fixtures/03-events.json'))['burn_rate'] == 3
    assert json.loads(run('cost','04-fixtures/05-usage.json'))['commerce'] == 2.88
    run('backup',d/'state.json','--out',d/'backup.json')
    run('restore',d/'backup.json','--out',d/'restored.json')
    assert (d/'restored.json').read_bytes() == (d/'state.json').read_bytes()
print('PASS: validation, rejection, plan, apply, convergence, scaffold, SLO, cost, backup and restore')
