##
## Chapitre 10 -- Exercice 20
##

import hashlib

def hache_sha1(chaine):
    octets = chaine.encode()
    hache = hashlib.sha1(octets)
    return hache.hexdigest()

print(hache_sha1("motdepasse"))
# 940c0f26fd5a30775bb1cbd1f6840398d39bb813

print(len(hache_sha1("motdepasse")))
# 40

# comparaison des longueurs de sortie sur des chaînes de longueurs différentes
print(hache_sha1("abc"))
# a9993e364706816aba3e25717850c26c9cd0d89d

print(hache_sha1("azertyuiop"))
# 58ad983135fe15c5a8e2e15fb5b501aedcf70dc2

