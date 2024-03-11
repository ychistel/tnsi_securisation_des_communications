# coding: utf-8

##
## Exercice 24 du chapitre 10 (Chiffrement par permutation)
##

# Question a
print(chr(ord("A")+0))
print(chr(ord("A")+25))

# On crée une liste alphabet, initialement vide, contenant toutes
# les lettres majuscules de A à Z.
alphabet = []
for i in range(26):
    alphabet.append(...) # À COMPLÉTER
print(alphabet)


# Question b
import random
random.shuffle(alphabet)
print(alphabet)

# On définit une fonction qui crée l'alphabet comme à la question a
# et le renvoie ainsi que l'alphabet permuté.
def creer_alphabet_permute():
    # Création de l'alphabet comme à la question a
    alphabet = []
    for i in range(26):
        alphabet.append(...) # À COMPLÉTER       
    # Cette instruction permet de copier la liste alphabet pour ne
    # pas la modifier en place.
    alphabet_permute = list(alphabet)
    # On permute alors la nouvelle liste.
    # À COMPLÉTER
    # On renvoie finalement les deux alphabets.
    return(alphabet,alphabet_permute)


# Question c

# On commence par créer les deux alphabets grâce à la fonction précédente.
alphabet, alphabet_permute = creer_alphabet_permute()

# On crée les deux dictionnaires.
dictionnaire_chiffrement = {}
dictionnaire_dechiffrement = {}
for i in range(26):
	dictionnaire_chiffrement[alphabet[i]] = ... # À COMPLÉTER
	dictionnaire_dechiffrement[alphabet_permute[i]] = ... # À COMPLÉTER


# Question d

print(dictionnaire_chiffrement.get("A","A"))
print(dictionnaire_chiffrement.get("a","a"))

# On utilise ce résultat pour chiffrer uniquement les lettres majuscules
# non accentuées.
def chiffrement(message):
    # On initialise message_chiffre à la chaîne vide.
    message_chiffre = ""
    # Pour chaque caractère du message, on le remplace par la valeur
    # correspondante dans dictionnaire_chiffrement si c'est une lettre
    # majuscule non accentuée.
    for c in message:
        message_chiffre += ... # À COMPLÉTER
    return(message_chiffre)

# Pour le déchiffrement, la méthode est identique en utilisant cette fois-ci
# le dictionnaire de déchiffrement.
def dechiffrement(chiffre):
    message = ""
    for c in chiffre:
        message += ...  # À COMPLÉTER
    return(message)

print(chiffrement("BIENVENUE, C'EST L'ETE"))
# print(dechiffrement(...)) # À COMPLÉTER AVEC LE RÉSULTAT AFFICHÉ
