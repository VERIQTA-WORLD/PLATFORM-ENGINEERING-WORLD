import hashlib
import json
from pathlib import Path
def restore(envelope, destination):
    payload = envelope["payload"]
    digest = hashlib.sha256(payload.encode()).hexdigest()
    if digest != envelope["sha256"]:
        raise ValueError("checksum mismatch")
    json.loads(payload)
    with Path(destination).open("x", encoding="utf-8") as output:
        output.write(payload)
