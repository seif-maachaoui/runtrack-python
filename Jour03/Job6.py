#Je créer mes variables
Message = "abcdefghijklmnopqrstuvwxyz"
Lettre = 0
Ligne = 15

for x in range(Lettre, Ligne):
    while Lettre <= len(Message):
        Lettre+=1
        print(Message[Lettre])


