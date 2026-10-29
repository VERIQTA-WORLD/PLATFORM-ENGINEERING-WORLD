import os
from http.server import BaseHTTPRequestHandler, HTTPServer
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            status, body = 200, b'{"status":"ok"}'
        elif self.path == "/":
            status, body = 200, b'{"service":"checkout"}'
        else:
            status, body = 404, b'{"error":"not found"}'
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
port = int(os.environ.get("PEW_PORT", "18082"))
server = HTTPServer(("127.0.0.1", port), Handler)
print("Listening on", port, flush=True)
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
