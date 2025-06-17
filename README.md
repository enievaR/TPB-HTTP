# Partie 

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


# Partie 2.1
- **Est-ce que votre client (navigateur, curl, telnet…) reçoit bien une réponse ? Quel contenu voyez-vous à l’écran ?**

    - Oui on recoit bien une réponse. On recoit la string "Hello World!" qui est le contenu de la page demandée.

- **Quelle est la structure exacte du message que vous renvoyez (statut, entêtes, ligne vide, corps) ?**

    - La structure exacte du message que je renvoie est la suivante :
        1. **Ligne de statut** : "HTTP/1.1 200 OK" indique que la requête a été traitée avec succès.
        2. **En-têtes** : 
            - "Content-Type: text/plain" indique que le contenu est du texte brut.
            - "Content-Length: 13" indique la longueur du corps de la réponse (13 octets pour "Hello World!").
        3. **Ligne vide** : Sépare les en-têtes du corps de la réponse.
        4. **Corps** : "Hello World!" est le contenu réel de la réponse.

- **Que se passe-t-il si vous changez Content-Length: 12 en une autre valeur ?**

    - Si je change "Content-Length: 12" en une autre valeur, cela peut entraîner des problèmes lors de la réception de la réponse par le client. Si la valeur est inférieure à la longueur réelle du corps, le client peut ne pas recevoir tout le contenu, ce qui peut provoquer des erreurs ou un affichage incorrect. Si la valeur est supérieure, le client peut attendre plus de données qu'il n'en reçoit, ce qui peut également entraîner des erreurs ou un comportement inattendu.

- **Que se passe-t-il si vous omettez complètement cette ligne ?**
    - Si j'omets complètement la ligne "Content-Length", le client peut ne pas savoir combien de données il doit attendre dans le corps de la réponse. Cela peut entraîner un comportement indéfini, où le client attend indéfiniment des données ou ne reçoit pas le contenu complet. Certains clients peuvent gérer cela en utilisant d'autres mécanismes, comme le transfert en morceaux (chunked transfer encoding), mais cela dépend de la configuration du serveur et du client.

- **Que se passe-t-il si vous supprimez la ligne vide entre les entêtes et le message ? Le navigateur ou le client affiche-t-il encore quelque chose ?**

    - Si je supprime la ligne vide entre les en-têtes et le message, le client peut ne pas interpréter correctement la réponse. Certains clients peuvent afficher un message d'erreur ou ne pas afficher du tout le contenu, car ils s'attendent à une séparation claire entre les en-têtes et le corps de la réponse. Cela peut entraîner un comportement inattendu, comme l'affichage d'une page blanche ou d'un message d'erreur indiquant que la réponse est mal formée.

- **Le message s’affiche-t-il dans telnet ? Et dans curl ? Et dans un navigateur ? Pourquoi certains outils sont-ils plus stricts que d’autres ?**

    - Dans **telnet**, le message s'affiche généralement correctement, car telnet est un outil simple qui affiche le texte brut reçu du serveur. 
    - Dans **curl**, le message s'affiche également correctement, car curl est conçu pour traiter les requêtes HTTP et afficher le contenu de la réponse.
    - Dans un **navigateur**, le message peut ne pas s'afficher correctement si les en-têtes ne sont pas conformes aux spécifications HTTP, comme l'absence de ligne vide ou une mauvaise gestion des en-têtes. Les navigateurs sont souvent plus stricts dans la validation des réponses HTTP pour garantir une expérience utilisateur cohérente et éviter les erreurs d'affichage.

# Partie 2.2

- **Quelle est la structure de la ligne de requête HTTP reçue côté serveur ? Quels sont les trois éléments que vous devez extraire ?**

    - La structure de la ligne de requête HTTP reçue côté serveur est composée de trois éléments :
        1. **Méthode** : Indique le type de requête (par exemple, "GET", "POST").
        2. **Chemin** : Spécifie la ressource demandée (par exemple, "/").
        3. **Version du protocole** : Indique la version du protocole HTTP utilisée (par exemple, "HTTP/1.1").

- **Que se passe-t-il si la ligne est mal formée (ex. : vide ou incomplète) ? Comment éviter une erreur dans votre code ?**

    - Si la ligne est mal formée (par exemple, vide ou incomplète), le serveur peut renvoyer une erreur 400 Bad Request, indiquant que la requête n'est pas valide. Pour éviter une erreur dans le code, il est important de vérifier la validité de la ligne de requête avant de tenter d'extraire les éléments. Cela peut inclure des vérifications pour s'assurer que la ligne n'est pas vide, qu'elle contient les trois éléments attendus et qu'ils sont correctement formatés.

