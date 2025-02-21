import http.server
import socketserver

PORT = 8080

class Proxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, this is a simple HTTP proxy!')

with socketserver.TCPServer(("", PORT), Proxy) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
