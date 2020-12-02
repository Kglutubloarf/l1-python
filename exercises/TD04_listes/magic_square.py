carre_magique = [
    [4,14,15,1],
    [9,7,6,12],
    [5,11,10,8],
    [16,2,3,13]
]

carre_pas_magique = []



carre_pas_magique[1][1] = 3


def afficheCarre(carre):
    for l in carre:
        print(l)

afficheCarre(carre_magique)


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    val = -1
    for l in carre:
        pass
    
#print(testLignesEgales(carre_mag))
#print(testLignesEgales(carre_pas_mag))