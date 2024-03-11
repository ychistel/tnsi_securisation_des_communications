import os, subprocess, base64

#os.system("C:/windows/notepad.exe")

#directory = os.getcwd()

#os.startfile("..\code_cesar.pdf")

def chemin(path,niveau=1):
    dossier = path.split('\\')
    if niveau <= len(dossier):
        for _ in range(niveau):
            dossier.pop()
    new_path = '\\'.join(dossier)
    return new_path

def les_dossiers(path):
    """ recherche les dossiers contenus dans un dossier indiqué par son chemin (path)
        renvoie la liste des dossiers contenus"""
    p = path
    dossiers=[]
    for elt in os.listdir(path):
        if os.path.isdir(p+"\\"+elt):
            dossiers.append(elt)
        p = path
    return dossiers

for i in range(8):
    c=chemin(os.getcwd(),i)
    print(c)
d=les_dossiers(c)
print(d)  
    
#print(os.listdir(str(chemin(os.getcwd(),2))))
"""
fichier="www-interstices-info.pem"
print(fichier)
p1=subprocess.run(["C:\\Program Files\\OpenSSL-Win64\\bin\\openssl",\
                    "x509","-in",fichier,"-pubkey","-noout"],\
                 shell=True,capture_output=True,text=True)
print(p1.stdout)
"""
fichier="www-interstices-info.pem"
p2=subprocess.Popen(["C:\\Program Files\\OpenSSL-Win64\\bin\\openssl",\
                    "x509","-in",fichier,"-pubkey","-text"],\
                 shell=True,text=True)
"""
fichier = "C:\\Users\\yannick\\Documents\\Lycée\\TNSI\\21-22\\Latex\\Architecture_materielle\\img\\carrefour.png"
p3=subprocess.run(["mspaint" ,fichier])

"""

