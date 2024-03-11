def cle_publique(g,p,x):
    """
    g : générateur de base
    p : nombre premier servant au modulo
    x : clé privée valeur numérique aléatoire
    La fonction renvoie la clé publique calculée
    """
    pass
    
def cle_chiffrement_partage(x,p,X):
    """
    x : clé privée
    p : nombre premier servant au modulo
    X : clé publique calculée
    La fonction renvoie la clé partagée pour chiffrer et déchiffrer
    """
    pass

def est_premier(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

def chiffrer(message,cle):
    mot_chiffre = ''
    for i in range(len(message)):
        mot_chiffre += chr(ord(message[i])^cle)
    return mot_chiffre


# On définit un générateur g et un nombre premier p en commun
g = ...
p = ...

# Alice choisit une clé privée et génère une clé publique à partager A
a = int(input("Saisir la clé privée d'Alice : "))
A = ...
print("La clé publique envoyée par Alice à Bob est : ",A)

# Bob choisit une clé privée et génère une clé publique à partager B
b = int(input("Saisir la clé privée de Bob : "))
B = ...
print("La clé publique envoyée par Bob à Alice est : ",B)

# Après récéption des clés partagées, chacun calcule sa clé de chiffrement partagée
K_Alice = ...
K_Bob = ...

# Chiffrement d'un message par Alice avec sa clé partagée
message = input("Saisir un message à chiffrer :")
msg_chiffre = chiffrer(message,K_Alice)
print("Le message chiffré envoyé par Alice : ",msg_chiffre)

# Déchiffrement du message reçu par Bob avec sa cle partagée
msg_clair = chiffrer(msg_chiffre,K_Bob)
print("Le message déchiffré reçu par Bob : ",msg_clair)