def myList ():
    L =[5, 8, 3, 6, 10]
    print(L[1])
    i=0
    for i in range(len(L)):
        if L[i] == L[3]:
           L[3] = L[2]+L[4]
           print(L)

    print(L[4])             
myList()

