#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer 
from bs4 import BeautifulSoup

html_file = open('./index.html', 'r')
html_contexts = BeautifulSoup(html_file.read())
IP = "127.0.0.1"
PORT = 8080



class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"""
        
        <html>
            <head>
                <title>Some html i did remember</title>
            </head>
            <body>
                <h1>Simple http server</h1>
            </body>
        </html>
        
        """)

if __name__ == "__main__":
    webServer = HTTPServer((IP, PORT), WebServer)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        print("Interrupted by CTRL + C Exiting...")
        pass

    webServer.server_close()
    print('Server Closed!')


