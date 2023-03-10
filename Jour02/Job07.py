#Je créer ma fonction
def spec (langage):
    #Je place mes conditions
    if langage == "javascript":
        return "Tu es un développeur web, Harry"
    elif langage == "python" :
        print("Tu es un développeur IA, Harry")
    elif langage == "java" :
        print("Tu es un développeur logiciel, Harry")
    elif langage == "reactjs" :
        print("Tu es un développeur mobile, Harry")
    else :
        print("Un jour, je serai le meilleur dress.. développeur")

#J'apelle ma fonction avec différents paramètres
print(spec("javascript"))
spec("python")
spec("java")
spec("reactjs")
spec("")
