lista = []
c = None
while c != "":
    c = input("Adj meg kis a betűvel kezdődő szavakat\t")
    if c != "":
         print("")
    for x in c:
        if "a" in x:
            lista.append(c)
print(lista)