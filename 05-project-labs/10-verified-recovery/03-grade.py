"""Grade either the learner implementation or the instructor solution."""
import argparse
import importlib.util
from pathlib import Path
parser=argparse.ArgumentParser()
parser.add_argument('--solution',action='store_true')
parser.add_argument('--implementation',type=Path)
args=parser.parse_args()
path=args.implementation or Path(__file__).with_name('02-solution.py' if args.solution else '01-starter.py')
spec=importlib.util.spec_from_file_location('learner',path)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
import tempfile,hashlib,json
from pathlib import Path
body=json.dumps({"services":[]}); envelope={"payload":body,"sha256":hashlib.sha256(body.encode()).hexdigest()}
with tempfile.TemporaryDirectory() as d:
    target=Path(d)/"01-restored.json"; module.restore(envelope,target)
    assert target.read_text()==body
    try: module.restore(envelope,target)
    except FileExistsError: pass
    else: raise AssertionError("existing file overwritten")
    bad=dict(envelope,payload=body+" "); other=Path(d)/"02-bad.json"
    try: module.restore(bad,other)
    except ValueError: pass
    else: raise AssertionError("corruption accepted")
    assert not other.exists()
print("PASS: 10 verified-recovery")
