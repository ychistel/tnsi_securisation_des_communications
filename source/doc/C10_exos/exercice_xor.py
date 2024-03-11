# coding: utf-8

##
## Exercice 26 du chapitre 10 (Chiffrement XOR (2))
##

# Question a
message = "abc"
clef = "def"
print(ord(message[0])^ord(clef[0]))

# Question b
# On utilise l'instruction de la question précédente pour chiffrer 
# chaque caractère du message à l'aide de chaque caractère de 
# la clef (supposée assez longue).
def chiffrement_xor(message,clef):
    # On initialise la liste qui va contenir les codes des caractères 
    # chiffrés.
    c = []
    n = len(message)
    # On chiffre chaque caractère du message. 
    for i in range(n):
        c.append(...) # À COMPLÉTER
    return(c)

# Pour le déchiffrement, le message chiffré est une liste de codes,
# on n'utilise donc ord que pour les caractères de la clef. 
# On utilise ensuite chr pour récupérer le caractère.
def dechiffrement_xor(message_chiffre,clef):
    # On initialise la chaîne de caractères qui va contenir le message
    # déchiffré.
    m = ""
    n = len(message_chiffre)
    # On déchiffre chaque caractère du message. 
    for i in range(n):
        m = m + ... # À COMPLÉTER
    return(m)

# Question c

# La clef n'étant plus assez longue, il est nécessaire de la répéter.
def chiffrement_xor_vigenere(message,clef):
    # On initialise la liste qui va contenir les codes des caractères 
    # chiffrés.
    c = []
    n = len(message)
    k = len(clef)
    j = 0
    # On chiffre chaque caractère i du message avec le caractère j de la clef. 
    for i in range(n):
        c.append(...) # À COMPLÉTER
        # On utilise le caractère suivant de la clef.
        j = (j+1) % k
    return(c)

def dechiffrement_xor_vigenere(message_chiffre,clef):
    # On initialise la chaîne de caractères qui va contenir le message
    # déchiffré.
    m = ""
    n = len(message_chiffre)
    k = len(clef)
    j = 0
    # On déchiffre chaque caractère i du message avec le caractère j de la clef. 
    for i in range(n):
        m = m + ... # À COMPLÉTER
        # On utilise le caractère suivant de la clef.
        j = (j+1) % k
    return(m)


# Question d

print(dechiffrement_xor_vigenere([48, 23, 23, 13, 15, 4, 68, 4, 17, 6, 65, 13, 3, 82, 2, 15, 4, 2, 65, 6, 7, 65, 12, 27, 1, 21, 139, 19, 1, 65, 93],"abracadabra"))
