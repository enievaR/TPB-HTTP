from http.server import HTTPServer, BaseHTTPRequestHandler


class MonHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        reponse = """HTTP/1.1 200 OK
        Content-Type: text/plain
        Content-Length: 12
        Connection: close

        Hello World!"""
        self.wfile.write(reponse.encode())
        # Lancement du serveur sur le port 8000
        server = HTTPServer(("localhost", 8080), MonHandler)
        server.serve_forever()


        if __name__ == "__main__":
            MonHandler.do_GET(None)
            print("Serveur démarré. Accédez à http://localhost:8080/")
