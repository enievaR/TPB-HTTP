from http.server import HTTPServer, BaseHTTPRequestHandler


class MonHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        reponse = """HTTP/1.1 200 OK\n
        Content-Type: text/plain\n
        Content-Length: 12\n
        Connection: close\n
        \n
        Hello World!"""
        self.wfile.write(reponse.encode())
        # Lancement du serveur sur le port 8000
        server = HTTPServer(("0.0.0.0", 8000), MonHandler)
        print("Serveur HTTP actif sur le port 8000")
        server.serve_forever()


        if __name__ == "__main__":
            MonHandler.do_GET(None)
            print("Serveur démarré. Accédez à http://localhost:8000/")
