from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):


    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()


    def do_POST(self):
        content_len = int(self.headers.get('content-length'))
        post_body = self.rfile.read(content_len)
        data = json.loads(post_body)
        self.send_response(200)
        self.end_headers()

        print("the data is :", data)


def run():
  server_address = ('127.0.0.1', 8000)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()


run()
