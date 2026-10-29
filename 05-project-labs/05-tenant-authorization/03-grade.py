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
assert module.allowed({"tenant":"commerce","role":"developer"},"create","commerce")
assert not module.allowed({"tenant":"commerce","role":"operator"},"delete","search")
assert not module.allowed({"tenant":"commerce","role":"reader"},"create","commerce")
assert not module.allowed({"tenant":"commerce","role":"unknown"},"read","commerce")
assert not module.allowed({"tenant":"commerce","role":"operator"},"impersonate","commerce")
print("PASS: 05 tenant-authorization")
