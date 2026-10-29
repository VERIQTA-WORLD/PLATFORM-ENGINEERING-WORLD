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
assert module.plan({"checkout":2},{}) == [("create","checkout",2)]
assert module.plan({"checkout":2},{"checkout":1}) == [("update","checkout",2)]
assert module.plan({"checkout":2},{"checkout":2}) == []
assert module.plan({}, {"checkout":1}) == [("retain","checkout",1)]
a={"z":1}; before=dict(a); module.plan({"a":1},a); assert a == before
print("PASS: 04 desired-state-controller")
