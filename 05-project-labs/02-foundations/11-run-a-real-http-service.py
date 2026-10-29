import json
from http.server import BaseHTTPRequestHandler, HTTPServer
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        payload = json.dumps({"message": "hello platform"}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)
print("Listening at http://127.0.0.1:18081", flush=True)
HTTPServer(("127.0.0.1", 18081), Handler).serve_forever()
