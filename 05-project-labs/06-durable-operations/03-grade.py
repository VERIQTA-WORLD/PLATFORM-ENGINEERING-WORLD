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
import sqlite3
with sqlite3.connect(":memory:") as c:
    first=module.accept(c,"commerce","key-1",{"name":"checkout","replicas":2})
    assert first == module.accept(c,"commerce","key-1",{"replicas":2,"name":"checkout"})
    assert first != module.accept(c,"search","key-1",{"name":"checkout","replicas":2})
    try: module.accept(c,"commerce","key-1",{"name":"different"})
    except ValueError: pass
    else: raise AssertionError("conflicting request accepted")
    assert c.execute("SELECT COUNT(*) FROM operations").fetchone()[0] == 2
print("PASS: 06 durable-operations")
