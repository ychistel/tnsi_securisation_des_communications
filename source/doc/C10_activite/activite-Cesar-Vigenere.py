# coding: utf-8

##
## Activité du chapitre 10 (Chiffrements de César et de Vigenère)
##

# On crée le dictionnaire correspondant à un chiffrement de César avec le décalage 3.
dictionnaire_Cesar_3 = {}
for i in range(26):
    dictionnaire_Cesar_3[chr(i + ord("A"))] = chr((i + 3)%26 + ord("A"))
print(dictionnaire_Cesar_3)

# Sur ce modèle, la fonction creer_dictionnaire_Cesar crée le dictionnaire 
# correspondant à un chiffrement de César avec le décalage d fourni en paramètre.

def creer_dictionnaire_Cesar(d):
    dictionnaire_Cesar = {}
    for i in range(26):
        # À COMPLÉTER
    return(dictionnaire_Cesar)

# On vérifie que la fonction appliquée au paramètre 3 redonne bien 
# le dictionnaire dictionnaire_Cesar_3.

print(creer_dictionnaire_Cesar(3) == dictionnaire_Cesar_3)

# La fonction chiffrement_Cesar prend comme paramètres un entier d et une chaîne 
# de caractères message_clair et renvoie le message chiffré correspondant 
# au chiffrement de César de message_clair avec le décalage d. Seules les lettres 
# majuscules non accentuées seront chiffrées, les autres caractères étant 
# recopiés tels quels.

def chiffrement_Cesar(d, message_clair):
    message_chiffre = ""
    dictionnaire = # À COMPLÉTER
    for c in message_clair:
        # À COMPLÉTER en utilisant dictionnaire.get
    return(message_chiffre)

print(chiffrement_Cesar(7, "BONJOUR A TOUS LES ELEVES"))

# La fonction dechiffrement_Cesar prend comme paramètres un entier d et une chaîne 
# de caractères message_chiffre qui a été chiffrée avec un décalage de `d`. 
# Elle renvoie le message clair correspondant. 

def dechiffrement_Cesar(d, message_chiffre):
    return(chiffrement_Cesar(...)) # À  COMPLÉTER

print(dechiffrement_Cesar(4, "FMIRZIRYI HERW PI QSRHI HI PE GVCTXSKVETLMI"))

# La fonction chiffrement_Vigenere prend comme paramètres une chaîne de 
# caractères clef (qu'on suppose composée uniquement de lettres majuscules 
# non accentuées) et une chaîne de caractères message_clair et renvoie 
# le message chiffré correspondant au chiffrement de Vigenère de message_clair 
# avec les décalages donnés par clef. Seules les lettres majuscules non accentuées 
# seront chiffrées, les autres caractères étant recopiés tels quels.

# Pour cela, on découpe le message clair en paquets de n lettres (où n est
# la longueur de la clef) et on applique le chiffrement de César correspondant 
# à chaque lettre du paquet.

# On commence par créer les dictionnaires nécessaires pour chaque caractère
# de la clef.

def creer_dictionnaires_chiffrement(clef):
    dictionnaires = []
    n = len(clef)
    for i in range(n):
        dictionnaires.append(creer_dictionnaire_Cesar(...)) # À COMPLÉTER
    return(dictionnaires)     

# Pour le déchiffrement, on change simplement la valeur du décalage, comme
# pour le déchiffrement de César.

def creer_dictionnaires_dechiffrement(clef):
    dictionnaires = []
    n = len(clef)
    for i in range(n):
        dictionnaires.append(creer_dictionnaire_Cesar(...)) # À COMPLÉTER
    return(dictionnaires)

# Une fois les dictionnaires créés, on peut les utiliser pour transformer le message
# d'entrée en le message de sortie.

def applique_dictionnaire(dictionnaires, message_entree):
    # L'entier i désigne le caractère de la clef qui définit le décalage de César.
    i = 0
    n = len(dictionnaires)
    message_sortie = ""
    for c in message_entree:
        # On ne modifie le caractère que si c'est une lettre majuscule accentuée.
        if c in dictionnaires[i]:
            # À COMPLÉTER en utilisant dictionnaires.get
            # On incrémente i pour le caractère suivant.
            i = ... # À COMPLÉTER
        # Sinon, on recopie le caractère tel quel.
        else:
            message_sortie = message_sortie + c
    return(message_sortie)

# Il ne reste plus qu'à appliquer ces fonctions pour le chiffrement et le déchiffrement.

def chiffrement_Vigenere(clef, message_clair):
    # On utilise les dictionnaires liés à la clef.
    dictionnaires = creer_dictionnaires_chiffrement(clef)
    # On chiffre le message.
    message_chiffre = applique_dictionnaire(dictionnaires,message_clair)
    return(message_chiffre)

def dechiffrement_Vigenere(clef, message_chiffre):
    # On utilise les dictionnaires liés à la clef.
    dictionnaires = creer_dictionnaires_dechiffrement(clef)
    # On déchiffre le message.
    message_clair = applique_dictionnaire(dictionnaires,message_chiffre)
    return(message_clair)

print(dechiffrement_Vigenere("GLCO", "PP UIOD XSTF, L'OO GW, X'GT XOOYEI. PFNSY NGGGC"))
