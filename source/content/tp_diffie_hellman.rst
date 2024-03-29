TP : Méthode Diffie - Hellman
=============================

La méthode consiste à fabriquer une clef de chiffrement symétrique en utilisant un canal de communication non sécurisé. Lors d'une communication chiffrée entre 2 participants:

-  Chaque participant dispose d'une clef privée secrète;
-  Chaque participant crée avec sa clé privée et des paramètres communs une clef publique;
-  Les participants échangent leurs clefs publiques;
-  Chaque participant construit une clé secrète qui sera utilisée pour le chiffrement symétrique de la communication.

.. hint::

   La clef de chiffrement symétrique fabriquée par chaque participant est la même. Cela résulte de calculs mathématiques utilisant des nombres premiers.

Alice et Bob souhaitent communiquer en chiffrant leur message. Ils commencent par construire une clef symétrique avec la méthode de Diffie-Hellman. Cela se déroule en plusieurs étapes:

.. image:: ../img/diffie-hellman.svg
   :align: center
   :width: 500px

- Alice et Bob choisissent en commun 2 nombres :math:`g` et :math:`p`.
- Alice choisit un nombre secret appelé :math:`a`.
- Bob choisit un nombre secret appelé :math:`b`.

Calcul d'une clé de chiffrement commune
---------------------------------------

Pour la suite du TP, on décide de fixer :math:`g = 2` et :math:`p = 19`.

#. Alice choisit pour valeur secrète le nombre :math:`a = 11`. Elle crée sa clé publique A en effectuant le calcul : :math:`A = g^a ~\%~ p`. Quelle est la valeur de A ?
#. Bob choisit pour valeur secrète le nombre :math:`b = 13`. Calculer la valeur de la clé publique B de Bob.
#. Bob envoie sa clé publique B à Alice. Avec sa clé secrète, Alice calcule la clé de chiffrement K avec la relation :math:`K = B^a ~\%~ p`. Calculer la valeur de K.
#. Bob reçoit la clé publique A d'Alice et calcule aussi la clé de chiffrement K. Vérifier que Bob a la même clé de chiffrement qu'Alice.
#. Recommencer en utilisant des valeurs différentes pour :math:`g`, :math:`p`, :math:`a` et :math:`b`.

Méthode Diffie - Hellman en Python
----------------------------------

Avec ce partage de clés entre Alice et Bob, ils sont en capacité de chiffrer leur communication. La clé partagée étant la même, on utilise la cryptographie symétrique.

Le fichier Python ``diffie_hellman.py`` permet de reproduire le calcul des clés et l'échange de messages chiffrés. Ce fichier est à récupérer sur l'ENT.

On rappelle que la fonction python ``pow`` calcule des puissances : ``pow(a,b)`` est égal à :math:`a^b`.

#. Il est possible d'utiliser un troisième paramètre avec la fonction ``pow``. Rechercher en quoi il modifie le calcul.
#. Compléter les fonctions ``cle_publique(g,p,x)`` et ``cle_chiffrement_partage(x,p,X)`` sur le fichier Python.

#.  Le programme principal permet d'effectuer un échange de messages en le chiffrant avec la clé partagée. Compléter ce programme et tester l'échange de messages.
