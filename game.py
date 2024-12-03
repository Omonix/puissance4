def grille_vide():
    return [[1 for i in range(7)] for j in range(6)]
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
def coup_possible(g, c):
    i = len(g)
    while i > 0:
        if g[i - 1][c] == 0:
            return True
        i -= 1
    return False
def jouer(g, j, c):
    if coup_possible(g, c) == True:
        if j == 1:
            point = 'X'
        else:
            point = 'O'
        i = len(g)
        while i > 0:
            if g[i - 1][c] == 0:
                g[i - 1][c] = point
                break
            i -= 1
def horiz(g, j, l, c):
    for i in range(l, l + 4):
        if g[i][c] != j:
            return False
    return True
def vert(g, j, l, c):
    for i in range(c, c + 4):
        if g[l][i] != j:
            return False
    return True
def diag(g, j, l, c):
    for i in range(4):
        if g[l + i][c + i] != j:
            return False
    return True
