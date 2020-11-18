""" Q3-1
    Recopier l'affectation suivante:
    n, a = 10 ** 10, 5
    puis écrire le code qui affiche le nombre de fois où il faut
    multiplier a par 3 avant de dépasser strictement la valeur de n.
    Le code doit fonctionner quelles que soient les valeurs de n et de a."""

"""n, a = 10 ** 10, 5
cpt = 0

while a < n:
    cpt = cpt + 1
    a = a * 3

print(cpt)"""



""" Q3-2
    Ecrire le code qui choisit deux nombres au hasard entre
    1 et 10 et qui répète cette action tant que les 2 nombres sont différents.
    Le code doit alors afficher le nombre de
    valeurs aléatoires qui ont été générées."""

"""
import random

a = random.randint(1, 10)
b = random.randint(1, 10)
cpt = 2

while a == b:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    cpt = cpt + 2
print(cpt)
"""

""" Q3-3
    Recopier l'affectation suivante:
    n = 10 ** 10
    puis écrire le code qui affiche le nombre minimum de fois où
    il faut diviser n par 2 (en division entière) pour obtenir 0.
    Le code doit fonctionner quelle que soit la valeur de n."""

"""n = 10 ** 10
res = n
cpt = 0

while res != 0:
    cpt = cpt + 1
    res = res // 2

print(cpt)"""


""" Q3-4
    Recopier l'affectation suivante:
    n = 20
    A chaque étape, si n est pair on le divise par 2,
    sinon on le multiplie par 3 et on ajoute 1.
    Ecrire le code qui affiche toutes les valeurs de n
    jusqu'à ce que la variable soit égale à un de la manière suivante:
    20
    10
    5
    16
    8
    4
    2
    Le code doit fonctionner quelle que soit la valeur de n."""

n = 20
while n != 1:
    print(n)
    if n % 2 == 0:
        n = n//2
    else:
        n = n * 3 + 1
