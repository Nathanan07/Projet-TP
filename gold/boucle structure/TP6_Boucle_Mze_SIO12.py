# ========================== EXO 1 ========================== #

def serie_1(n:int):
    nb_entiers = []

    for i in range(1, n+1):
        nb_entiers.append(i)
    
    return tuple(nb_entiers)

def serie_2(n:int):
    nb_entiers = []
    nb = 1

    while nb < n+1:
        nb_entiers.append(nb)
        nb += 1
    
    return nb_entiers

def serie_3(n:int):
    nb_entiers = range(1, n+1)
    return nb_entiers

# ========================== EXO 2 ========================== #

def serie_inverse_1(n:int):
    nb_entiers = []

    for i in range(1, n+1):
        nb_entiers.append(i)
    
    nb_entiers.reverse()

    return tuple(nb_entiers)

def serie_inverse_2(n:int):
    nb_entiers = []
    nb = 1

    while nb < n+1:
        nb_entiers.append(nb)
        nb += 1
    
    nb_entiers.reverse()
    
    return nb_entiers

def serie_inverse_3(n:int):
    nb_entiers = list(range(1, n+1))
    nb_entiers.reverse()
    return nb_entiers

# ========================== EXO 3 ========================== #


def somme_1(n:int):
    sommes = 0
    
    for i in range(1,n+1):
        sommes += i
        
    return sommes

def somme_2(n:int):
    pass

def somme_3(n:int):
    sommes = list(range(1,n))
    return sum(sommes) # Ensuite on retourne la somme de la liste

# ========================== EXO 4 ========================== #

def somme_cube_1(n:int):
    apl_conv = list(serie_1(n))
    # On crée une liste qui va stocker les resultats de chaque element 
    # de la liste apl_conv au cube.
    liste = []
    for i in apl_conv:
        liste.append(i**3)
    
    # On retiourne la somme de la liste qu'on avait stocker les cube de 
    # chaque element de la liste apl_conv
    return sum(liste)

def somme_cube_2(n:int):
    liste = []
    compteur = 0

    while compteur < n:
        compteur += 1 

        liste.append(compteur**3)

    return sum(liste)


# ========================== EXO 5 ========================== #

def produit_1(n:int):
    liste = list(serie_2(n))
    res = 1

    for i in liste:
        res *= i

    return f"la factorielle de {n}! = {res}"

def produit_2(n:int):
    pass


# ========================== EXO 6 ========================== #

def produit_pair_1(n:int):
    liste = list(range(2,n,2))
    compteur = 1

    for i in range(len(liste)):
        compteur = liste[i]*compteur

    return compteur
        

def produit_pair_2(n:int):
    liste = list(range(1,n))
    compteur = 1

    for i in liste:
        if i%2 == 0:
            compteur = i*compteur
        else:
            continue

    return compteur

def produit_pair_3(n:int):
    lim = 1 # Cette variable nous permettra de rendre la bloucle au bout d'un moment False
    resultat = 1 # Voici la résultat quis era mis à jour à chaque répetition de la boucle

    while lim <= n: 
        if lim%2 == 0:
            resultat *= lim

        lim += 1

    return resultat 
    
# ========================== EXO 7 ========================== #

def inverse(n:int):
    resultat = 0

    for i in range(1,n+1):
        resultat += ((-1)**(i+1))/i

    return resultat

# ========================== EXO 8 ========================== #

def liste_partie(n:list)-> tuple:
    ls_pairs = []
    ls_impairs = []

    for i in n:
        if i%2 == 0:
            ls_pairs.append(i)
        else:
            ls_impairs.append(i)

    return ls_pairs, ls_impairs
    # return f"Liste de nombre paire : {ls_pairs} \nListe de nombre impaire : {ls_impairs}"

# ========================== EXO 9 ========================== #
def occurence(n:list):
    pass

# ========================== EXO 10 ========================== #

def del_occurence(n:list):

    ls_s1_occu = []

    for i in n:
        if i not in ls_s1_occu:
            ls_s1_occu.append(i)
        else:
            continue

    return ls_s1_occu 

# ========================== EXO 11 ========================== #

def nb_premier(n:int):
    pass

# ========================== Code principale ========================== #
                
# Exo 1 :
# print(serie_1(10)) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(serie_2(15)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# print(serie_2(20)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# EXO 2 :
# print(serie_inverse_1(5)) # (5, 4, 3, 2, 1)
# print(serie_inverse_2(6)) # [6, 5, 4, 3, 2, 1]
# print(serie_inverse_3(7)) # [7, 6, 5, 4, 3, 2, 1]

# EXO 3 :
# print(somme_1(14)) # 105
# print(somme_2(14))
# print(somme_3(3))

# EXO 4 :
# print(somme_cube_1(5)) # 225
# print(somme_cube_2(5)) # 225


# EXO 5 :
# print(produit_1(5)) # 120


# EXO 6 :
# print(produit_pair_1(5)) # 8
# print(produit_pair_2(5)) # 8
# print(produit_pair_3(5)) # 8

# EXO 7 : 
# print(inverse(3))

# EXO 8 :
# print(liste_partie([6,5,8,1,3,4,7,2]))

# EXO 9 :
# print(occurence([6,5,8,6,2,7,6,5,2]))

# EXO 10 :
# print(del_occurence([6,5,8,6,2,7,6,5,2]))

# EXO 11 :
# print(nb_premier(5))
# print(nb_premier(6))




# A connaître :
 
""" 
    Laboucle While: on l'utilise que quand on sait opas qund est ce qu'on va s'arrêté.
    Et lea boucle For est utiliser pour un nombre de repetition dont on sait d'avance. 
"""



3 5 7 9 11 13 15

