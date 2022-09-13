import random

#Je mets dans une liste les différents choix possibles
choices = ['C', 'P', 'Pi']
score_cpu = 0
score_joueur = 0

while True:
    #L'ordinateur choisi un des choix possible au hasard
    cpu = random.choice(choices)   
    #Le joueur choisi son jeu
    joueur = str(input("C : Ciseaux, P : Papier ou Pi : Pierre ? Pour terminer, veuillez taper 'Fin' : ")).capitalize()
    
    if joueur == cpu:
        print("Egalité !")

    elif joueur == 'Pi':
        if cpu == 'P':
            print("Vous perdez, le papier couvre la pierre")
            score_cpu += 1
        elif cpu == 'C':
            print("Vous gagnez, la pierre casse les ciseaux")
            score_joueur +=1

    elif joueur=="C":
        if cpu == "Pi":
            print("Vous perdez, la pierre casse les ciseaux")
            score_cpu += 1
        elif cpu == "P":
            print("Vous gagnez, les ciseaux coupent le papier")
            score_joueur += 1

    elif joueur == "P":
        if cpu == "Pi":
            print("Vous gagnez, la papier couvre la pierre")
            score_joueur += 1
        elif cpu == "C":
            print("Vous perdez, les ciseaux coupent le papier")
            score_cpu += 1
            
    elif joueur == "Fin":
        print("Résultat")
        print(f"CPU : {score_cpu}")
        print(f"Joueur : {score_joueur}")
        if score_cpu == score_joueur:
            print("Egalité, *il n'y a pas de vainqueur")
        elif score_cpu > score_joueur:
            print("Dommage, vous avez perdu le match")
        elif score_cpu < score_joueur:
            print("Félicitations, vous avez gagné le match")
        break

    else: 
        print("Vous avez choisi un choix qui n'existe pas")
