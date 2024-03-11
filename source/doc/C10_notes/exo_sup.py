##
## Chapitre 10 : exercice supplémentaire
##

# question 3
print(ord("A"))
# 65

print(chr(65))
# A

print(0 ^ 1)
# 1

# question 3a
print(51 ^ 69)
# 118

print(0b00110011)
# 51

print(0b01000101)
# 69

print(0b01110110)
# 118

# question 3b
def chaine_vers_liste(chaine):
    liste = []
    for c in chaine:
        liste.append(ord(c))
    return liste

print(chaine_vers_liste("ACL"))
# [65, 67, 76]

# question 3c
def liste_vers_chaine(liste):
    chaine = ""
    for x in liste:
        chaine = chaine + chr(x)
    return chaine

print(liste_vers_chaine([65, 67, 76]))
# ACL

# question 3d
def chiffrement_listes(message_liste, clef_liste):
    message_chiffre_liste = []
    for i in range(len(message_liste)):
        message_chiffre_liste.append(message_liste[i] ^ clef_liste[i])
    return message_chiffre_liste

print(chiffrement_listes([65,67],[55,50]))
# [118, 113]

print(65^55)
# 118

print(67^50)
# 113

# question 3e
def chiffrement(message, clef):
    message_liste = chaine_vers_liste(message)
    clef_liste = chaine_vers_liste(clef)
    chiffre_liste = chiffrement_listes(message_liste, clef_liste)
    chiffre = liste_vers_chaine(chiffre_liste)
    return chiffre

print(chiffrement("AC", "72"))
# vq

# question 3f
def dechiffrement(message_chiffre, clef):
    return chiffrement(message_chiffre, clef)

print(dechiffrement("vq", "72"))
# AC