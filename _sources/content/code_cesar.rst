Code César
==========

On étudie une méthode de chiffrement de chaines de caractères alphabétiques. Cette méthode de chiffrement est appelée *code de César*. On considère que les messages ne contiennent que les lettres capitales de l’alphabet `ABCDEFGHIJKLMNOPQRSTUVWXYZ` et la méthode de chiffrement utilise un nombre entier fixé appelé clef de chiffrement.

Soit la classe `CodeCesar` définie ci-dessous:

.. code:: python

   class CodeCesar:
         
         def __init__(self,cle):
            self.cle = cle
            self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
         
         def decale(self, lettre):
            """
            La méthode renvoie une lettre issue de l'alphabet.
            Cette lettre est obtenue à partir de la lettre passée en argument après un décalage égal à la valeur de la clé de chiffrement.
            Variables:
            - num_1 est la position de la lettre passée en argument dans l'alphabet
            - num_2 est la position de la lettre chiffrée après ajout de la clé
            - nouvelle_lettre est la lettre chiffrée renvoyée par la fonction; il faut tenir compte de la position de la lettre qui peut être supérieur au nombre de lettres de l'alphabet.
            Par exemple, si la lettre passée en argument est "Y" alors num_1 = 24. Si la clé vaut 5 alors num_2 = 29 ce qui ne correspond pas à une lettre de l'alphabet!
            """ 
            num_1 = ...
            num_2 = num_1 + ...
            if num_2 ...:
               num_2 = ...
            nouvelle_lettre = self.alphabet[...]
            return nouvelle_lettre
            
On rappelle que la méthode ``str.find(lettre)`` renvoie l'indice (index) de la ``lettre`` dans la chaine de caractères ``str``.
   
#. Représenter le résultat de l'exécution du code Python suivant:

   >>> code_1 = CodeCesar(3)
   >>> print(code_1.decale('C'))
   >>> print(code_1.decale('X'))       

#. La méthode de chiffrement du code César consiste à décaler les lettres du message dans l'alphabet selon un nombre de rangs fixé par la clef de chiffrement. Par exemple, avec la clef 3, toutes les lettres sont décalées de 3 rangs vers la droite : le A devient le D, le B devient le E, etc.

   Compléter le code de la méthode ``decale`` et tester son bon fonctionnement.

#. Ajouter la méthode ``chiffrer(self, texte)`` dans la classe ``CodeCesar`` définie à la question précédente, qui reçoit en paramètre une chaîne de caractères (le message à chiffrer) et qui retourne une chaîne de caractères (le message crypté).

   Cette méthode ``chiffrer(self, texte)`` doit chiffrer la chaîne texte avec la clef de l'objet de la classe ``CodeCesar`` qui a été instancié.

   .. admonition:: Exemple

      >>> code_1 = CodeCesar(3)
      >>> code_1.chiffrer('NSI')
      'QVL'   

#. Écrire un programme qui:

   -  demande de saisir la clef de chiffrement
   -  crée un objet de classe CodeCesar
   -  demande de saisir un texte à chiffrer
   -  affiche le texte chiffré en appelant la méthode ``chiffrer``
.

#. On ajoute la méthode ``transforme(texte)`` à la classe ``CodeCesar``:

   .. code:: python

      def transforme(self, texte):
          self.cle = - self.cle
          message = self.chiffrer(texte)
          self.cle = - self.cle
          return message  

   On exécute la ligne suivante : ``print(CodeCesar(10).transforme("PSX"))``

   Que va-t-il s’afficher ? Expliquer votre réponse.

.. note::
   
   La robustesse de cette méthode de chiffrement est très faible. Il est possible de tester toutes les clés possibles pour déchiffrer un message en sachant qu'il existe 26 clés différentes !
