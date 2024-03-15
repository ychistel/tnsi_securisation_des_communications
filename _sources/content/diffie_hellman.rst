
Méthode de Diffie-Hellman
=========================

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

#. Alice et Bob se mettent d'accord sur des paramètres publics communs (générateur et nombre premier).
#. Alice dispose d'une clé privée secrète (a). Bob dispose d'une clé privée secrète (b).
#. Alice crée avec une clé publique (A) avec sa clef privée :math:`a` et les paramètres communs publics. Bob crée avec une clé publique (B) avec sa clef privée :math:`b` et les paramètres communs publics.

#. Alice et Bob échangent leurs clés publiques.

#. Alice crée avec sa clef privée :math:`a` et la clé publique de Bob :math:`B` une clé de chiffrement :math:`K_{A}`.

   Bob crée avec sa clef privée :math:`b` et la clé publique d'Alice :math:`A` une clé de chiffement :math:`K_{B}`.

#. En fait :math:`K_{A}=K_{B}=K`. Donc, Alice et Bob sont en possession d'une clé de chiffrement commune dite clé partagée. 

#. Disposant de la même clé :math:`K`, ils peuvent communiquer des messages avec un **chiffrement symétrique**.

.. rubric:: Analogie des pots de peinture
   :name: analogie-des-pots-de-peinture

Pour comprendre la méthode de Diffie-Hellman, on la compare au mélange de couleurs de pots de peinture.

-  Une couleur publique commune est choisie, par exemple un jaune.
-  Alice choisit une couleur privée, par exemple du bleu. Bob choisit aussi une couleur privée, par exemple du vert.
-  Alice mélange la couleur publique (jaune) avec sa couleur privée (bleu) et on obtient un premier mélange vert kaki.
-  De son côté, Bob mélange la couleur publique (jaune) avec sa couleur privée (vert) et on obtient un mélange vert pistache.
-  Alice et Bob échangent leurs mélanges de couleur. 
-  Alice mélange alors le vert pistache envoyé par Bob avec sa couleur privée bleu et Bob de son côté mélange le vert kaki envoyé par Alice avec sa couleur privée vert.
-  Après mélange, Alice et Bob dispose de la même couleur!

Le mélange des trois couleurs donnera la clef commune finale pour le chiffrement symétrique. La robustesse de la méthode s'explique par le fait que lorsqu'on connaît le mélange de 2 couleurs et l'une des 2
couleurs, il est quasi impossible de retouver exactement la seconde couleur qui a servi à fabriquer le mélange. Seule la multiplication des essais permettrait d'y parvenir.

.. image:: ../img/diffie_hellman_couleurs.svg
   :alt: diffie_hellman_couleurs.svg
   :align: center
   :width: 600px
