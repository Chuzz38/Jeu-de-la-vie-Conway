import time
import os

hauteur = 40
largeur = 200

def init_grille():
    plateau = []
    for _ in range(hauteur):
        ligne = [0] * largeur
        plateau.append(ligne)
    return plateau

def init_forme_depart(grille):
    grille[24][25] = 1
    grille[24][26] = 1
    grille[25][26] = 1
    grille[26][26] = 1
    grille[26][25] = 1
    grille[26][24] = 1

def affiche_grille(grille):
    for i in range(hauteur):
        for j in range(largeur):
            if grille[i][j] == 0: # cel morte
                print(".", end = "")
            else: # cel vivante
                print("#", end = "")
        print()

def compte_voisin(grille, x, y):
    if grille[x][y] == 0:
        n = 0
    else:
        n = -1
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if 0 <= (x + i) < hauteur and 0 <= (y + j) < largeur:
                if grille[x+i][y+j] == 1:
                    n += 1
    return n

def prochain_etat_cel(grille, x, y):
    n = compte_voisin(grille, x, y)
    if n == 3:
        return 1
    elif n == 2:
        return grille[x][y]
    else:
        return 0

def vider_grille(grille):
    for _ in range(hauteur):
        grille.pop()

def copier_grille(grille1, grille2):
    for i in range(hauteur):
        for j in range(largeur):
            grille1[i][j] = grille2[i][j]
            
def maj_grille(grille):
    nouvelle_grille = init_grille()
    for i in range(hauteur):
        for j in range(largeur):
            nouvelle_grille[i][j] = prochain_etat_cel(grille, i, j)
    
    return nouvelle_grille

def main():
    grille = init_grille()
    init_forme_depart(grille)
    affiche_grille(grille)
    
    while True:
        time.sleep(0.5)
        grille = maj_grille(grille)
        os.system("cls")
        affiche_grille(grille)
        
    
main()