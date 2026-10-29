"""Loopback-only teaching API with SQLite-backed operations and synthetic identities."""
import argparse
import hmac
import json
import re
import sqlite3
import uuid
from contextlib import closing
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

# Public fictional identities for this loopback lab, never real credentials.
ACTORS = {
    'demo-commerce': {'tenant': 'commerce', 'role': 'developer'},
    'demo-search': {'tenant': 'search', 'role': 'developer'},
    'demo-operator': {'tenant': '*', 'role': 'operator'},
}
class Problem(Exception):
    def __init__(self, status, message):
        self.status, self.message = status, message
        super().__init__(message)

class Store:
    def __init__(self, path):
        self.path = str(path)
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with closing(self.connect()) as c, c:
            c.executescript('''
            CREATE TABLE IF NOT EXISTS operations (
                id TEXT PRIMARY KEY, tenant TEXT NOT NULL, key TEXT NOT NULL,
                name TEXT NOT NULL, request TEXT NOT NULL, state TEXT NOT NULL,
                UNIQUE(tenant,key));
            CREATE TABLE IF NOT EXISTS services (
                tenant TEXT NOT NULL, name TEXT NOT NULL, replicas INTEGER NOT NULL,
                revision INTEGER NOT NULL, PRIMARY KEY(tenant,name));
            ''')
    def connect(self):
        c = sqlite3.connect(self.path, timeout=5)
        c.row_factory = sqlite3.Row
        return c
    def submit(self, tenant, key, request):
        if not isinstance(key, str) or not 1 <= len(key) <= 100:
            raise Problem(422, 'supply Idempotency-Key of 1–100 characters')
        if not isinstance(request, dict): raise Problem(422, 'request must be an object')
        if request.get('tenant', tenant) != tenant: raise Problem(403, 'cross-tenant request denied')
        if not isinstance(request.get('name'), str) or not re.fullmatch(r'[a-z][a-z0-9-]{1,39}', request['name']):
            raise Problem(422, 'name must be 2–40 lowercase letters, digits or hyphens, starting with a letter')
        replicas = request.get('replicas')
        if type(replicas) is not int or not 1 <= replicas <= 4:
            raise Problem(422, 'replicas must be an integer from 1 to 4')
        body = json.dumps({'name':request['name'], 'replicas':replicas}, sort_keys=True)
        with closing(self.connect()) as c:
            c.execute('BEGIN IMMEDIATE')
            try:
                old = c.execute('SELECT * FROM operations WHERE tenant=? AND key=?', (tenant,key)).fetchone()
                if old:
                    if old['request'] != body: raise Problem(409, 'idempotency key conflicts with request')
                    c.commit(); return dict(old)
                if c.execute('SELECT 1 FROM operations WHERE tenant=? AND name=?', (tenant,request['name'])).fetchone():
                    raise Problem(409, 'service name already requested; use the existing operation')
                # Count pending and completed requests under the same serialized transaction.
                if c.execute('SELECT COUNT(*) FROM operations WHERE tenant=?', (tenant,)).fetchone()[0] >= 3:
                    raise Problem(409, 'demo tenant quota is three services')
                operation = str(uuid.uuid4())
                c.execute('INSERT INTO operations VALUES (?,?,?,?,?,?)', (operation,tenant,key,request['name'],body,'requested'))
                c.commit()
                return {'id':operation,'tenant':tenant,'key':key,'name':request['name'],'request':body,'state':'requested'}
            except Exception:
                c.rollback(); raise
    def get_operation(self, tenant, operation):
        with closing(self.connect()) as c:
            row = c.execute('SELECT * FROM operations WHERE tenant=? AND id=?', (tenant,operation)).fetchone()
            if row is None: raise Problem(404, 'operation not found')
            return dict(row)
    def list_services(self, tenant):
        with closing(self.connect()) as c:
            return [dict(row) for row in c.execute('SELECT * FROM services WHERE tenant=? ORDER BY name', (tenant,))]
    def reconcile(self):
        with closing(self.connect()) as c:
            c.execute('BEGIN IMMEDIATE')
            try:
                rows = c.execute("SELECT * FROM operations WHERE state='requested' ORDER BY id").fetchall()
                for row in rows:
                    body = json.loads(row['request'])
                    c.execute('INSERT INTO services VALUES (?,?,?,1)', (row['tenant'],row['name'],body['replicas']))
                    c.execute("UPDATE operations SET state='ready' WHERE id=?", (row['id'],))
                c.commit(); return len(rows)
            except Exception:
                c.rollback(); raise
    def update(self, tenant, name, request):
        if not isinstance(request, dict): raise Problem(422,'request must be an object')
        replicas, revision = request.get('replicas'), request.get('expected_revision')
        if type(replicas) is not int or not 1 <= replicas <= 4: raise Problem(422,'replicas must be 1–4')
        if type(revision) is not int or revision < 1: raise Problem(422,'expected_revision must be positive')
        with closing(self.connect()) as c, c:
            cursor = c.execute('UPDATE services SET replicas=?, revision=revision+1 WHERE tenant=? AND name=? AND revision=?', (replicas,tenant,name,revision))
            if cursor.rowcount != 1: raise Problem(409,'resource is missing or expected_revision is stale')
        return {'name':name,'tenant':tenant,'replicas':replicas,'revision':revision+1}
    def metrics(self):
        with closing(self.connect()) as c:
            return {state: c.execute('SELECT COUNT(*) FROM operations WHERE state=?',(state,)).fetchone()[0] for state in ('requested','ready')}
    def backup(self, target):
        target=Path(target)
        with target.open('xb'): pass
        try:
            with closing(self.connect()) as source, closing(sqlite3.connect(target)) as destination:
                source.backup(destination)
                if destination.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
                    raise ValueError('backup integrity check failed')
        except Exception:
            target.unlink(missing_ok=True); raise

