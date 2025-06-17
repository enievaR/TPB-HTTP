- **Quelle est la structure de la ligne GET / HTTP/1.1 ? Quels sont les trois éléments et leur rôle ?**

    - La structure de la ligne GET / HTTP/1.1 est composée de trois éléments :
        1. **Méthode** : "GET" indique le type de requête HTTP, ici une demande pour récupérer des données.
        2. **Chemin** : "/" spécifie la ressource demandée, ici la racine du serveur.
        3. **Version du protocole** : "HTTP/1.1" indique la version du protocole HTTP utilisée pour la communication.

- **Pourquoi faut-il appuyer deux fois sur Entrée pour que le serveur réponde ? Que représente cette ligne vide dans le protocole HTTP ?**

    - Il faut appuyer deux fois sur Entrée pour indiquer la fin des en-têtes de la requête HTTP. La ligne vide représente la séparation entre les en-têtes de la requête et le corps de la requête (s'il y en avait un). Dans le cas d'une requête GET, il n'y a pas de corps, donc cette ligne vide signale au serveur que les en-têtes sont terminés et qu'il peut traiter la requête.

- **Que se passe-t-il si vous oubliez cette ligne vide ? Le serveur répond-il quand même ?**

    - Si vous oubliez cette ligne vide, le serveur peut ne pas comprendre que les en-têtes de la requête sont terminés. Cela peut entraîner un comportement inattendu, comme le serveur ne répondant pas ou renvoyant une erreur. En général, les serveurs HTTP s'attendent à cette ligne vide pour traiter correctement la requête.

- **Que signifie le code 200 OK dans la réponse ? Qu’indique un code 404 ou 301 ?**
    - Le code **200 OK** dans la réponse signifie que la requête a été traitée avec succès et que la ressource demandée est disponible. 
    - Un code **404 Not Found** indique que la ressource demandée n'a pas été trouvée sur le serveur. 
    - Un code **301 Moved Permanently** signifie que la ressource a été déplacée de façon permanente vers une nouvelle URL, et le client doit utiliser cette nouvelle URL pour les futures requêtes.

- **Quelle est la toute première ligne envoyée par le serveur ? Que contient-elle ?**
    - La toute première ligne envoyée par le serveur est la ligne de statut, qui commence par "HTTP/1.1 200 OK". Elle contient la version du protocole HTTP utilisée (HTTP/1.1), le code de statut (200) et une brève description du statut (OK). Cette ligne informe le client que la requête a été traitée avec succès.

- **Relevez les entêtes présents dans la réponse (Content-Type, Content-Length,etc.) : à quoi servent-ils ?**
    - Les en-têtes présents dans la réponse HTTP fournissent des informations supplémentaires sur la réponse. Par exemple :
        - **Content-Type** : Indique le type de contenu de la réponse (par exemple, "text/html" pour une page HTML).
        - **Transfer-Encoding** : Indique la méthode de codage utilisée pour transférer le corps de la réponse (par exemple, "chunked" pour un transfert en morceaux).
        - **Last-Modified** : Indique la date et l'heure de la dernière modification de la ressource, permettant au client de savoir si la ressource a été modifiée depuis sa dernière récupération.
        - **Cache-Control** : Indique les directives de mise en cache pour la réponse, permettant au client de savoir comment gérer la mise en cache de la ressource.
        - **Expires** : Indique la date et l'heure auxquelles la réponse expire, après quoi elle ne doit plus être considérée comme valide.
        - **Vary** : Indique les en-têtes qui peuvent influencer la réponse, permettant au serveur de gérer les variations de contenu en fonction des en-têtes de la requête.
        - **cf-cache-status** : Indique l'état du cache pour la réponse, utilisé par les serveurs de cache pour déterminer si la réponse peut être servie à partir du cache ou doit être récupérée à nouveau.
        - **report-to** : Indique l'URL à laquelle les rapports d'erreurs ou de problèmes doivent être envoyés.
        **NEL** : Indique les paramètres de la politique de rapport d'erreurs, permettant au serveur de collecter des informations sur les erreurs rencontrées par le client.
        **CF-RAY** : Indique l'identifiant unique de la requête, utilisé pour le suivi et le diagnostic des problèmes.
        - **ALT-SVC** : Indique les services alternatifs disponibles pour la ressource, permettant au client de savoir s'il existe d'autres moyens d'accéder à la même ressource.
        - **Server-timing** : Indique le temps de traitement du serveur pour la requête, permettant au client de mesurer les performances du serveur.
        - **Server** : Indique le logiciel du serveur qui a traité la requête.
        - **Connection** : Indique si la connexion doit rester ouverte ou être fermée après la réponse.

- **Quelle est la première ligne non entête du corps ? À quoi reconnaît-on la séparation ?**

    - La première ligne non entête du corps est la ligne qui contient le contenu réel de la réponse, généralement le code HTML de la page demandée. On reconnaît la séparation entre les en-têtes et le corps par la ligne vide qui suit les en-têtes. Cette ligne vide indique que les en-têtes sont terminés et que le corps de la réponse commence.

- **Que se passe-t-il si vous tapez une URL invalide (ex : GET /truc HTTP/1.1) ? Quel est le code de retour ?**

    - Si vous tapez une URL invalide, comme "GET /truc HTTP/1.1", le serveur renvoie généralement un code de retour **404 Not Found**. Cela signifie que la ressource demandée n'a pas été trouvée sur le serveur. Le serveur peut également renvoyer d'autres codes d'erreur en fonction de la configuration et de la nature de l'erreur rencontrée.

- **Le contenu retourné dans ce cas est-il aussi du HTML ? Que contient-il exactement ?**

    - Oui, le contenu retourné dans le cas d'une URL invalide est généralement du HTML. Il contient un message d'erreur indiquant que la ressource demandée n'a pas été trouvée. Ce message peut inclure des informations supplémentaires, comme une description de l'erreur, des liens vers d'autres ressources ou une suggestion pour corriger l'erreur. Le but est de fournir au client une indication claire de ce qui s'est mal passé et comment il peut éventuellement résoudre le problème.

