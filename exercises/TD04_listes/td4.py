"""
En partant d'un entier n de départ, on définit une suite d'entiers en obtenant chaque nouveau 
terme à partir du précédent soit en le divisant par 2 s'il est pair,
soit en le multipliant par 3 et en ajoutant 1 s'il est impair.

Ecrire la fonction qui, à partir d'un entier initial, renvoie la liste des valeurs successives jusqu'à ce que
la valeur 1 soit atteinte (le dernier élément de la liste est donc toujours 1).
"""


def syracuse(n):
    lis = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        lis.append(n)
    return lis


import matplotlib.pyplot as plt
import numpy as np

x = [65,44,27,18,52,84]
y = [20,48,55,68,78,90]
ax = [65,52]
ay = [20,78]
bx = [44,18]
by = [48,68]
cx = [27,84]
cy = [55,90]

plt.plot(x, y)
plt.plot(ax, ay)
plt.plot(bx, by)
plt.plot(cx, cy)
plt.show()

#(65, 20, 0) (44, 48, 1) (27, 55, 2) (18, 68, 1) (52, 78, 0) (84, 90, 2) 