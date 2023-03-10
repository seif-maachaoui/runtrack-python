def pairList ():
    L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
    somme = 0
    for i in range (len(L)):
        if L[i]%2 == 0:
            somme = somme + L[i] 
    print(somme, "est la somme des nombres paires")
     
pairList()