- **Que contient exactement la variable chemin ? Est-ce toujours ce que l’utilisateur a tapé dans l’URL ?**
    - La variable `chemin` contient la partie de l'URL qui suit le nom de domaine et le port, généralement la ressource demandée sur le serveur. Ce n'est pas toujours exactement ce que l'utilisateur a tapé dans l'URL, car le serveur peut rediriger ou modifier le chemin en fonction de sa configuration ou des règles de routage. Par exemple, un serveur peut rediriger une requête vers une autre ressource ou ajouter des paramètres de requête supplémentaires.

**Que fait votre serveur si la méthode reçue est autre que GET ?Par exemple : POST, FOO, TEAPOT ?**

    - Si la méthode reçue est autre que GET, le serveur peut renvoyer une erreur 405 Method Not Allowed, indiquant que la méthode n'est pas prise en charge pour la ressource demandée. Pour des méthodes spécifiques comme POST, le serveur peut également renvoyer une erreur 501 Not Implemented si la méthode n'est pas implémentée. Pour des méthodes non standard comme FOO ou TEAPOT, le serveur peut également renvoyer une erreur 418 I'm a teapot, qui est une réponse humoristique définie dans le protocole HTTP pour indiquer que le serveur ne peut pas traiter la requête.

**Que se passe-t-il si le chemin n’est pas reconnu (ex. : /truc) ? Quel message retournez-vous ? Est-il lisible ?**

    - Si le chemin n'est pas reconnu (par exemple, "/truc"), le serveur renvoie généralement une erreur 404 Not Found, indiquant que la ressource demandée n'a pas été trouvée sur le serveur. Le message retourné peut être un simple texte ou du HTML, mais il est important qu'il soit lisible pour l'utilisateur. Par exemple, le message peut contenir une description de l'erreur et des suggestions pour corriger la requête, comme vérifier l'URL ou contacter l'administrateur du site.

**Le message 404 Not Found est-il suffisant comme réponse ? Pourriez-vous y ajouter un texte plus explicite ?**

    - Le message 404 Not Found est un bon point de départ, mais il peut être amélioré en ajoutant un texte plus explicite. Par exemple, le message peut inclure des informations supplémentaires sur la nature de l'erreur, des suggestions pour corriger la requête (comme vérifier l'URL ou utiliser la barre de recherche du site), et éventuellement des liens vers d'autres ressources ou pages du site. Cela améliore l'expérience utilisateur en fournissant des informations utiles et en aidant l'utilisateur à naviguer sur le site.

**Est-ce que les chemins /motd, /motd/, et /motd ?x=42 sont identiques ? Comment les différencier ou les normaliser ?**

    - Les chemins `/motd`, `/motd/`, et `/motd?x=42` ne sont pas identiques. 
        - `/motd` et `/motd/` peuvent être considérés comme équivalents dans de nombreux contextes, car le dernier slash est souvent utilisé pour indiquer un répertoire.
        - Cependant, `/motd?x=42` inclut un paramètre de requête (`x=42`), ce qui le rend différent des deux premiers chemins.
    - Pour les différencier ou les normaliser, on peut :
        - Supprimer le dernier slash si ce n'est pas nécessaire pour la logique du serveur.
        - Traiter les paramètres de requête séparément pour éviter toute confusion entre les chemins et les paramètres.
        - Utiliser une fonction de normalisation pour standardiser les chemins avant de les traiter, en s'assurant qu'ils sont tous dans un format cohérent.

**Pour ajouter un nouveau chemin comme /bonjour, que faut-il modifier dans votre code ? Est-ce que votre structure est facilement extensible ?**

    - Pour ajouter un nouveau chemin comme `/bonjour`, il faut modifier le code pour inclure une nouvelle condition dans la logique de traitement des requêtes. Par exemple, on peut ajouter un bloc `if` pour vérifier si le chemin est `/bonjour` et renvoyer la réponse appropriée.
    - La structure du code doit être conçue de manière à être facilement extensible, par exemple en utilisant des fonctions ou des classes pour gérer les différentes routes et leurs réponses. Cela permet d'ajouter de nouveaux chemins sans avoir à modifier beaucoup de code existant, ce qui facilite la maintenance et l'évolution du serveur.

