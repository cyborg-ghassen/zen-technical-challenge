from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8000

class MyHandler(SimpleHTTPRequestHandler):
    pass

httpd = HTTPServer(('localhost', PORT), MyHandler)
print(f"Serving at http://localhost:{PORT}")
httpd.serve_forever()