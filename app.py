import http.server
import threading
from fastapi import FastAPI
import uvicorn

fastapi_app = FastAPI()

@fastapi_app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b'Hello world')

def start_http_server():
    server_address = ('0.0.0.0', 8000)
    httpd = http.server.HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("HTTP server started on http://localhost:8000")
    httpd.serve_forever()


def start_fastapi_server():
    print("FastAPI server started on http://localhost:8100/docs")
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8100)


if __name__ == "__main__":
    http_thread = threading.Thread(target=start_http_server)
    http_thread.daemon = True
    http_thread.start()

    start_fastapi_server()










