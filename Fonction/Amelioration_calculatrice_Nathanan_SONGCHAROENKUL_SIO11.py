# TP_Calculatrice_Amélioration

from math import *

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
    elif operation == "^":   
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
        # Cas pair : moyenne des deux valeurs du milieu
        milieu1 = liste_triee[n//2 - 1]
        milieu2 = liste_triee[n//2]
        return (milieu1 + milieu2) / 2
    else:
        # Cas impair : valeur du milieu
        return liste_triee[n//2]
    
# Amélioration avec un affichage menu dans la console :

def menu():
    while True:
        print("\n=== CALCULATRICE ===")
        print("1. Addition (+)")
        print("2. Soustraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Puissance (^)")
        print("6. Racine carrée (sqrt)")
        print("7. Modulo (%)")
        print("8. Parité (pair/impair)")
        print("9. Médiane d'une liste")
        print("0. Quitter")
        
        choix = input("Choisissez une option : ")

        if choix == "0":
            print("Au revoir !")
            break

        # Opérations à 2 nombres
        if choix in ["1","2","3","4","5","7"]:
            try:
                a = float(input("Premier nombre : "))
                b = float(input("Deuxième nombre : "))
            except ValueError:
                print("Entrée invalide.")
                continue

            if choix == "1":
                resultat = addition(a,b)
            elif choix == "2":
                resultat = soustraction(a,b)
            elif choix == "3":
                resultat = multiplication(a,b)
            elif choix == "4":
                resultat = division(a,b)
            elif choix == "5":
                resultat = puissance(a,b)
            elif choix == "7":
                resultat = modulo(a,b)

            print(f"Résultat : {resultat}")

        # Opérations à 1 nombre
        elif choix == "6":
            try:
                a = float(input("Entrez un nombre : "))
            except ValueError:
                print("Entrée invalide.")
                continue
            resultat = racine_carree(a)
            print(f"Résultat : {resultat}")

        elif choix == "8":
            try:
                n = int(input("Entrez un entier : "))
            except ValueError:
                print("Entrée invalide.")
                continue
            if est_pair(n):
                print(f"Le nombre {n} est pair.")
            else:
                print(f"Le nombre {n} est impair.")

        elif choix == "9":
            liste_str = input("Entrez les nombres séparés par des espaces : ")
            try:
                liste = [float(x) for x in liste_str.split()]
            except ValueError:
                print("Entrée invalide.")
                continue
            resultat = calculer_mediane(liste)
            print(f"Résultat : {resultat}")

        else:
            print("Option invalide, réessayez.")


menu()