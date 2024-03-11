##
## Chapitre 10 -- Exercice 23
##

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def position(lettre):
    return ALPHABET.find(lettre)

print(position("E"))
print(position("e"))

def chiffrement_Cesar(message, d):
    message_chiffre = ""
    for lettre in message:
        if lettre in ALPHABET:
            nouvel_indice = (position(lettre) + d)%26
            message_chiffre = message_chiffre + ALPHABET[nouvel_indice]
        else:
            message_chiffre = message_chiffre + lettre
    return(message_chiffre)

print(chiffrement_Cesar("CHIFFREMENT DE CESAR", 4))
# GLMJJVIQIRX HI GIWEV

def dechiffrement_Cesar(message, d):
    return chiffrement_Cesar(message, -d)

print(dechiffrement_Cesar("NPEEP XPESZOP FETWTDP FYP WTDEP AWFEZE BF'FY OTNETZYYLTCP.", 11))
# CETTE METHODE UTILISE UNE LISTE PLUTOT QU'UN DICTIONNAIRE.


print(chiffrement_Cesar("CETTE METHODE UTILISE UNE LISTE PLUTOT QU'UN DICTIONNAIRE.", 11))
# NPEEP XPESZOP FETWTDP FYP WTDEP AWFEZE BF'FY OTNETZYYLTCP.