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
calls=[]
def transient():
    calls.append(1)
    if len(calls)<3: raise TimeoutError("temporary")
    return "ready"
assert module.attempt(transient,3)=="ready" and len(calls)==3
calls.clear()
def denied():
    calls.append(1); raise PermissionError("denied")
try: module.attempt(denied,4)
except PermissionError: pass
else: raise AssertionError("denial swallowed")
assert len(calls)==1
try: module.attempt(lambda: (_ for _ in ()).throw(TimeoutError()),2)
except TimeoutError: pass
else: raise AssertionError("exhaustion swallowed")
print("PASS: 08 retry-classification")
