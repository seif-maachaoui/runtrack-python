#Je souhaite afficher les nombres premiers jusqu'à 1000
#Je commence par déclarer une variable qui va vérifier les nombres
est_premier = True
#Ensuite je commence par déclarer une première boucle qui affiche les nombres de 2 jusqu'à 1000
for i in range (2, 10):
    #Ensuite je créer une autre boucle qui elle va permettre de vérifier si les nombres sont premiers ou non
    for n in range(2, i):
        #Si le reste du nombre divisé par i est égal à zéro alors il ne sera pas premier
        if i%n == 0 :
            print(i, "n'est pas premier")
            est_premier = False
            break
        #Sinon il sera alors premier
    if (est_premier == True):
        print(i, 'est permier')
    #On change l'état de la variable est_premier en True, pour que l'opération puisse se réitérer.
    est_premier = True    



        
        
    
    
    
        
    
    
        


        
    