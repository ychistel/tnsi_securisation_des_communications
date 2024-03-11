##
## Chapitre 10 -- Exercice 27
##

import random

def affiche_chiffres_aleatoires(n):
    for i in range(n):
        print(random.randint(0, 9), end='')
    print()

affiche_chiffres_aleatoires(10)
# 3518472394 par exemple...

random.seed(0)
affiche_chiffres_aleatoires(10)
# 6604876475

random.seed(0)
affiche_chiffres_aleatoires(10)
# 6604876475

random.seed(1)
affiche_chiffres_aleatoires(10)
# 2914177763