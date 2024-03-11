##
## Chapitre 10 -- Exercice 33
##

def valeur_publique_Alice(p, g, a):
    return pow(g, a, p)

def valeur_publique_Bob(p, g, b):
    return pow(g, b, p)

def clef_secrete_Alice(p, a, B):
    return pow(B, a, p)

def clef_secrete_Bob(p, b, A):
    return pow(A, b, p)

p = 71
g = 23
a = 8
b = 12

A = valeur_publique_Alice(p, g, a)
print(A)  
# 48

B = valeur_publique_Bob(p, g, b)
print(B)  
# 20

K_A = clef_secrete_Alice(p, a, B)
K_B = clef_secrete_Bob(p, b, A)
print (K_A, K_B)   
# 20 20