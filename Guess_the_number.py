import random

chosen_number = random.randint(1,6)
result = False

#J'instancie le nombre de tentatives à 3
for i in range(3):
    proposed_number = int(input("Saisir un nombre entre 1 et 6 : "))
    if chosen_number == proposed_number:
        result = True
        break
    elif chosen_number < proposed_number:
        print("Le nombre que vous avez proposé est supérieur à celui de l'ordinateur")
    elif chosen_number > proposed_number:
        print("Le nombre que vous avez proposé est inférieur à celui de l'ordinateur")

if result == True:
    print("Bravo, vous avez gagné")

else: 
    print(f'Vous avez perdu, le bon numéro était {chosen_number}')