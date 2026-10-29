import importlib.util
import json
from pathlib import Path
import sqlite3
import tempfile
from concurrent.futures import ThreadPoolExecutor
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('api',ROOT/'05-project-labs/11-self-service-api/01-server.py')
api=importlib.util.module_from_spec(spec);spec.loader.exec_module(api)
class ApiStoreTests(unittest.TestCase):
    def setUp(self):
        self.directory=tempfile.TemporaryDirectory();self.addCleanup(self.directory.cleanup)
        self.store=api.Store(Path(self.directory.name)/'01-state.sqlite')
    def test_durable_request_replay(self):
        first=self.store.submit('commerce','1',{'name':'checkout','replicas':2})
        restarted=api.Store(self.store.path)
        self.assertEqual(first['id'],restarted.submit('commerce','1',{'replicas':2,'name':'checkout'})['id'])
        with self.assertRaises(api.Problem) as caught:restarted.submit('commerce','1',{'name':'checkout','replicas':3})
        self.assertEqual(caught.exception.status,409)
    def test_concurrent_request_has_one_operation(self):
        with ThreadPoolExecutor(max_workers=4) as pool:
            results=list(pool.map(lambda _:self.store.submit('commerce','same',{'name':'checkout','replicas':1}),range(8)))
        self.assertEqual(len({r['id'] for r in results}),1)
        self.assertEqual(self.store.metrics()['requested'],1)
    def test_tenant_isolation(self):
        operation=self.store.submit('commerce','1',{'name':'checkout','replicas':1})
        with self.assertRaises(api.Problem) as caught:self.store.get_operation('search',operation['id'])
        self.assertEqual(caught.exception.status,404)
        with self.assertRaises(api.Problem):self.store.submit('commerce','2',{'name':'other','replicas':1,'tenant':'search'})
    def test_reconciliation_is_repeatable(self):
        operation=self.store.submit('commerce','1',{'name':'checkout','replicas':2})
        self.assertEqual(self.store.reconcile(),1)
        self.assertEqual(self.store.reconcile(),0)
        self.assertEqual(self.store.get_operation('commerce',operation['id'])['state'],'ready')
        self.assertEqual(len(self.store.list_services('commerce')),1)
    def test_stale_update_preserves_previous_write(self):
        self.store.submit('commerce','1',{'name':'checkout','replicas':1});self.store.reconcile()
        self.assertEqual(self.store.update('commerce','checkout',{'replicas':2,'expected_revision':1})['revision'],2)
        with self.assertRaises(api.Problem):self.store.update('commerce','checkout',{'replicas':4,'expected_revision':1})
        self.assertEqual(self.store.list_services('commerce')[0]['replicas'],2)
    def test_quota_counts_pending_requests(self):
        for n in range(3):self.store.submit('commerce',str(n),{'name':'service-'+str(n),'replicas':1})
        with self.assertRaises(api.Problem) as caught:self.store.submit('commerce','4',{'name':'extra','replicas':1})
        self.assertEqual(caught.exception.status,409)
    def test_backup_snapshot_and_collision(self):
        self.store.submit('commerce','1',{'name':'checkout','replicas':1});self.store.reconcile()
        target=Path(self.directory.name)/'02-backup.sqlite';self.store.backup(target)
        restored=api.Store(target)
        self.assertEqual(restored.list_services('commerce'),self.store.list_services('commerce'))
        with self.assertRaises(FileExistsError):self.store.backup(target)
    def test_invalid_requests_have_no_side_effect(self):
        for replicas in (0,5,True,'2'):
            with self.assertRaises(api.Problem):self.store.submit('commerce','bad',{'name':'checkout','replicas':replicas})
        self.assertEqual(self.store.metrics()['requested'],0)
if __name__=='__main__':unittest.main()
