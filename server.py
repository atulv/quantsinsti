import time

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        path = self.path
        print path
        path = path.split('?')[1]
        path = path.split('&')
        for param in path:
            k,v = param.split('=')
        if long(v)%2:
            self.wfile.write({"sold": "True"})
        else:
            self.wfile.write({"sold": "False"})
        
    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write({"id": str(long(time.time())) })
        
def run(server_class=HTTPServer, handler_class=S, port=27015):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    run()
