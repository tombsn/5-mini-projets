import random

#L'utilisateur indique la longueur de son mot de passe
lengthPassword = int(input('Donner la longueur du mot de passe : ')) 

#J'indique les caractères utilisables par le générateur
s='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

#Regrouper les caractères sélectionnés aléatoirement en un seul mot
password = ''.join(random.sample(s, lengthPassword))

#J'affiche le mot de passe
print(password)