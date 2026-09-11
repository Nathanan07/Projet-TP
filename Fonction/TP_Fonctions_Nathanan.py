# Exercice 1 :
"""def ma_fonction():
    print("Hello World !")

ma_fonction()"""

# Exercice 2 :
"""def dire_bonjour(prénom):
    print("Bonjour",prénom)

print(dire_bonjour("Anna"))
print(dire_bonjour("Tim")) """

# Exerccice 3 :
"""def min_max(list):
    return (min(list),max(list))

print(min_max([56, 14, 99, 7, 38]))
print(min_max(["pomme", "banane", "abricot", "orange"]))"""


# Exercice 4 :

"""def somme(x: int ,y: int):
    return x + y

print(somme(2, 5))
print(somme(-4, 5))
print(somme(3, 4*2))
print(somme("trois", "six"))"""

# Exercice 5 :

"""def examen(note_fr, note_math, note_ang, note_info):
    # Coefficients pour chaque matière
    coefficients = [1, 2, 2, 3]

    # Calcul de la moyenne pondérée
    total_notes = note_fr * coefficients[0] + note_math * coefficients[1] + note_ang * coefficients[2] + note_info * coefficients[3]
    total_coeffs = sum(coefficients)
    moyenne = total_notes / total_coeffs

    # Déterminer l'admission
    if moyenne < 8:
        result = 'Refusé'
    elif moyenne <= 10:
        result = 'Rattrapage'
    else:
        result = 'Admis'

    # Déterminer la mention si l'admission est réussie
    if moyenne >= 10:
        if moyenne < 12:
            mention = 'Passable'
        elif moyenne < 14:
            mention = 'Assez bien'
        elif moyenne < 16:
            mention = 'Bien'
        elif moyenne < 18:
            mention = 'Très bien'
        else:
            mention = 'Félicitations du jury'
        return [moyenne, result, mention]

    return [moyenne, result]

# Tests
print(examen(1, 2, 3, 4)) # [2.75, 'Refusé']
print(examen(7, 8, 9, 10)) # [8.75, 'Rattrapage']
print(examen(10, 11.5, 12, 10)) # [10.6875, 'Admis', 'Passable']
print(examen(10, 12, 13, 14)) # [12.5, 'Admis', 'Assez bien']
print(examen(11, 18, 13, 16)) # [14.25, 'Admis', 'Bien']
print(examen(18.5, 13, 15.5, 16)) # [16.125, 'Admis', 'Très bien']
print(examen(19, 18.5, 19.5, 20)) # [19.4375, 'Admis', 'Félicitations du jury']"""

#==================================================================================================================================================

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


"""def calculer(operation, a, b = None):
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

"""def demander_calcul():
    a = int(input("Entrez le premier nombre : "))
    b = int(input("Entrez le deuxième nombre : "))
    operation = input("Entrez l'opération (+, -, *, /) : ")
    if operation == "/" and a == 0 or b == 0:
        print("Le résultat de ", float(a), operation, float(b), "est : ", (calculer(operation,a,b)))
    else:
        print("Le résultat de ", float(a), operation, float(b), "est : ", float(calculer(operation,a,b)))"""

#demander_calcul()

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
"""def calculer(operation, a, b: None):
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

def racine_carree(a):
    return math.sqrt(a)

def modulo(a, b):
    return a % b"""

# Exercice 5 :

def calculer2(cal):
    elements = cal.split()
    nombre1 = float(elements[0])
    operateur = (elements[1])
    nombre2 = float(elements[2])

    if operateur == "+":
        resultat = addition(nombre1,nombre2)
    elif operateur == "-":
        resultat = soustraction(nombre1,nombre2)
    elif operateur =="*":
        resultat = multiplication(nombre1,nombre2)
    elif operateur == "/":
        resultat = division(nombre1,nombre2)
    elif operateur == "^":
        resultat = puissance(nombre1, nombre2)
    elif operateur == "%":
        resultat = modulo(nombre1,nombre2)
    else:
        return "Opérateur non reconnu."
    print("Le résultat de ", nombre1, operateur, nombre2, "est : ",resultat)

calculer2("2 ^ 3")
calculer2("5.4 + 16")
calculer2("11 % 2")

# Exercice 6 :

"""def est_pair(n):
    if n % 2 == 0:
        n = True
    else:
        n = False
    return n"""

def est_pair(n):
    reste = calculer2(n % 2)
    return reste == 0


print(est_pair(4))
print(est_pair(7))


def afficher_parite():
    n = int(input("Entrez un nombre entier : "))
    if est_pair(n):
        print("Le nombre", n, "est pair.")
    else:
        print("Le nombre", n, "est impair.")

#afficher_parite()

# Test

"""print(calculer("^", 2, 3))
print(calculer("sqrt", 16))
print(calculer("%", 10, 3))
print(calculer("sqrt", -9))"""