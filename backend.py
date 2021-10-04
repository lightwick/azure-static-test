from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from mimetypes import types_map

port = 4000

class simpleServer(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path == "/":
                self.path = "/index.html"
            if self.path == "favico.ico":
                return
            fname,ext = os.path.splitext(self.path)
            if ext in (".html",".css",".js"):
                with open(os.path.join(curdir,self.path)) as f:
                    self.send_response(200)
                    self.send_header('Content-type', types_map[ext])
                    self.end_headers()
                    self.wfile.write(f.read())
            return
        except IOError:
            self.send_error(404)
            
webServer = HTTPServer(('0.0.0.0', port), simpleServer)
print(f'Server running on port:{port}')
try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass

webServer.server_close()
print("Server stopped")

