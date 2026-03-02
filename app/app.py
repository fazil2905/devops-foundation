import os
import logging
import time

START_TIME = time.time()

from http.server import BaseHTTPRequestHandler, HTTPServer

REQUEST_COUNT = 0
APP_HEALTHY = True

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global REQUEST_COUNT
        global APP_HEALTHY

        # Health endpoint
        if self.path == "/health":
            uptime = int(time.time() - START_TIME)

            logging.info("Health check requested")

            if APP_HEALTHY:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(f"OK - Uptime: {uptime}s".encode())
            else:
                logging.error("Application reported as UNHEALTHY")
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b"UNHEALTHY")

            return

            
        # Normal request handling
        REQUEST_COUNT += 1

        if REQUEST_COUNT > 20:
            logging.error("System marked unhealthy due to high request load")
            APP_HEALTHY = False

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
