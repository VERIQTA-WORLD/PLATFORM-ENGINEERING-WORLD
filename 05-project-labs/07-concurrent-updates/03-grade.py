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
    c.execute("CREATE TABLE services(name TEXT PRIMARY KEY, replicas INTEGER, revision INTEGER)")
    c.execute("INSERT INTO services VALUES ('checkout',1,1)"); c.commit()
    assert module.update(c,"checkout",1,2) == 2
    try: module.update(c,"checkout",1,9)
    except ValueError: pass
    else: raise AssertionError("stale writer accepted")
    assert c.execute("SELECT replicas,revision FROM services").fetchone() == (2,2)
print("PASS: 07 concurrent-updates")
