# coding: utf-8

##
## Exercice 28 du chapitre 10 (Fréquence des lettres au Scrabble)
##

# Question a
points = {
    'E': 1, 'A': 1, 'I': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'L': 1,
    'D': 2, 'G': 2, 'M': 2,
    'B': 3, 'C': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4,
    'J': 8, 'Q': 8,
    'K': 10, 'W': 10, 'X': 10, 'Y': 10, 'Z': 10
}

# Question b
frequences = {
    'A': 7.11 + 0.31,
    'B': 1.14,
    'C': 3.18,
    'D': 3.67,
    'E': 12.10 + 1.94 + 0.31,
    'F': 1.11,
    'G': 1.23,
    'H': 1.11,
    'I': 6.59,
    'J': 0.34,
    'K': 0.29,
    'L': 4.96,
    'M': 2.62,
    'N': 6.39,
    'O': 5.02,
    'P': 2.49,
    'Q': 0.65,
    'R': 6.07,
    'S': 6.51,
    'T': 5.92,
    'U': 4.49,
    'V': 1.11,
    'W': 0.17,
    'X': 0.38,
    'Y': 0.46,
    'Z': 0.15,
}

# Question c
def affichage():
    lettres_avec_frequences = []

    for lettre, frequence in frequences.items():
        # À COMPLÉTER: ajouter les couples fréquence / lettre à la
        # variable lettres_avec_frequences
        ...

    # À COMPLÉTER: parcourir la variable lettres_avec_frequences triée
    # pour afficher les lettres par fréquence d'apparition décroissante
    for frequence, lettre in ...:
        print(f"{lettre}\t{frequence}\t{points[lettre]}")
