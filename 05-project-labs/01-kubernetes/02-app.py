"""Tiny dependency-free service for the disposable cluster lab."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/healthz':
            status, body = 200, {'status': 'ok'}
        elif self.path == '/':
            status, body = 200, {'service': 'hello-platform', 'version': '1'}
        else:
            status, body = 404, {'error': 'not found'}
        payload = json.dumps(body).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

if __name__ == '__main__':
    HTTPServer(('0.0.0.0', 8080), Handler).serve_forever()
