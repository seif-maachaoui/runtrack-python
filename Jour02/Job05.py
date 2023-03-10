#Déclaration de ma fonction
def calcule(num1, operator, num2):

#Je place des conditions pour pouvoir gérer le fonctionnement des différents opérateurs
    if operator == '+' :
        print(num1+num2)
    elif operator == '-':
        print(num1-num2)
    if operator == '*':
        print(num1*num2)
    elif operator == '/':
        print(num1/num2)
    if operator == '%' :
        print(num1%num2)
    else :
        return "null"

# J'appelle ma fonction en plaçant les paramètres        
calcule(8, '+', 2)
calcule(5, '*', 5)
calcule(8, '/', 4)



