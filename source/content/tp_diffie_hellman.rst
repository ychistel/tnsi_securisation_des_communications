TP : Méthode Diffie - Hellman
=============================

La méthode repose sur des calculs mathématiques liés au logarithme discret.

On se place dans la situation où 2 personnes, Alice et Bob, souhaitent sécuriser leurs échanges en utilisant une clé de chiffrement commune appelée clé partagée. 

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
