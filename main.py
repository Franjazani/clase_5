from http.server import BaseHTTPRequestHandler, HTTPServer 
import requests
import time

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                bytes("<html><head><title>https://pythonbasics.org</title></head>"
                      f"<p>Request: {self.path}</p>"
                      "<body><p>Trabajo Practico 5 - Python.</p></body></html>",
                      "utf-8",
                      )
            )
        elif self.path == "/photos":
            response = requests.get(
                "https://jsonplaceholder.typicode.com/albums/1/photos")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                bytes(
                    response.text,
                    "utf-8",
                )
            )

        elif self.path == "/comments":
            response = requests.get(
                "https://jsonplaceholder.typicode.com/posts/1/comments")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                bytes(
                    response.text,
                    "utf-8",
                )
            )

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%:%" % (hostName, serverPort))

    try:
        webServer.server_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")    
            
