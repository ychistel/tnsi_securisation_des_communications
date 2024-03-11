msg = 'Le père Noël est une ordure !'
crypt = ''
decrypt = ''

for lettre in msg:
    crypt += chr(ord(lettre)+7)
print(msg)
print(crypt)

for lettre in crypt:
    decrypt += chr(ord(lettre)-7)
print(decrypt)