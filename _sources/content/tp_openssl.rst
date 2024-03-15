TP : openssl
==============

**OpenSSL** est un logiciel de cryptographie qui possède de nombreux algorithmes de chiffrement. OpenSSL est disponible sur les systèmes **windows/linux/mac** et s'utilise en ligne de commandes.

L'encodage d'un fichier peut se réaliser avec différents algorithmes. Un algorithme assez répandu est **base64**. Voici les commandes à utiliser.

.. rubric:: Pour encoder

.. code:: bash

   openssl enc -base64 -in mon-fichier.txt
   openssl enc -base64 -in mon-fichier.txt -out mon-fichier-encode.txt

.. rubric:: Pour décoder

.. code:: bash

   openssl enc -d -base64 -in mon-fichier.txt
   openssl enc -d -base64 -in mon-fichier-encode.txt -out nouveau-fichier.txt

Le chiffrement symétrique d'un fichier est réalisable avec openssl. Un mot de passe est alors demandé pour chiffrer et déchiffré un fichier. Openssl contient de nombreux algorithmes de chiffrement. On utilisera ici l'algorithme ``des3``.

.. rubric:: Pour chiffrer avec un algorithme DES symétrique

.. code:: bash

   openssl enc -des3 -in fichier_clair
   openssl enc -des3 -in fichier_clair -out fichier_chiffre

.. rubric:: Pour déchiffrer avec un algorithme DES symétrique

.. code:: bash

   openssl enc -des3 -d -in fichier_chiffre
   openssl enc -des3 -d -in fichier_chiffre -out nouveau_fichier_clair

.. important::

   L'encodage n'est pas un chiffrement. C'est transformer un contenu en l'écrivant avec un autre codage de caractères, dans un format particulier.

Encoder un fichier
------------------

#. Créer un fichier texte contenant un message court.
#. Encoder votre message avec l’algorithme **base64** puis envoyer le à un camarade pour qu’il le déchiffre.

Encoder une image
-----------------

Sur le web, dans le code source des pages html, il arrive d’avoir des images encodées avec l’algorithme **base64**. La source de l’image située dans la balise ``img`` de la page html ne contient pas une url mais le code encodé avec l’algorithme base64.


#. Créer une page html contenant une image au format jpg:

   .. code:: html

      <!Doctype html>
      <html lang="fr">
      <body> 
      <img src='chemin/vers/mon/image' />
      </body>
      </html>

#. Encoder votre image avec **openssl** en utilisant l’algorithme base64.

#. Copier et coller votre code (image encodée) dans votre page web en remplaçant l'url de l'image par l'encodage comme ci-dessous:

   .. code:: html

      <!Doctype html>
      <html lang="fr">
      <body> 
      <img src='data:image/jpg;base64, image-encodée-base64' />
      </body>
      </html>

Chiffrement symétrique
----------------------

#. Encoder votre message avec l'algorithme **des3** en utilisant le mot de passe *encoder*. Vous enregistrerez le fichier chiffré sous le nom `message.des3`. 
#. Pour finir, déchiffrez votre message sans l'enregistrer dans un fichier mais en le visualisant à l'écran.
#. Chiffrer une image en l'enregistrant au format ``jpg`` et afficher son contenu. Déchiffrer l'image chiffrée et vérifier son contenu.