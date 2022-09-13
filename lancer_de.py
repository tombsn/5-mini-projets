import random
print("1: Lancer le dé , 0 : Quitter le jeu")
while True:
    #On demande à l'utilisateur de saisir un nombre
    x = int (input("Cliquer sur un bouton "))
    if x == 0:
        print("Bye, à la prochaine")
        break

    elif x == 1:
        print(random.randint(1,6))

    else: 
        print("Je n'ai pas compris")