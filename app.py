print('hello world')

# http://localhost:8000/

import http.server

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(b'Hello world')

if __name__ == '__main__':
    server_address = ('0.0.0.0', 8000)  # Слушаем на всех интерфейсах
    httpd = http.server.HTTPServer(server_address, SimpleHTTPRequestHandler)

    print("Server started on http://localhost:8000")
    httpd.serve_forever()

#run
#py app.py

# Commands
# docker build -t my-python-app .
# запускать докер в браузере    docker run -it -p 8000:8000 my-python-app