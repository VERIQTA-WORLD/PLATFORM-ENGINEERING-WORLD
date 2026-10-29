"""Exercise actual loopback HTTP using a temporary database and ephemeral port."""
import importlib.util
import json
from pathlib import Path
import tempfile
import threading
from urllib.request import Request,urlopen
from urllib.error import HTTPError
from http.server import ThreadingHTTPServer
spec=importlib.util.spec_from_file_location('api',Path(__file__).with_name('01-server.py'))
api=importlib.util.module_from_spec(spec);spec.loader.exec_module(api)
with tempfile.TemporaryDirectory() as directory:
    store=api.Store(Path(directory)/'01-state.sqlite')
    server=ThreadingHTTPServer(('127.0.0.1',0),api.handler_for(store))
    thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
    base='http://127.0.0.1:'+str(server.server_address[1])
    def request(method,path,body=None,token='demo-commerce',key='request-1'):
        headers={'Authorization':'Bearer '+token,'Idempotency-Key':key,'Content-Type':'application/json'}
        data=None if body is None else json.dumps(body).encode()
        try:
            with urlopen(Request(base+path,data=data,headers=headers,method=method),timeout=3) as response:
                return response.status,json.load(response)
        except HTTPError as error:return error.code,json.load(error)
    try:
        assert request('GET','/healthz')[0]==200
        assert request('GET','/services',token='unknown')[0]==401
        status,operation=request('POST','/services',{'name':'checkout','replicas':2});assert status==202
        assert request('POST','/services',{'replicas':2,'name':'checkout'})[1]['id']==operation['id']
        assert request('POST','/services',{'name':'checkout','replicas':3})[0]==409
        assert request('GET','/operations/'+operation['id'],token='demo-search')[0]==404
        assert request('POST','/reconcile',{})[0]==403
        assert request('POST','/reconcile',{},token='demo-operator')[1]['reconciled']==1
        assert request('POST','/reconcile',{},token='demo-operator')[1]['reconciled']==0
        assert request('GET','/services')[1]['services'][0]['revision']==1
        assert request('PUT','/services/checkout',{'replicas':3,'expected_revision':1})[0]==200
        assert request('PUT','/services/checkout',{'replicas':4,'expected_revision':1})[0]==409
        assert request('GET','/services',token='demo-search')[1]['services']==[]
        print('PASS: real HTTP, 401, tenant isolation, request replay, conflict, operator authorization, reconciliation and stale-write rejection')
    finally:
        server.shutdown();thread.join(timeout=5);server.server_close()
