"""Run actual numbered test modules, project solutions and walkthroughs; refuse zero tests."""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.dont_write_bytecode=True
os.environ['PYTHONDONTWRITEBYTECODE']='1'
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--unit-only',action='store_true')
parser.add_argument('--skip-http',action='store_true',help='Report HTTP integration as unverified and run the offline checks')
args=parser.parse_args()
suite=unittest.TestSuite()
for index,path in enumerate(sorted((ROOT/'07-checks').glob('*-test*.py'))):
    spec=importlib.util.spec_from_file_location('numbered_test_'+str(index),path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(module))
if suite.countTestCases()==0:sys.exit('FAIL: no tests were loaded')
result=unittest.TextTestRunner(verbosity=2).run(suite)
if not result.wasSuccessful():sys.exit(1)
if args.unit_only:sys.exit(0)
def run(relative,*extra):
    subprocess.run([sys.executable,str(ROOT/relative),*extra],cwd=ROOT,check=True)
run('06-tools/01-audit.py')
run('06-tools/04-walkthrough.py')
for project in json.loads((ROOT/'05-project-labs/03-project-catalog.json').read_text()):
    run(project['grader'],'--solution')
if args.skip_http:print('UNVERIFIED: HTTP integration intentionally skipped')
else:run('05-project-labs/11-self-service-api/02-http-smoke.py')
print('PASS: required checks completed; Docker/kind execution is separate')
