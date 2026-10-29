import json
from urllib.request import urlopen
with urlopen("http://127.0.0.1:18081/", timeout=3) as response:
    print(response.status)
    print(response.headers.get("Content-Type"))
    body = json.load(response)
    print(body["message"])
