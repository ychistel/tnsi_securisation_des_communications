##
## Chapitre 10 : projet supplémentaire
##

import time

def comparaison_chaines(chaine1, chaine2):
	if len(chaine1) != len(chaine2):
		return False
	for i in range(len(chaine1)):
		if chaine1[i] != chaine2[i]:
			return False
	return True

debut=time.time()
for i in range(1000000):
	comparaison_chaines("abcdefghijklmnopqrstuvwxyz", 
		"abcdefghijklmnopqrstuvwxyz")
fin=time.time()
print(fin-debut)
# environ 1,7s

debut=time.time()
for i in range(1000000):
	comparaison_chaines("zbcdefghijklmnopqrstuvwxyz", 			
                "abcdefghijklmnopqrstuvwxyz")
fin=time.time()
print(fin-debut)
# environ 0,4s