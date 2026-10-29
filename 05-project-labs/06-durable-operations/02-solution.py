import json
import uuid
def accept(connection, tenant, key, request):
    body = json.dumps(request, sort_keys=True, separators=(",", ":"))
    connection.execute("CREATE TABLE IF NOT EXISTS operations (tenant TEXT, key TEXT, body TEXT, id TEXT, UNIQUE(tenant,key))")
    connection.commit()
    connection.execute("BEGIN IMMEDIATE")
    try:
        row = connection.execute("SELECT body,id FROM operations WHERE tenant=? AND key=?", (tenant,key)).fetchone()
        if row:
            if row[0] != body:
                raise ValueError("idempotency key conflicts with request")
            operation = row[1]
        else:
            operation = str(uuid.uuid4())
            connection.execute("INSERT INTO operations VALUES (?,?,?,?)", (tenant,key,body,operation))
        connection.commit()
        return operation
    except Exception:
        connection.rollback()
        raise
