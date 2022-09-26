der = int(input("adj meg egy számot"))
import random

szam = random.randint(1,5 )
#print(f'A generált szám: {szam}')

if szam > der:
    print("nagyobb")
    
if szam < der:
    print("kisebb")

else:
    print("egyenlő")
    




#print(der,"ez a te számod")