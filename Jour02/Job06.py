#Déclaration de ma fonction
def state(nombre):

#Je créer mes conditions
    if nombre > 0 :
        print("Positif")
    elif nombre < 0 :
        print("Négatif")
    else :
        return "null"

#Appel de la fonction avec plusieurs paramètres
state(1)
state(-5)
state(8)
state(-4)