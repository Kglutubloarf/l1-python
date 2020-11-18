
""" Ecrire le code qui demande un nombre entier à un utilisateur puis
    affiche "Gagné" si ce nombre est compris
    entre 20 (inclus) et 50 (inclus). """

num = 30
if num in range(20, 51):
    print("Gagné")

""" Q1-2
    Ecrire le code qui demande à l'utilisateur de saisir un mot,
    et qui affiche "Gagné" si ce mot se trouve
    entre les mots "informatique" (inclus) et "physique"
    (non inclus) dans un dictionnaire. """

word = input()
if word >= "informatique" and word < "physique":
    print("Gagné")

""" Q1-4
    Ecrire le code qui demande un nombre entier
    à un utilisateur puis affiche "Gagné" si
    ce nombre est supérieur ou égal à 25, et qui affiche
    "dommage" s'il est égal à 24."""

num = int(input())
if num >= 25:
    print("Gagné")

if num == 24:
    print("Dommage")