def handler_for(store):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, format, *args):
            # Avoid logging token-bearing headers or payloads.
            pass
        def reply(self, status, body):
            payload=json.dumps(body).encode()
            self.send_response(status)
            self.send_header('Content-Type','application/json')
            self.send_header('Content-Length',str(len(payload)))
            self.end_headers(); self.wfile.write(payload)
        def actor(self):
            presented=self.headers.get('Authorization','')
            for token, actor in ACTORS.items():
                if hmac.compare_digest(presented, 'Bearer '+token): return actor
            raise Problem(401,'use a documented fictional demo identity')
        def body(self):
            try: size=int(self.headers.get('Content-Length','0'))
            except ValueError: raise Problem(400,'invalid Content-Length')
            if not 0 < size <= 4096: raise Problem(413,'body must contain 1–4096 bytes')
            try: return json.loads(self.rfile.read(size))
            except (ValueError,UnicodeError): raise Problem(400,'malformed JSON')
        def dispatch(self):
            if self.command=='GET' and self.path=='/healthz':return 200,{'status':'ok'}
            actor=self.actor(); tenant=actor['tenant']
            if self.path in ('/reconcile','/metrics'):
                if actor['role']!='operator': raise Problem(403,'operator role required')
                if self.path=='/reconcile' and self.command=='POST':return 200,{'reconciled':store.reconcile()}
                if self.path=='/metrics' and self.command=='GET':return 200,store.metrics()
            if actor['role']!='developer': raise Problem(403,'developer identity required for tenant service operations')
            if self.path=='/services':
                if self.command=='POST':return 202,store.submit(tenant,self.headers.get('Idempotency-Key'),self.body())
                if self.command=='GET':return 200,{'services':store.list_services(tenant)}
            if self.path.startswith('/operations/') and self.command=='GET':return 200,store.get_operation(tenant,self.path.rsplit('/',1)[-1])
            if self.path.startswith('/services/') and self.command=='PUT':return 200,store.update(tenant,self.path.rsplit('/',1)[-1],self.body())
            raise Problem(404,'route not found')
        def execute(self):
            self.connection.settimeout(5)
            try:
                status, body=self.dispatch()
                self.reply(status,body)
            except Problem as error:self.reply(error.status,{'error':error.message})
            except sqlite3.OperationalError:self.reply(503,{'error':'database unavailable; inspect the local database and retry safely'})
            except TimeoutError:self.reply(408,{'error':'request body timed out'})
        do_GET=execute
        do_POST=execute
        do_PUT=execute
    return Handler

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--db',required=True)
    parser.add_argument('--port',type=int,default=18083)
    parser.add_argument('--backup-to')
    args=parser.parse_args();store=Store(args.db)
    if args.backup_to:
        store.backup(args.backup_to); print('Backup verified'); return
    server=ThreadingHTTPServer(('127.0.0.1',args.port),handler_for(store))
    print('Teaching API: http://127.0.0.1:'+str(server.server_address[1]),flush=True)
    try:server.serve_forever()
    except KeyboardInterrupt:pass
    finally:server.server_close()
if __name__=='__main__':main()
