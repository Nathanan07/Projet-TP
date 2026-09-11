# TP_Calculatrice

from math import *

# Programme finale

def addition(a: int ,b: int):
    return a + b

def soustraction(a: int ,b: int):
    return a - b

def multiplication(a: int ,b: int):
    return a * b

def division(a: int ,b: int):
    if a == 0:
        return "Erreur : division par zéro"
    elif b == 0:
        return "Erreur : division par zéro"
    else:
        return float(a // b)

def puissance(a: int, b: int):
    return a ** b

def racine_carree(a: int):
    if a < 0:
        print("Erreur : racine carrée d’un nombre négatif")
    else:
        return sqrt(a)

def modulo(a: int, b: int):
    return a % b


def calculer(operation, a: int, b = None):
    if operation == "+":
        return addition(a,b)
    elif operation == "-":
        return soustraction(a,b)
    elif operation =="*":
        return multiplication(a,b)
    elif operation == "/":
        return division(a,b)
    elif operation == "^":   #modification ex4
        return puissance(a, b)
    elif operation == "sqrt":
        return racine_carree(a)
    elif operation == "%":
        return modulo(a, b)

def demander_calcul():
    a = int(input("Entrez le premier nombre : "))
    b = int(input("Entrez le deuxième nombre : "))
    operation = input("Entrez l'opération (+, -, *, /) : ")
    if operation == "/" and a == 0 or b == 0:
        print("Le résultat de ", float(a), operation, float(b), "est : ", (calculer(operation,a,b)))
    else:
        print("Le résultat de ", float(a), operation, float(b), "est : ", float(calculer(operation,a,b)))

def calculer2(cal: str):
    elements = cal.split()
    nbr1 = float(elements[0])
    operateur = (elements[1])
    nbr2 = float(elements[2])

    if operateur == "+":
        resultat = addition(nbr1,nbr2)
    elif operateur == "-":
        resultat = soustraction(nbr1,nbr2)
    elif operateur =="*":
        resultat = multiplication(nbr1,nbr2)
    elif operateur == "/":
        resultat = division(nbr1,nbr2)
    elif operateur == "^":
        resultat = puissance(nbr1, nbr2)
    elif operateur == "%":
        resultat = modulo(nbr1,nbr2)
    else:
        return "Opérateur non reconnu."
    
    print("Le résultat de ", nbr1, operateur, nbr2, "est : ", resultat)
    return resultat 

def est_pair(n):
    resultat = calculer2(f"{n} % 2")
    return resultat == 0

def afficher_parite():
    n = int(input("Entrez un nombre entier : "))
    if est_pair(n):
        print("Le nombre", n, "est pair.")
    else:
        print("Le nombre", n, "est impair.")

def calculer_mediane(liste):
    liste_triee = sorted(liste)
    n = len(liste_triee)

    if est_pair(n):
        milieu1 = liste_triee[n//2 - 1]
        milieu2 = liste_triee[n//2]
        mediane = (milieu1 + milieu2) / 2
    else:
        mediane = liste_triee[n//2]

    print(f"La médiane est : {mediane}")
    return mediane

# Exercice 1 :
"""def addition(a: int ,b: int):
    return a + b

def soustraction(a: int ,b: int):
    return a - b

def multiplication(a: int ,b: int):
    return a * b

def division(a: int ,b: int):
    if a == 0:
        return "Erreur : division par zéro"
    elif b == 0:
        return "Erreur : division par zéro"
    else:
        return float(a // b)"""

"""print(addition(3, 4))
print(soustraction(10, 5))
print(multiplication(6, 7))
print(division(8, 2))
print(division(8, 0)) """

# Exercice 2 :
"""def calculer(operation: str, a: int, b: None):
    if operation == "+":
        return addition(a,b)
    elif operation == "-":
        return soustraction(a,b)
    elif operation =="*":
        return multiplication(a,b)
    elif operation == "/":
        return division(a,b)

print(calculer("+", 3, 4))
print(calculer("-", 10, 5))
print(calculer("*", 6, 7))
print(calculer("/", 8, 2))
print(calculer("/", 8, 0))"""

# Exercice 3 :

"""def demander_calcul():
    a = int(input("Entrez le premier nombre : "))
    b = int(input("Entrez le deuxième nombre : "))
    operation = input("Entrez l'opération (+, -, *, /) : ")
    if operation == "/" and a == 0 or b == 0:
        print("Le résultat de ", float(a), operation, float(b), "est : ", (calculer(operation,a,b)))
    else:
        print("Le résultat de ", float(a), operation, float(b), "est : ", float(calculer(operation,a,b)))"""

#demander_calcul()

# Exercice 4 :

"""def puissance(a, b):
    return a ** b

def racine_carree(a: int):
    if a < 0:
        print("Erreur : racine carrée d’un nombre négatif")
    else:
        return sqrt(a)

def modulo(a, b):
    return a % b"""

"""def calculer(operation, a: int, b = None):
    if operation == "+":
        return addition(a,b)
    elif operation == "-":
        return soustraction(a,b)
    elif operation =="*":
        return multiplication(a,b)
    elif operation == "/":
        return division(a,b)
    elif operation == "^":   #modification ex4
        return puissance(a, b)
    elif operation == "sqrt":
        return racine_carree(a)
    elif operation == "%":
        return modulo(a, b)"""

# Exercice 5 :

"""def calculer2(cal: str):
    elements = cal.split()
    nbr1 = float(elements[0])
    operateur = (elements[1])
    nbr2 = float(elements[2])

    if operateur == "+":
        resultat = addition(nbr1,nbr2)
    elif operateur == "-":
        resultat = soustraction(nbr1,nbr2)
    elif operateur =="*":
        resultat = multiplication(nbr1,nbr2)
    elif operateur == "/":
        resultat = division(nbr1,nbr2)
    elif operateur == "^":
        resultat = puissance(nbr1, nbr2)
    elif operateur == "%":
        resultat = modulo(nbr1,nbr2)
    else:
        return "Opérateur non reconnu."
    
    print("Le résultat de ", nbr1, operateur, nbr2, "est : ", resultat)
    return resultat """

# Exercice 6 :

"""def est_pair(n):
    # utiliser calculer2 pour faire n % 2
    resultat = calculer2(f"{n} % 2")
    return resultat == 0 """

""" def afficher_parite():
    n = int(input("Entrez un nombre entier : "))
    if est_pair(n):
        print("Le nombre", n, "est pair.")
    else:
        print("Le nombre", n, "est impair.") """

# Exercice 7 :

def calculer_mediane(liste):
    liste_triee = sorted(liste)
    n = len(liste_triee)

    if est_pair(n):
        milieu1 = liste_triee[n//2 - 1]
        milieu2 = liste_triee[n//2]
        mediane = (milieu1 + milieu2) / 2
    else:
        mediane = liste_triee[n//2]

    print(f"La médiane est : {mediane}")
    return mediane
    
# Test finale

# test ex1 :
print(addition(3, 4))
print(soustraction(10, 5))
print(multiplication(6, 7))
print(division(8, 2))
print(division(8, 0)) 

# test ex2 :

print(calculer("+", 3, 4))
print(calculer("-", 10, 5))
print(calculer("*", 6, 7))
print(calculer("/", 8, 2))
print(calculer("/", 8, 0))

# test ex3 :
demander_calcul()

#test ex4 :
print(calculer("^", 2, 3))
print(calculer("sqrt", 16))
print(calculer("%", 10, 3))
print(calculer("sqrt", -9))

#test ex5 :
calculer2("2 ^ 3")
calculer2("5.4 + 16")
calculer2("11 % 2")

# test ex6 :
print(est_pair(4))
print(est_pair(7))

afficher_parite()

# test ex7 :
print(calculer_mediane([5, 2, 9, 7]))
print(calculer_mediane([4, 6, 1, 8, 5]))