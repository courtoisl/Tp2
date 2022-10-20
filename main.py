"""
Programme fait par Evan Courtois
Groupe: 406
Description: Un code qui permet de jouer contre l'ordinateur a un match de "devine le chiffre"
import random
chiffre_aleatoire = random.randint(1, 69)


guess = int(input("Il faut deviner un nombre entre 1 et 69"))

if guess == chiffre_aleatoire:
    print("Bravo, ta réponse est correcte.")

elif guess > chiffre_aleatoire:
    print(guess + "est trop haut!")
"""
import random

chiffre_aleatoire = random.randint(1, 60)
essai = 0
guess = int(input("Entrez un nombre de 1 a 60: "))
while chiffre_aleatoire != guess:

    if guess < chiffre_aleatoire:
        essai = essai + 1
        print("Ton nombre est trop bas")
        guess = int(input("Entrez un nombre de 1 a 60: "))
    elif guess > chiffre_aleatoire:
        essai = essai + 1
        print("Ton nombre est trop haut")
        guess = int(input("Entrez un nombre de 1 a 60: "))

essai = essai + 1
print("Bravo, ta réponse est correcte!")
print(f"Tu l'as eu en {essai} essais.")