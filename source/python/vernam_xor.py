from random import randint

def cle_alea(longueur):
    cle = ''
    for _ in range(longueur):
        cle += chr(randint(33,127))
    return cle

def chiffrer(message):
    mot_chiffre = b''
    msg = bytes(message,'latin1')
    cle = bytes(cle_alea(len(msg)),'latin1')
    print(msg,cle)
    for i in range(len(msg)):
        c = bytes(chr((msg[i]^cle[i])),'latin1')
        mot_chiffre += c
    return mot_chiffre,cle

def dechiffrer(message,cle):
    msg_clair = ''
    print(message,len(message),len(cle))
    for i in range(len(message)):
        msg_clair += chr(message[i]^cle[i])
    return msg_clair


message = 'La cryptographie symétrique est fantastique'
message_2 = "Les lettres é,è,à,ç,ï,ô,â,û,ê,ù sont pénibles à coder!"

msg_chiffre,cle = chiffrer(message_2)
msg_clair = dechiffrer(msg_chiffre,cle)

