from http.server import HTTPServer, BaseHTTPRequestHandler


class MonHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            message = "Hello World!"
            self.send_header("Content-Length", str(len(message)))
            self.end_headers()
            self.wfile.write(message.encode())
        else:
            self.send_error(404, "Ressource non trouvée")
        # Lancement du serveur sur le port 8000
        server = HTTPServer(("0.0.0.0", 8000), MonHandler)
        print("Serveur HTTP actif sur le port 8000")
        server.serve_forever()


        if __name__ == "__main__":
            server = HTTPServer(("0.0.0.0", 8000), MonHandler)
            print("Serveur HTTP actif sur le port 8000")
            server.serve_forever()
