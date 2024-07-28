from random import randint
import os

reponse = randint(0, 100)
nombrechoisi = 0
essais = 0
print("L'ordinateur choisit un nombre entier compris entre 1 et 100: \nc'est le nombre mystère! Il y a donc 100 nombres possibles pour toi à deviner.\n Puis, tu proposes un nombre: \nsi le nombre mystère est plus grand que la proposition, \ntu verras «c'est plus » sur ton écran, sinon, \nil répond «c'est moins ». \nUne fois que ta réponse est correcte le message « Bravo » va s'afficher.")

while nombrechoisi != reponse and essais < 8:
    nombrechoisi = int(input("A quel nombre tu penses? "))
    essais = essais + 1
    if nombrechoisi > reponse:
        print("C'est moins. \n")

    elif nombrechoisi < reponse:
        print("C'est plus. \n")

if nombrechoisi == reponse:
    print(f"Bravo. Vous avez gagné en {essais} coups! ")

else :
    print(f"Trop lent, vous n'aviez que 3 chances.  {reponse}")


