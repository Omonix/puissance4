from random import randint

def grille_vide():
    return [[0 for i in range(7)] for j in range(6)]
def affiche(g):
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] == 0:
                print('\033[1;97m.', end='')
            elif g[i][j] == 1:
                print('\033[1;32mX', end='')
            else:
                print('\033[1;31mO', end='')
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
        i = len(g)
        while i > 0:
            if g[i - 1][c] == 0:
                g[i - 1][c] = j
                break
            i -= 1
        return True
    return False
    
def horiz(g, j, l, c):
    if l + 4 < len(g[0]):
        for i in range(l, l + 4):
            if g[i][c] != j:
                return False
        return True
    return False
def vert(g, j, l, c):
    if c + 4 < len(g):
        for i in range(c, c + 4):
            if g[l][i] != j:
                return False
        return True
    return False
def diag(g, j, l, c):
    if l + 4 < len(g[0]) and c + 4 < len(g):
        for i in range(5):
            if g[l + i][c + i] != j:
                return False
        k = 5
        while k > 0:
            if g[l - k][c - k] != j:
                return False
        return True
    return False
def victoire(g, j):
    for i in range(len(g)):
        for k in range(len(g[i])):
            if horiz(g, j, i, k) or vert(g, j, i, k) or diag(g, j, i, k):
                return True
    return False
def match_nul(g):
    for i in range(len(g)):
        if g[0][i] == 0:
            return False
    return True
def coup_aleatoire(g, j):
    i = 0
    c = randint(i, 6)
    while coup_possible(g, c) == False and i < 6:
        i += 1
        c = randint(i, 6)
    jouer(g, j, c)

master_grille = grille_vide()
affiche(master_grille)
while True:
    affiche(master_grille)
    if match_nul(master_grille):
        affiche(master_grille)
        print('\033[1;97mMatch nul\033[0m')
        break
    request = input('\033[1;34mPlacer pion dans la colonne : ')
    if int(request) == 10:
        master_grille = [[1, 0, 1, 2, 2, 2, 1], [1, 2, 1, 2, 1, 2, 2], [2, 2, 2, 1, 2, 1, 1], [1, 1, 1, 2, 2, 2, 1], [1, 1, 1, 2, 1, 1, 2], [2, 2, 2, 1, 2, 1, 1]]
    elif int(request) == 11:
        master_grille = [[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 2, 1, 2], [0, 1, 2, 2, 1, 1], [1, 2, 2, 1, 1, 2]]
    if request.isdigit() == True and int(request) <= 7 and int(request) >= 0 and jouer(master_grille, 1, int(request) - 1):
        if victoire(master_grille, 1) == True:
            affiche(master_grille)
            print('\033[1;33mGagné !\033[0m')
            break
    else:
        continue
    coup_aleatoire(master_grille, 2)
    if victoire(master_grille, 2) == True:
        affiche(master_grille)
        print('\033[1;91mPerdu !\033[0m')
        break
