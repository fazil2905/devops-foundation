from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from DevOps Foundation")


server = HTTPServer(("0.0.0.0", 8080), Handler)
print("App running on port 8080", flush=True)
server.serve_forever()
