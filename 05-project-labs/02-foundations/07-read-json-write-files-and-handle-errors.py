import json
from pathlib import Path
path = Path("04-fixtures/02-desired.json")
catalog = json.loads(path.read_text())
service = catalog["services"][0]
print(service["name"])
print(service["replicas"])
try:
    json.loads('{"replicas": }')
except json.JSONDecodeError:
    print("malformed JSON rejected")
print(json.dumps({"auth": True}, sort_keys=True))
