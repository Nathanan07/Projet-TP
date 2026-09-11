# TP6 Python : Boucle For & While
# Exercice 1 :

def serie_for(n:int):
    t = ()
    for i in range(1, n + 1):
        t += (i,)
    return t



def serie_while(n:int):
    x = 0
    while n > x :
        x += 1
        print(x, end=" ")



def serie_tr(n):
    return tuple(range(1, n + 1))


print(serie_for(5))
print(serie_while(5))
print(serie_tr(5))

# Exercice 2 : 

def serie_inverse_for(n:int):
    tu = []
    for s in range(n, 0, -1):
        tu.append(s)
    return tuple(tu)



def serie_inverse_while(n):
    resultat = []
    i = n
    while i >= 1:
        resultat.append(i)
        i -= 1
    return resultat     



def serie_inv_tr(n):
    return tuple(range(n, 0, -1))

print(serie_inverse_for(5))
print(serie_inverse_while(5))
print(serie_inv_tr(5))

# Exercice 3 :

def somme_for(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(somme_for(3), somme_for(5), somme_for(14))

def somme_while(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

print(somme_while(3), somme_while(5), somme_while(14))

def somme_sum_range(n):
    return sum(range(1, n + 1))

print(somme_sum_range(3), somme_sum_range(5), somme_sum_range(14))

# Exercice 4 :

def somme_cube_for(n):
    total = 0
    for i in range(1, n + 1):
        total += i**3
    return total

def somme_cube_while(n):
    total = 0
    i = 1
    while i <= n:
        total += i**3
        i += 1
    return total

print(somme_cube_for(3), somme_cube_for(5), somme_cube_for(14))
print(somme_cube_while(3), somme_cube_while(5), somme_cube_while (14))

# Exercice 5 :

def produit_for(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total

def produit_while(n):
    total = 1
    a = 1
    while a <= n:
        total *= a
        a += 1
    return total

print(produit_for(3),produit_for(5),produit_for(14))
print(produit_while(3),produit_while(5),produit_while(14))

# Exercice 6 :

def produit_pair_forrange(n):
    total = 1
    for i in range(2, n+1, 2):
        total *= i
    return total

def produit_pair_forif(n):
    total = 1
    for i in range(1, n + 1):
        if i % 2 == 0:
            total *= i
    return total

print(produit_pair_forrange(3),produit_pair_forrange(5),produit_pair_forrange(14))
print(produit_pair_forif(3),produit_pair_forif(5),produit_pair_forif(14))

# Exercice 7 :

def inverse(n):
    total = 0
    for i in range(1, n + 1):
        total += ((-1)**(i+1)) / i
    return total

print(inverse(3),inverse(5),inverse(14))

# Exercice 8 :

def liste_parite(n: list):
    pair=[]
    impair=[]
    for i in n:
        if i % 2 == 0:
            pair.append(i)
        else:
            impair.append(i)
    return (pair, impair)

print(liste_parite([6,5,8,1,3,4,7,2]))

# Exercice 9:

"""def occurence(n):
    liste = []
    for i in range(1,n+1):
        




occurence([6,5,8,6,2,7,6,5,2])"""