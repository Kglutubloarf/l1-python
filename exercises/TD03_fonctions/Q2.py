""" Q2-1
    Recopier l'affectation suivante:
    n = 6
    puis écrire le code qui affiche le carré suivant:
    aaaaab
    aaaaab
    aaaaab
    aaaaab
    aaaaab
    aaaaab

    c'est-à-dire n lignes constituées de n-1 a et un b.
    Le code doit fonctionner quelle que soit la valeur de n. """

n = 6
for i in range(0, n):
    print("a" * (n-1) + "b")

""" Q2-2
    Recopier l'affectation suivante:
    n = 6
    puis écrire le code qui affiche le triangle de n lignes suivant:
    wwwwww
    wwwww
    wwww
    www
    ww
    w

    Le code doit fonctionner quelle que soit la valeur de n."""

n = 6
for i in range(n, 0, -1):
    print("w" * i)


""" Q2-3
    Recopier l'affectation suivante:
    n = 60
    puis écrire le code qui affiche tous les nombres
    qui divisent n de la manière suivante:
    1
    2
    3
    4
    5
    6
    10
    12
    15
    20
    30
    60
    Le code doit fonctionner quelle que soit la valeur de n."""

n = 60
for i in range(1, n+1):
    if n % i == 0:
        print(i)

""" Q2-4
    Recopier l'affectation suivante:
    n = 6
    puis écrire le code qui affiche
    la table de multiplication de n de la manière suivante:
    6 x 0 = 0
    6 x 1 = 6
    6 x 2 = 12
    6 x 3 = 18
    6 x 4 = 24
    6 x 5 = 30
    6 x 6 = 36
    6 x 7 = 42
    6 x 8 = 48
    6 x 9 = 54
    Le code doit fonctionner quelle que soit la valeur de n."""

n = 6
for i in range(0, 10):
    print(n, "x", i, "=", n * i)