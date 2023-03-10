# Je commence par importer le module string, un module est une collection de variables et de fonctions
import string
#Je commence par définir une variable alphabet qui contient la fonction string suivi d'ascii
alphabet = string.ascii_uppercase

#Ensuite je vais définir une variable reverse_alphabet
#la fonction join va fusionner tout les caractères résultant de la fonction reversed
#la fonction reversed ici est utilisé pour donner l'inverse de la variable alphabet
reverse_alphabet = ''.join(reversed(alphabet))
print("the reversed alphabet is", reverse_alphabet)