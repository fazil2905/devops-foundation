import os
import random

from http.server import BaseHTTPRequestHandler, HTTPServer

print("Starting application")

print("Starting application")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from DevOps Foundation")


server = HTTPServer(("0.0.0.0", 8080), Handler)
print("App running on port 8080", flush=True)

if os.getenv("CI") == "true":
    if random.choice([True, False]):
        print("CI sanity check passed")
        exit(0)
    else:
        print("CI sanity check failed randomly")
        exit(1)
