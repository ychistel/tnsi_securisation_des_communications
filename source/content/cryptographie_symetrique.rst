La cryptographie symétrique
===========================

La méhode de chiffrement symétrique utilise une clef qui est la même pour le **chiffrement** et le **déchiffrement**.

Les chiffrements par le code César et par le code Vigenère sont symétriques.

.. admonition:: Propriété
   :class: propriete

   La cryptographie symétrique utilise deux fonctions :

   -  une fonction de chiffrement :math:`C(m,k)` qui prend en argument un message **m** et une clef de chiffrement **k** et renvoie un message chiffré **c**.
   -  une fonction de déchiffrement :math:`D(c,k)` qui prend en argument un message chiffré **c** et la clef de chiffrement :math:`k` et renvoie le message déchiffré **m**.

Chiffrement de Vernam
---------------------

.. admonition:: Méthode
   :class: methode

   Le chiffrement de Vernam, aussi appelé **masque jetable**, consiste à combiner un message avec une clé de chiffrement en respectant les propriétés suivantes:

   - la clé de chiffrement est aussi longue que le message à chiffrer;
   - la clé est choisie de façon aléatoire;
   - chaque clé n'est utilisée qu'une seule fois d'où le nom de masque jetable.

Le chiffrement de Vernam est un chiffrement symétrique puisqu'on utilise la même clé pour chiffrer et déchiffrer le message. 

Si on chiffre numériquement un message avec le chiffement de Vernam, on utilise la fonction logique ``XOR`` appelée **ou exclusif**.

.. rubric:: Chiffrement par XOR

Le **ou exclusif** ou **XOR** est un opérateur logique noté :math:`\oplus`. La table de vérité est:

.. table:: table de vérité de XOR
   :widths: auto
   :align: center

   = = ===================
   X Y X :math:`\oplus`\ Y
   = = ===================
   0 0         0
   0 1         1
   1 0         1
   1 1         0
   = = ===================

Une propriété intéressante de l'opérateur **XOR** est qu'il est réversible: si :math:`m \oplus k = c` alors :math:`c \oplus k = m`.

Cette propriété permet alors de déchiffrer un message en utilisant la même clé de chiffrement:

.. figure:: ../img/msg_chiffre_1.png
   :alt: msg_chiffre_1.png
   :align: center

.. admonition:: Exemple

   La lettre S a pour code décimal :math:`83` dans la table ASCII ou UNICODE soit :math:`0101 0011` en binaire;

   La lettre P a pour code décimal :math:`80` dans la table ASCII ou UNICODE soit :math:`0101 0000` en binaire;

   La valeur :math:`83 \oplus 80 = 0101 0011 \oplus 0101 0000` ce qui donne, bit à bit :math:`0000 0011` soit 3 en décimal:

   .. image:: ../img/ou_exclusif_2.png
      :alt: ou_exclusif_2.png
      :align: center

   Le caractère obtenu est non imprimable et a pour valeur décimale :math:`3`.

.. rubric:: Opérateur XOR en Python

En Python cet opérateur est noté par le circonflexe et s'applique à des nombres entiers. Par conséquent, pour appliquer cet opérateur logique entre deux valeurs, une conversion de la valeur en décimal est nécessaire.

-  Lorsque les valeurs sont nombres entiers, l'opérateur s'applique directement : 3 ^ 4.
-  Lorsque les valeurs sont des caractères quelconques, une conversion du caractère en valeur décimale est nécessaire. Ensuite, le résultat décimal pourra être transformé en caractère. Cela est alors équivalent à l'opération logique XOR avec les écritures binaires.

Faiblesse de la cryptographie symétrique
----------------------------------------

.. rubric:: Chiffrement de Vernam

Le chiffrement de Vernam est très robuste et impossible à déchiffrer en théorie si les conditions sont bien respectées : clef de chiffrement est aussi longue que le message à chiffrer et utilisée une seule fois. 

En pratique cela n'est pas possible ! En effet, il faut utiliser la clé une seule fois, cela implique de transmettre une nouvelle clé à chaque nouveau message. Conclusion, autant donner le message directement.

.. rubric:: Faiblesse

Le principal problème de la cryptographie symétrique est la transmission de la clef de chiffrement qui est utilisée pour chiffrer et déchiffrer le message. Cela implique, à un instant donné, de transmettre la clef et donc un risque d'interception.

C'est un obstacle qui a été surmonté en utilisant un autre système de cryptographie qui permet de transmettre une clé pour effectuer un chiffrement symétrique.