**Que pourrait-il se passer si un utilisateur tape une URL comme /../../etc/passwd ? Pourquoi est-ce potentiellement dangereux ?**

    - Si un utilisateur tape une URL comme `/../../etc/passwd`, cela peut être dangereux car cela tente d'accéder à un fichier système sensible (dans ce cas, le fichier `passwd` sur un système Unix/Linux). Cela peut entraîner une **vulnérabilité de traversée de répertoire** (directory traversal), où l'utilisateur peut accéder à des fichiers en dehors du répertoire racine du serveur.
    - Pour éviter cela, il est important de valider et de nettoyer les chemins d'URL avant de les traiter. Cela peut inclure la suppression des séquences de traversée de répertoire (`..`) et la restriction des chemins aux ressources autorisées sur le serveur. Utiliser des bibliothèques ou des frameworks qui gèrent ces problèmes de sécurité peut également aider à prévenir les attaques potentielles.

**Est-ce que vous traitez le chemin comme une simple chaîne de caractères, ou comme une ressource contrôlée ? Quelles protections pourriez-vous ajouter pour éviter les comportements inattendus ?**

    - Il est préférable de traiter le chemin comme une ressource contrôlée plutôt que comme une simple chaîne de caractères. Cela signifie que le serveur doit valider et normaliser le chemin avant de l'utiliser pour accéder aux ressources.
    - Pour éviter les comportements inattendus, on peut ajouter plusieurs protections :
        - **Validation des chemins** : Vérifier que le chemin ne contient pas de séquences de traversée de répertoire ou d'autres caractères dangereux.
        - **Liste blanche des chemins autorisés** : Définir une liste de chemins autorisés et rejeter les requêtes qui ne correspondent pas à ces chemins.
        - **Gestion des erreurs** : Fournir des messages d'erreur clairs et sécurisés en cas de requêtes invalides, sans divulguer d'informations sensibles sur la structure du serveur.
        - **Limitation des ressources accessibles** : Restreindre l'accès aux ressources sensibles du système, en s'assurant que seules les ressources nécessaires sont exposées au client.
        - **Utilisation de bibliothèques sécurisées** : Utiliser des bibliothèques ou des frameworks qui gèrent automatiquement ces problèmes de sécurité pour réduire le risque d'erreurs humaines dans la gestion des chemins.


# Partie 2.3

- **Quelle est la ligne exacte reçue par le serveur quand un client appelle /date ? Comment repérez-vous ce chemin ?**

    - La ligne exacte reçue par le serveur quand un client appelle `/date` est généralement de la forme : `GET /date HTTP/1.1`. On repère ce chemin en analysant la ligne de requête HTTP reçue, qui contient la méthode (GET), le chemin (/date) et la version du protocole (HTTP/1.1).

