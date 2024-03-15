TP : Cryptographie RSA
======================

**OpenSSL** est un logiciel de cryptographie qui possède de nombreux algorithmes de chiffrement. OpenSSL est disponible sur les systèmes **windows/linux/mac** et s'utilise en ligne de commandes.

Nous allons dans cette activité utiliser la machine virtuelle UBUNTU pour :

-  créer une paire de clés RSA;
-  signer un message
-  chiffre et déchiffrer un message

Créer une paire de clé RSA
--------------------------

#. Ouvrir un terminal.
#. Créer votre paire de clés en saisissant la commande suivante:

   .. code-block:: bash
   
      # Création des clés RSA
      openssl genrsa -out cle.prv 2048

#. Afficher la clé générée avec la commande:

   .. code-block:: bash

      cat cle.prv

#. La clé créée contient la clé privée **et** la clé publique. Il faut extraire la clé publique en saisissant la commande suivante en remplaçant ``prenom`` par votre prénom:

   .. code-block:: bash

      # Sauvegarder la clé dans un fichier
      openssl rsa -in cle.prv -pubout -out cle_prenom.pub

#. Lister votre dossier et vérifier la présence des fichiers ``cle.prv`` et ``cle_prenom.pub`` contenant les clés avec la commande :

   .. code-block:: bash

      ls

#. Afficher votre clé publique avec la commande suivante en remplaçant ``prenom`` par votre prénom:

   .. code-block:: bash

      cat cle_prenom.pub

#. Envoyer votre **clé publique** à votre partenaire de binôme en utilisant la messagerie de l'ENT.
#. Récupérer la **clé publique** de votre partenaire de binôme et l'enregistrer dans le dossier qui contient vos clés.

.. warning::

   On vient de créer notre paire de clés RSA. La clé privée est **secrète** et ne doit pas être communiquée.

Signer un fichier
-----------------

Maintenant que nos clés sont créées, on peut **signer** des messages. Cela permet d'authentifier la source d'un message.

#. Créer dans un éditeur de texte un court message. Enregistrer ce message dans un fichier nommé ``message.txt`` dans le même dossier que vos clés.
#. Signer le fichier qui contient votre message avec votre clé privée en saisissant la commande suivante en remplaçant ``prenom`` par votre prénom :

   .. code-block:: bash

      # Signer un fichier avec sa clé privée
      openssl rsautl -sign -inkey cle.prv -in message.txt -out message_prenom_signe
   
   Afficher le message signé et vérifier qu'il n'est pas compréhensible.

#. Envoyer via la messagerie de l'ENT votre message signé à votre binôme. 
#. Récupérer le message signé par votre binôme et l'enregistrer dans le dossier contenant vos clés.
#. On va maintenant vérifier la **signature** du message signé. Seule la clé publique de la source du message peut le déchiffrer. Saisir la commande suivante :

   .. code-block:: bash

      # Vérifier la signature avec une clé publique
      openssl rsautl -verify -pubin -inkey cle.pub -in message_prenom_signe

   Si le message s'affiche en clair alors, vous avez l'assurance qu'il provient de votre binôme qui est le seul à pouvoir le signer avec sa clé privée.
      
Chiffrer un message
---------------------

On va communiquer en chiffrant des messages. 

#. Reprendre le message en clair ``message.txt``.
#. Chiffrer ce message avec la clé publique de votre binôme en saisissant la commande:

   .. code-block:: bash
      
      # Chiffrer un message sauvegardé dans un fichier
      openssl rsautl -encrypt -pubin -inkey cle_prenom.pub -in message.txt -out message_chiffre

   Afficher le message chiffré et vérifier qu'il n'est pas compréhensible.
   
#. Envoyer à votre binôme le message chiffré et récupérer son message chiffré en l'enregistrant dans le dossier qui contient vos clés.
#. Déchiffrer le message avec votre clé privé en saisissant la commande :

   .. code-block:: bash
      
      # Déchiffrer un fichier sans sauvegarde
      openssl rsautl -decrypt -inkey cle.prv -in message_chiffre

#. Recommencer l'échange de messages chiffrés avec une image de votre choix.
