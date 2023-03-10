def replaceItem():
    myList = ["Jack", "Kate", "Desmond", "John"]
    #Je créer des variables pour stocker les valeurs de mes index
    index1 = myList[0]
    index2 = myList[3]
    
    i=0
    for i in range (len(myList)):
        if   myList[i] == index1:
             myList[i] = index2
        elif myList[i] == index2:
             myList[i] = index1

    print(myList)

replaceItem()