- **Comment déterminez-vous que la requête est terminée ? Quelle est l’utilité de la ligne vide à la fin de la requête ?**

    - La requête est terminée lorsque le serveur reçoit une ligne vide après les en-têtes de la requête. Cette ligne vide indique que les en-têtes sont terminés et que le corps de la requête (s'il y en avait un) commence. L'utilité de cette ligne vide est de signaler au serveur qu'il peut commencer à traiter la requête, car tous les en-têtes nécessaires ont été fournis.

- **Que contient la réponse retournée par votre serveur ? Est-ce que la date change à chaque appel ?**
    - Oui, la date change à chaque appel, car le serveur génère la date et l'heure actuelles au moment de la requête.

- **Quel champ d’entête est indispensable pour que la réponse soit bien comprise par le client ? Que se passe-t-il si vous oubliez Content-Length ?**

    - Le champ d'en-tête indispensable pour que la réponse soit bien comprise par le client est `Content-Type`. Il indique le type de contenu de la réponse (par exemple, `text/plain` pour du texte brut). Si on oublie `Content-Length`, le client peut ne pas savoir combien de données il doit attendre dans le corps de la réponse, ce qui peut entraîner un comportement indéfini, comme l'attente indéfinie de données ou l'affichage incorrect du contenu.

- **Que se passe-t-il si Content-Length est incorrect (trop petit ou trop grand) ? Testez avec curl, telnet, et un navigateur.**

    - Si `Content-Length` est incorrect (trop petit ou trop grand), cela peut entraîner des problèmes lors de la réception de la réponse par le client :
        - Avec **curl**, le client peut afficher un message d'erreur indiquant que la réponse est mal formée ou tronquée.
        - Avec **telnet**, le client peut afficher une partie du contenu, mais il peut également se bloquer en attendant plus de données si `Content-Length` est trop grand.
        - Dans un **navigateur**, le contenu peut ne pas s'afficher correctement, et le navigateur peut afficher un message d'erreur ou une page blanche si `Content-Length` est incorrect.
    - En général, les clients HTTP s'attendent à ce que `Content-Length` corresponde exactement à la taille du corps de la réponse, et toute incohérence peut entraîner des erreurs ou un comportement inattendu.


- **Le corps de votre réponse contient-il des caractères spéciaux ou des retours à la ligne (\n) ? Comment sont-ils affichés selon le client utilisé ?**

    - Le corps de la réponse peut contenir des caractères spéciaux ou des retours à la ligne (`\n`). 
    - Dans **curl**, les retours à la ligne sont généralement affichés correctement, car curl traite le texte brut et affiche les caractères spéciaux tels quels.
    - Dans **telnet**, les retours à la ligne peuvent également être affichés correctement, mais cela dépend de la configuration du terminal utilisé.
    - Dans un **navigateur**, les retours à la ligne peuvent être interprétés différemment. Par exemple, si le contenu est du texte brut, les retours à la ligne seront affichés comme des sauts de ligne. Si le contenu est du HTML, les retours à la ligne peuvent être ignorés ou traités différemment en fonction des balises HTML utilisées.
    - Il est important de s'assurer que le contenu est correctement formaté pour chaque type de client afin d'assurer une expérience utilisateur cohérente.

- **Que renvoie votre serveur si un autre chemin est demandé, par exemple/time ou /now ? Est-ce prévu ? Que se passe-t-il ?**

    - Si un autre chemin est demandé, comme `/time` ou `/now`, le serveur peut renvoyer une erreur 404 Not Found si ces chemins ne sont pas prévus dans la logique de traitement des requêtes. 
    - Si ces chemins sont prévus, le serveur peut renvoyer une réponse appropriée avec la date et l'heure actuelles ou un message indiquant que la ressource est disponible.
    - Si ce n'est pas prévu, le comportement dépend de la configuration du serveur. Il peut renvoyer une page d'erreur générique ou un message indiquant que la ressource n'est pas disponible. Il est important de gérer ces cas pour éviter les comportements inattendus et fournir une expérience utilisateur cohérente.

- **Est-ce que le serveur répond de manière fiable même si deux clients se connectent successivement ? Et en même temps ?**

    - Oui, le serveur doit répondre de manière fiable même si deux clients se connectent successivement ou en même temps. 
    - Pour les connexions successives, le serveur traite chaque requête indépendamment, en générant une réponse pour chaque client sans interférence.
    - Pour les connexions simultanées, le serveur doit être capable de gérer plusieurs requêtes en parallèle. Cela peut être réalisé en utilisant des threads, des processus ou des mécanismes d'asynchrone pour traiter chaque requête dans son propre contexte d'exécution. 
    - Si le serveur est correctement configuré pour gérer la concurrence, il devrait répondre de manière fiable à toutes les requêtes, quelle que soit la charge ou le nombre de clients connectés simultanément.

- **Pourriez-vous ajouter un autre chemin dynamique (comme /uptime) ? Quelles informations pourraient être utiles à afficher ?**

    - Oui, il est possible d'ajouter un autre chemin dynamique comme `/uptime`. Pour ce faire, il suffit d'ajouter une nouvelle condition dans la logique de traitement des requêtes pour vérifier si le chemin demandé est `/uptime` et renvoyer les informations appropriées.
    - Les informations utiles à afficher pour `/uptime` pourraient inclure :
        - Le temps écoulé depuis le dernier redémarrage du serveur.
        - La charge actuelle du serveur (par exemple, le nombre de requêtes en cours de traitement).
        - Des statistiques sur les performances du serveur, comme le nombre de requêtes traitées depuis le démarrage.
        - Des informations sur l'état du serveur, comme la mémoire utilisée et disponible.
    - Ces informations peuvent aider les administrateurs à surveiller la santé et les performances du serveur.

- **Que faudrait-il faire pour rendre ce serveur un peu plus “propre” ou modulaire ? Est-ce que le code pourrait être réorganisé pour gérer plusieurs routes dynamiques plus facilement ?**

    - On pourrait déjà créer une fonction pour gérer les routes dynamiques, ce qui permettrait de centraliser la logique de traitement des requêtes. Par exemple, on pourrait avoir une fonction `handle_request(path)` qui prend le chemin en paramètre et renvoie la réponse appropriée en fonction du chemin demandé.
    - On pourrait également utiliser un dictionnaire ou une table de hachage pour mapper les chemins aux fonctions de traitement correspondantes, ce qui permettrait d'ajouter facilement de nouvelles routes sans modifier la logique principale du serveur.
    - En outre, on pourrait organiser le code en modules ou en classes pour séparer les différentes responsabilités, comme la gestion des requêtes, la génération des réponses et la configuration du serveur. Cela rendrait le code plus lisible, maintenable et extensible.

