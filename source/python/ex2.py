def chiffre(mot,clef):
    chiffre=''
    for i in range(len(mot)):
        print(ord(mot[i])^ord(clef[i%4]))
        chiffre+=(chr(ord(mot[i])^ord(clef[i%4])))
    return chiffre

def melange_couleur(couleur1,couleur2):
    couleur=[0,0,0]
    for i in range(3):
        couleur[i]=(couleur1[i]+couleur2[i])//2
    return couleur

def diffie_helman(couleur1,couleur2):
    """ les couleurs sont au format RGB, c'est à dire un triplet,
    de trois valeurs comprises entre 0 et 255.
    Dans le cas contraire, valeur hexadécimale, on la transforme
    la fonction renvoie une couleur !
    """
    couleur=[0,0,0]
    for i in range(3):
        couleur[i]=((2*couleur1[i]+couleur2[i])//3)
    return couleur

if __name__=='__main__' :
    mot_chiffre=chiffre('BONJOUR LA MÉTÉO','09yz')
    mot_clair=chiffre(mot_chiffre,'09yz')
    """
    couleur_publique=(250,205,0)
    couleur_source=(50,102,190)
    couleur_dest=(48,96,65)
    
    # Clef à la source :
    couleur_dest_publique=melange_couleur(couleur_dest,couleur_publique)
    print(couleur_dest_publique)
    clef1=diffie_helman(couleur_dest_publique,couleur_source)
    print(clef1)
    
    # Clef destinataire :
    couleur_source_publique=melange_couleur(couleur_source,couleur_publique)
    print(couleur_source_publique)
    clef2=diffie_helman(couleur_source_publique,couleur_dest)
    print(clef2)
    """