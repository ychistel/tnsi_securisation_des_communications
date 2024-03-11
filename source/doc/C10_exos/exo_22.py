##
## Chapitre 10 -- Exercice 22
##

import hashlib
import time

def hache_sha1(chaine):
    octets = chaine.encode()
    hache = hashlib.sha1(octets)
    return hache.hexdigest()

def teste_hache(n):
    debut = time.time()
    for i in range(n):
        x = hache_sha1("motdepasse")
    fin = time.time()
    return (fin - debut)

print(teste_hache(1000000))
# environ 0,6 secondes

print(teste_hache(10000000))
# environ 6,7 secondes