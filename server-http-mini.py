from socketserver import TCPServer, StreamRequestHandler
# On définit une classe qui gère une connexion client.
# Elle hérite de StreamRequestHandler, qui fournit wfile (sortie)
#et rfile (entrée).
class MonHandler(StreamRequestHandler):
    def handle(self):
    # Ici on peut lire avec self.rfile.readline() ou écrire
    #avec self.wfile.write()
        self.wfile.write(""""HTTP/1.1 200 OK
        Content-Type: text/plain
        Content-Length: 12
        Connection: close

        Hello World!""".encode())
# Création du serveur, lié à l'adresse et au port (ici toutes
#interfaces, port 63000).
# À chaque nouvelle connexion, une instance de MonHandler sera
#créée.
server = TCPServer(("", 8080), MonHandler)
# Lancement du serveur : boucle infinie qui accepte les
#connexions
server.serve_forever()