def myNumber ():
    L = [8, 24, 48, 2, 16]
    compteur = 0
    for i in range (len(L)):
        if L[i]%3 == 0:
            compteur+=1
            print(L[i], "est un multiple de 3")
        else:
            print(L[i], "n'est pas un multiple de 3")
    print("il y a ", compteur, "multiple de 3" )
myNumber()