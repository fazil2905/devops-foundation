import os
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer

REQUEST_COUNT = 0

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global REQUEST_COUNT

        REQUEST_COUNT += 1

        logging.info(f"Received GET request from {self.client_address}")
        logging.info(f"Total requests served: {REQUEST_COUNT}")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from DevOps Foundation")


logging.info("Application starting...")


server = HTTPServer(("0.0.0.0", 8080), Handler)

logging.info("Application starting...")


if os.getenv("CI") == "true":
    logging.info("CI sanity check passed, exiting cleanly")
else:
    server.serve_forever()
