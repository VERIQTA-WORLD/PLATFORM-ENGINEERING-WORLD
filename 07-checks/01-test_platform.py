import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('pe', ROOT/'03-reference-platform/01-pe.py')
pe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pe)

class PlatformTests(unittest.TestCase):
    def setUp(self):
        self.desired = pe.read(ROOT/'04-fixtures/02-desired.json')
        self.actual = pe.read(ROOT/'04-fixtures/01-actual.json')

    def cli(self, *args):
        return subprocess.run([sys.executable, str(ROOT/'03-reference-platform/01-pe.py'), *map(str,args)], cwd=ROOT, capture_output=True, text=True)

    def test_valid_and_invalid_contracts(self):
        self.assertEqual(pe.validate(self.desired), [])
        errors = pe.validate(pe.read(ROOT/'04-fixtures/04-invalid.json'))
        self.assertEqual(len(errors), 2)
        self.assertTrue(any('owner' in e for e in errors))
        self.assertTrue(any('authentication' in e for e in errors))

    def test_duplicate_identity_rejected(self):
        self.desired['services'] *= 2
        self.assertTrue(any('duplicate' in e for e in pe.validate(self.desired)))

    def test_name_cannot_escape_output_root(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.cli('scaffold', '../escape', '--owner', 'team', '--out', Path(directory)/'service')
            self.assertEqual(result.returncode, 2)
            self.assertFalse((Path(directory)/'service').exists())

    def test_apply_converges_without_mutating_inputs(self):
        baseline = copy.deepcopy(self.actual)
        merged = pe.apply(self.desired, self.actual)
        self.assertEqual(pe.reconcile(self.desired, merged), [])
        self.assertEqual(self.actual, baseline)
        self.assertEqual(merged['services'][0]['replicas'], 2)

    def test_unmanaged_resources_are_retained(self):
        result = pe.apply({'services': []}, self.actual)
        self.assertEqual(result, self.actual)
        self.assertEqual(pe.reconcile({'services': []}, result)[0]['action'], 'retain-unmanaged')

    def test_rejected_apply_does_not_write(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)/'state.json'
            result = self.cli('apply', '04-fixtures/04-invalid.json', '04-fixtures/01-actual.json', '--out', target)
            self.assertEqual(result.returncode, 2)
            self.assertFalse(target.exists())

    def test_policy_rejection_exit_code(self):
        self.assertEqual(self.cli('validate', '04-fixtures/04-invalid.json').returncode, 1)
        self.assertEqual(self.cli('validate', 'examples/absent.json').returncode, 2)

    def test_slo_budget_and_latency(self):
        result = pe.reliability(pe.read(ROOT/'04-fixtures/03-events.json'), .99)
        self.assertEqual((result['good'], result['bad']), (97, 3))
        self.assertEqual(result['remaining_budget'], -2)
        self.assertEqual(result['burn_rate'], 3)
        self.assertEqual(pe.reliability([{'status':200,'latency_ms':300}], .99)['good'], 1)

    def test_slo_missing_data_is_unknown(self):
        with self.assertRaises(ValueError): pe.reliability([], .99)
        with self.assertRaises(ValueError): pe.reliability([{'status':200,'latency_ms':1}], 1)

    def test_scaffold_is_valid_and_refuses_collision(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)/'inventory'
            args = ('scaffold','inventory','--owner','commerce','--out',target)
            self.assertEqual(self.cli(*args).returncode, 0)
            self.assertEqual(pe.validate(pe.read(target/'01-service.json')), [])
            self.assertTrue((target/'01-docs/01-runbook.md').is_file())
            content = (target/'01-service.json').read_bytes()
            self.assertEqual(self.cli(*args).returncode, 2)
            self.assertEqual((target/'01-service.json').read_bytes(), content)

    def test_backup_round_trip_corruption_and_collision(self):
        with tempfile.TemporaryDirectory() as directory:
            backup, restored = Path(directory)/'backup.json', Path(directory)/'restored.json'
            self.assertEqual(self.cli('backup','04-fixtures/02-desired.json','--out',backup).returncode, 0)
            self.assertEqual(self.cli('restore',backup,'--out',restored).returncode, 0)
            self.assertEqual(restored.read_bytes(), (ROOT/'04-fixtures/02-desired.json').read_bytes())
            self.assertEqual(self.cli('restore',backup,'--out',restored).returncode, 2)
            envelope = pe.read(backup)
            envelope['payload'] += ' '
            backup.write_text(json.dumps(envelope))
            target = Path(directory)/'corrupted.json'
            self.assertEqual(self.cli('restore',backup,'--out',target).returncode, 2)
            self.assertFalse(target.exists())

    def test_contract_field_types(self):
        for value in (True, '2', 1.5, 0):
            catalog = copy.deepcopy(self.desired)
            catalog['services'][0]['replicas'] = value
            self.assertTrue(any('replicas' in e for e in pe.validate(catalog)))
        catalog = copy.deepcopy(self.desired)
        catalog['services'][0]['auth'] = 'true'
        self.assertTrue(any('boolean' in e for e in pe.validate(catalog)))
        catalog['services'][0]['name'] = ['invalid']
        self.assertTrue(pe.validate(catalog))

    def test_slo_rejects_invalid_telemetry(self):
        for event in ({'status': 700, 'latency_ms': 1},
                      {'status': 200, 'latency_ms': -1},
                      {'status': 200, 'latency_ms': float('nan')}):
            with self.assertRaises(ValueError): pe.reliability([event], .99)

    def test_malformed_json_has_actionable_error(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory)/'bad.json'
            source.write_text('{')
            result = self.cli('validate', source)
            self.assertEqual(result.returncode, 2)
            self.assertIn('error:', result.stderr)
            self.assertNotIn('Traceback', result.stderr)

    def test_cost_fixture(self):
        result = self.cli('cost','04-fixtures/05-usage.json')
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout), {'commerce':2.88, 'search':4.8})

if __name__ == '__main__': unittest.main()
