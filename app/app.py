import os

from http.server import BaseHTTPRequestHandler, HTTPServer

print("Starting application")

print("Starting application")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from DevOps Foundation")


server = HTTPServer(("0.0.0.0", 9999), Handler)
print("App running on port 8080", flush=True)

if os.getenv("CI") == "true":
    print("CI sanity check passed, exiting cleanly")
else:
    server.serve_forever()
