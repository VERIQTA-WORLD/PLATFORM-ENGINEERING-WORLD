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
    c.execute("CREATE TABLE customers(id INTEGER PRIMARY KEY,name TEXT)")
    c.execute("INSERT INTO customers VALUES (1,'Ada')"); c.commit()
    module.migrate(c); module.migrate(c)
    assert c.execute("SELECT name,display_name FROM customers").fetchone()==("Ada","Ada")
    c.execute("UPDATE customers SET display_name='Preferred'"); c.commit()
    module.migrate(c)
    assert c.execute("SELECT display_name FROM customers").fetchone()[0]=="Preferred"
print("PASS: 09 schema-migration")
