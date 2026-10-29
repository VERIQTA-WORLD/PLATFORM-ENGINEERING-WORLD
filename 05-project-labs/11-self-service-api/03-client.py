"""Small client so the API lab does not require curl or shell-specific JSON quoting."""
import argparse
import json
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
import sys
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('method',choices=('GET','POST','PUT'))
parser.add_argument('path')
parser.add_argument('--identity',choices=('commerce','search','operator','invalid'),default='commerce')
parser.add_argument('--key',default='lesson-request-1')
parser.add_argument('--body-file',type=Path)
parser.add_argument('--save',type=Path)
parser.add_argument('--port',type=int,default=18083)
args=parser.parse_args()
body=args.body_file.read_bytes() if args.body_file else (b'{}' if args.method=='POST' else None)
headers={'Authorization':'Bearer demo-'+args.identity,'Idempotency-Key':args.key,'Content-Type':'application/json'}
request=Request('http://127.0.0.1:'+str(args.port)+args.path,data=body,headers=headers,method=args.method)
try:
    with urlopen(request,timeout=6) as response:status,result=response.status,json.load(response)
except HTTPError as error:status,result=error.code,json.load(error)
except URLError as error:sys.exit('Connection failed. Start 01-server.py and verify the port. '+str(error.reason))
print('HTTP',status);print(json.dumps(result,indent=2))
if args.save:
    with args.save.open('x') as output:json.dump(result,output,indent=2)
sys.exit(0 if status<400 else 1)
