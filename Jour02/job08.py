#Je déclare ma fonction
def seasons (type, saison):

    #Je place mes conditions
    if type == "fruits" and saison == "hiver" :
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été" :
        print("Poire, fraise, cassis")
    if type == "légume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "légume" and saison == "été":
        print("artichaut, aubergine, navet")
    else :
        return "null"

#Appel de fonction avec différents paramètres
seasons("fruits", "été")
seasons("légume", "hiver")


    
