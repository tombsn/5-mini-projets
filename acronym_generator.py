import random

#Je demande à l'utilisateur de rentrer une chaine de caractère
text = str(input('Entrez une chaine de caractères : '))

word = text.split()

accro = ''

for i in word:
    accro=accro+str(i[0]).upper()

print("Voici l'acronyme de la chaine de caractère : " + accro)