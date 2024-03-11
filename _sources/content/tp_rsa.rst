TP : Cryptographie RSA
======================

**OpenSSL** est un logiciel de cryptographie qui possède de nombreux algorithmes de chiffrement. OpenSSL est disponible sur les systèmes **windows/linux/mac** et s’utilise en ligne de commandes.

Voici les commandes que nous allons utiliser:

.. rubric:: Générer des clés RSA

La clé générée est la clé privée. Elle contient des informations sur la clé dont la clé publique.

.. code:: bash

   # Sans les sauvegarder dans un fichier
   openssl genrsa 2048
   # Sauvegarde dans un fichier (attention au chemin)
   openssl genrsa -out cle.prv 2048
   # Clé protégée par un mot de passe
   openssl genrsa -des3 -out cle.prv 2048

.. rubric:: Afficher sa clé (privée)

.. code:: bash

   openssl rsa -in cle.prv
   # ou
   openssl rsa -in cle.prv -text -noout
   
.. rubric:: Extraire la clé publique

.. code:: bash

   # Sans la sauvegarder dans un fichier
   openssl rsa -in cle.prv -pubout
   # Sauvegarder la clé dans un fichier
   openssl rsa -in cle.prv -pubout -out cle.pub

.. rubric:: Chiffrer un message avec la clé publique

.. code:: bash

   # Chiffrer un message sans sauvegarde
   openssl rsautl -encrypt -pubin -inkey cle.pub -in fichier_clair
   # Chiffrer un message sauvegardé dans un fichier
   openssl rsautl -encrypt -pubin -inkey cle.pub -in fichier_clair -out fichier_chiffre

.. rubric:: Déchiffrer un message avec la clé privée

.. code:: bash

   # Déchiffrer un fichier sans sauvegarde
   openssl rsautl -decrypt -inkey cle.prv -in fichier_chiffre
   # Déchiffrer un fichier sauvegardé dans un fichier
   openssl rsautl -decrypt -inkey cle.prv -in fichier_chiffre -out nouveau_fichier_clair

.. rubric:: Signer et vérifier un fichier

.. code:: bash

   # Signer un fichier avec la clé privée
   openssl rsautl -sign -inkey cle.prv -in fichier_clair -out fichier_signe
   # Vérifier la signature avec la clé publique
   openssl rsautl -verify -pubin -inkey cle.pub -in fichier_signe -out nouveau_fichier_clair

Chiffrer un message
---------------------

Il est préférable de travailler en binôme et d'échager ses clés publiques. La clé privée doit rester secrète.

#. Générer une paire de clés RSA. Elles seront enregistrées dans le fichier ``cle_prenom.prv``.
#. Afficher la clé publique et l'enregistrer dans le fichier ``cle_prenom.pub``. Échanger vos clés publiques avec votre partenaire de binôme.
#. Créer un message en clair puis chiffrez-le avec la clé publique de votre partenaire. Donner à votre partenaire le message chiffré pour qu'il le déchiffre.
#. Recommencer avec une image de votre choix.

Signer un fichier
-----------------

#. Créer un fichier contenant un texte court et une image.
#. Signer votre fichier avec votre clé privée puis transméttez le fichier et sa signature à votre partenaire.
#. Vous avez reçu un fichier et sa signature.

   a. Déchiffrer la signature.
   b. Comparer le fichier reçu et sa signature. 

      La commande ``diff fichier_1 fichier_2`` permet de comparer 2 fichiers. Si rien ne s'affiche, ils sont identiques, sinon les différences sont affichées.