def tapis(n):
    #Je dessine la première ligne
    print("+", "-" * (n - 2), "+")
    #Ensuite je m'occupe des motifs présent sur le tapis
    for i in range(n-2):
        print("|", "#" * (n-3-i) + " "+ "#" * i,"|")
    #Enfin, la dernière ligne
    print("+", "-" * (n - 2), "+")
tapis(10)