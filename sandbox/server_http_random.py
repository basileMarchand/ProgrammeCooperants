from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import numpy as np
import json

PORT = 3003

class RandomHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        params = parse_qs(url.query)
        ressource = url.path.replace("3003", "")

        if not "n" in params.keys():
            params["n"]=[1]

        if ressource.startswith("/api/random/int"):
            xmin = 0
            xmax = 100
            value = np.random.randint(xmin,xmax,int(params["n"][0]))
        elif ressource.startswith("/api/random/float"):
            value = np.random.rand( int(params["n"][0]) )

        else:
            self.send_response(404)
            self.end_headers()
            return 

        self.send_response(200)
        self.send_header(b"Content-type", b"application/json")
        self.end_headers()
        to_send = json.dumps( value.tolist() )
        self.wfile.write( to_send.encode() )


server = HTTPServer(("127.0.0.1",PORT), RandomHandler)
server.serve_forever()

        

