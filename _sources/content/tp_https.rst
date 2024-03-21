

Protocole https
---------------

Le protocole HTTPS est l'association du protocole HTTP et du PROTOCOLE SSL/TLS.

-  Le protocole HTTP assure l'acheminement des données entre un client et un serveur. Cette transmission de données est basée sur des requêtes selon les méthodes GET ou POST.
-  Le protocole TLS assure le chiffrement des données pour qu'elles ne soient pas lisibles et l'échange de certificats pour s'assurer de la bonne identité du client et du serveur.

Il est possible de mettre en place sur une même machine un serveur WEB et un client pour observer les requêtes du protocole HTTP et même du protocole HTTPS.

.. rubric:: Travail préparatoire

#. Dans Thonny, vous devez vous assurer de la présence du module ``flask`` qui permet de créer un serveur WEB et du module ``pyopenssl`` qui se charge du chiffrement et des certificats du protocole TLS.
#. Créer un dossier de travail ``protocole`` contenant les dossiers ``templates`` et ``static``.

.. rubric:: Premier serveur web

#. Créer un fichier Python ``serveur.py`` contenant le code suivant:

   .. literalinclude:: ../python/serveur_ssl.py
      :linenos:

#. Exécuter le fichier ``serveur.py`` puis ouvrez l'url ``http://localhost:5000/`` dans un navigateur.

.. rubric:: Ajouter un fichier HTML

#. Créer, dans le dossier ``templates``, une page WEB ``index.html`` contenant un titre de niveau 1 etun petit paragraphe.
#. Modifier la ligne 9 du fichier Python ``serveur.py`` par la ligne suivante:

   .. code-block:: python

      return render_template("index.html")

.. rubric:: Protocole TLS

Le module Flask prend en charge des certificats créés à la volée pour créer rapidement une connexion HTTPS.

#. Ajouter en dernière ligne le paramètre ``ssl_context='adhoc'`` pour ajouter un protocole TLS au protocole HTTP:

   .. code-block:: python

      app.run(ssl_context='adhoc', debug=True)

#. Relancez votre serveur si nécessaire et actualiser votre page WEB. Attention, on a changé de protocole. Si tout se passe normalement, vous obtenez :

   .. image:: ../img/url_non_securise.png
      :align: center

   .. image:: ../img/risque_securite.png
      :align: center
      :width: 500

   Cliquez sur le bouton ``Avancé...`` puis sur le bouton ``Accepter le risque et poursuivre``.

#. Afficher et identifier votre certificat en donnant le nom du sujet, la validité et l'algorithme de chiffrement.

.. rubric:: Ajouter son certificat

Lorsqu'on développe un serveur WEB, il est nécessaire d'avoir son propre certificat. On doit en faire la demande auprès d'une autorité de certification. Comment faire pour créer un certificat et faire des tests ? On crée un certificat dit **auto-signé** avec ``openssl``.

#. Avec ``openssl``, créer une paire de clefs privée et publique (attention au chemin du dossier):

   .. code-block:: bash

      openssl genrsa -out key.pem 4096

#. Avec la paire de clefs créée, créer un certificat en utilisant la commande suivante:

   .. code-block:: bash

      openssl req -new -x509 -days 365 -key key.pem -out cert.pem

#. Actualiser le navigateur et vérifier que le certificat utilisé est bien celui créé précédemment.