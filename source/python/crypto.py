"""
QUELQUES INFORMATIONS:
----------------------

- le message en clair est enregisté danns le fichier clair.txt
- le message chiffré est enregistré dans le fichier crypte.txt
- le message déchiffré est enregistré dans le fichier decrypte.txt

Un message chiffré est en binaire et nécessite une lecture en binaire
Un message clair est rédigé en codage utf-8
Pour chiffrer un message, il est indispensable de le tranformer en binaire avec
la fonction encode(). La fonction decode() transforme un contenu binaire en codage utf-8
"""

# varibles à utiliser
# -------------------

msg = '' # mon message initial en clair
msg_chiffre = '' # mon message chiffré
msg_dechiffre = '' # mon message final déchiffré
clef = b'la clef de chiffrement' # la clef de chiffrement à remplacer par la votre!


# Fonction de chiffrement d'un message avec clef

def chiffrer_message(m,c):
    """
    Paramètres:
    - m est le message à chiffrer
    - c est la clef de chiffrement
    Principe:
    les arguments m et c sont en binaires;
    le message est transformé par OU exclusif
    la fonction renvoie une chaine en binaire (commence par b'...')
    Cette fonction peut déchiffrer un message chiffré avec la même clef !
    """
    return bytes([m[i] ^ c[i % len(clef)] for i in range(len(m))])


# Ouvrir un fichier au contenu en UTF-8 pour le chiffrer
# ------------------------------------------------------
def chiffrer(c):
    with open("clair.txt",mode="r",encoding='utf8') as f:
        # transforme le contenu utf-8 en binaire
        m=f.read().encode('utf-8')
        # Ici on affiche le message en binaire mais on peut le chiffrer ...
        # Ici c'est à vous de compléter !
        print(m,'\n')
    return m



# Ouvrir un fichier au contenu binaire pour traitement
# ----------------------------------------------------
def dechiffrer(c):
    # on récupère le message chiffré pour traitement
    with open("crypte.txt",mode="rb") as f:
        m=f.read()
        # Ici on affiche le message en binaire mais on peut le déchiffrer ...
        # Ici c'est à vous de compléter !
        print(m)
    return m
    


# Écrire une donnée en binaire dans un fichier
# -------------------------------------------
def enregistrer_crypte(m):
    with open("crypte.txt",mode="wb") as f:
        f.write(m)
        
        
# Écrire une donnée en UTF-8 dans un fichier
# -------------------------------------------
def enregistrer_decrypte(m):
    with open("decrypte.txt",mode="w",encoding='utf8') as f:
        f.write(m)


# Programme principal
# -------------------

if __name__=='__main__':
    # 1/ on chiffre le message avec sa clef
    msg_chiffre = ''
    
    # 2/ on enregistre le message chiffré dans un fichier
    

    # 3/ on déchiffre le message avec la clef 
    msg_dechiffre = ''
    
    # 4/ on enregistre le message déchiffré dans un fichier.
    # Attention, il faut appliquer la méthode decode() au message déchiffré !
    
    