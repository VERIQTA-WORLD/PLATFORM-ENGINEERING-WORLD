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
assert module.validate({"services": [{"name":"checkout","owner":"commerce","replicas":2}]}) == []
assert "owner required" in module.validate({"services":[{"name":"checkout","owner":"","replicas":2}]})
assert "invalid replicas" in module.validate({"services":[{"name":"checkout","owner":"commerce","replicas":True}]})
assert "duplicate name" in module.validate({"services":[{"name":"checkout","owner":"commerce","replicas":1}]*2})
print("PASS: 03 catalog-contract")
