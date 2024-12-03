def grille_vide():
    return [[0 for i in range(7)] for j in range(6)]
def affiche(g):
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] == 0:
                print('.', end='')
            elif g[i][j] == 1:
                print('X', end='')
            else:
                print('O', end='')
        print('', end='\n')