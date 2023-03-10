#Je déclare une fonction
def triangle (a, b, c) :

#Je créer mes conditions
    if a > 0 and b > 0 or c > 0 :
        print("Vous pouvez construire un triangle")
        if a**2 + b**2 == c**2 :
            print("Ceci un triangle rectangle")
        elif a == b and b == c or c == a :
            print("Ceci est un triangle isocèle")
        else :
            print("Ceci est un triange équilatéral")
    else :
        print("Ceci est un triangle quelconque")

#J'apelle ma fonction
triangle(6, 6, 3) 
    
    
    
    

    
    
    

