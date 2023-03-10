#Je souhaite afficher les nombres premiers jusqu'à 1000
# D'abord je commence par déclarer une première boucle qui affiche les nombres de 2 jusqu'à 1000
for i in range (2, 10):
    #Ensuite je créer une autre boucle qui elle va permettre de vérifier si les nombres sont premiers ou non
    for n in range(2, i):
        #Si le reste du nombre divisé par i est égal à zéro alors il ne sera pas premier
        if i%n == 0 :
            print(i, "n'est pas premier")
        #Sinon il sera alors premier
        else:
            print(i, "est premier")
    



        
        
    
    
    
        
    
    
        


        
    