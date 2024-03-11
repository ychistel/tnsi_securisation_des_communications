##
## Chapitre 10 -- Exercice 21
##

import hashlib

def hache_mot_de_passe_avec_sel(sel, mot_de_passe):
    octets = (sel + mot_de_passe).encode()
    valeur_hachee = hashlib.sha1(octets)
    return sel, valeur_hachee.hexdigest()

print(hache_mot_de_passe_avec_sel("8E3A9AB3295AFF33", "azerty12"))
# ('8E3A9AB3295AFF33', '0c43e66a2fb2f571e59fc7476ad233145952381c')

print(hache_mot_de_passe_avec_sel("8E3A9AB3295AFF33", "SECRETsecret"))
# ('8E3A9AB3295AFF33', 'ee74da494f2e630f6545d3afdec216cc3c0cf752')

print(hache_mot_de_passe_avec_sel("8E3A9AB3295AFF33", "873lzJGg2e"))
#('8E3A9AB3295AFF33', '4c4e1fe1ed6a827edd9772d85f5734596ef15240')