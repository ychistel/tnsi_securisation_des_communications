Chiffrement de Vernam
=====================

Le chiffrement de Vernam, aussi appelé **masque jetable**, consiste à combiner un message avec une clé de chiffrement en respectant les propriétés suivantes:

-  la clé de chiffrement est aussi longue que le message à chiffrer;
-  la clé est choisie de façon aléatoire;
-  chaque clé n'est utilisée qu'une seule fois d'où le nom de masque jetable.

Ce chiffrement s'applique sur des données en binaire et utilise l'opérateur binaire ``xor`` qui se note :math:`\oplus` et dont voici la table de vérité.

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

#.  On considère le message ``m = 0110`` à chiffrer avec la clé ``k = 1100``.

    a. Le chiffrement de Vernam peut-il s'appliquer ?
    b. En utilisant l'opérateur binaire ``xor`` bit à bit entre le message ``m`` et la clé ``k``, donner la valeur binaire du message chiffré ``c``.

#.  Chaque lettre est encodée en binaire avec la norme unicode. Les caractères ASCII sont encodés sur 1 octet. On en donne souvent une représentation hexadécimale.

    a. Donner l'encodage binaire sur 3 octets du mot **NSI**.
    b. Chiffrer le mot **NSI** en utilisant une clé ``k=0101...01`` constituée des bits 0 et 1 en alternance sur 3 octets.
    c. Retrouver les caractères associés au message chiffré.

#.  L'opérateur ``xor`` vérifie la propriété suivante: si :math:`m \oplus k = c` alors :math:`c \oplus k = m`. Vérifier dans les différents chiffrements réalisés précédemment que l'on retrouve le message initial ``m`` à partir du message ``chiffré``.

#.  En Python, l'opérateur ``xor`` est noté par le l'accent circonflexe et s'applique à des nombres entiers. Par conséquent, pour appliquer cet opérateur logique entre deux valeurs, une conversion de la valeur binaire en valeur décimale est nécessaire.

    a.  Calculer dans l'interpréteur Python ``25 ^ 17``. Vérifier en binaire la valeur obtenue.
    b.  Chaque lettre est représentée par une valeur décimale associée à son encodage binaire. Retrouver les valeurs décimales associées aux lettres du mot NSI et vérifier en Python le mot chiffré obtenu.

