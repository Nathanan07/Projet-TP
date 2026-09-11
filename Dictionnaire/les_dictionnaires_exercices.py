# Exercices sur les dictionnaires en Python. testez et affichez les résultats de chaque exercice.

# 1. Créer un dictionnaire vide nommé "mon_dict".

mon_dict = {}
print("1.", mon_dict)


# 2. Ajouter une paire clé/valeur ('nom', 'Alice') à "mon_dict".

mon_dict["nom"] = "Alice"
print("2.", mon_dict)

# 3. Ajouter plusieurs paires ('age', 25), ('ville', 'Paris') à "mon_dict".

mon_dict["age"] = 25
mon_dict["ville"] = "Paris"
print("3.", mon_dict)

# 4. Accéder à la valeur associée à la clé 'nom'.

print("4. nom =", mon_dict["nom"])
# 5. Modifier la valeur associée à la clé 'age' pour qu'elle vaille 30.

mon_dict["age"] = 30
print("5.", mon_dict)

# 6. Supprimer la clé 'ville' du dictionnaire.

del mon_dict["ville"]
print("6.", mon_dict)

# 7. Vérifier si la clé 'nom' existe dans le dictionnaire.

if "nom" in mon_dict:
    print("7. La clé 'nom' existe")

# 8. Parcourir toutes les clés du dictionnaire et les afficher.

print("8. Clés :")
for cle in mon_dict.keys():
    print(cle)

# 9. Parcourir toutes les valeurs du dictionnaire et les afficher.

print("9. Valeurs :")
for valeur in mon_dict.values():
    print(valeur)

# 10. Parcourir toutes les paires clé/valeur et les afficher.

print("10. Paires clé/valeur :")
for cle, valeur in mon_dict.items():
    print(f"{cle} : {valeur}")

# 11. Copier le dictionnaire dans un nouveau dictionnaire "copie_dict".

copie_dict = mon_dict.copy()
print("11. Copie :", copie_dict)

# 12. Fusionner deux dictionnaires : {'a': 1, 'b': 2} et {'b': 3, 'c': 4}.
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
fusion = d1 | d2   # Python 3.9+
print("12. Fusion :", fusion)

# 13. Obtenir la liste des clés du dictionnaire.

liste_cles = list(mon_dict.keys())
print("13. Liste des clés :", liste_cles)

# 14. Obtenir la liste des valeurs du dictionnaire.

liste_valeurs = list(mon_dict.values())
print("14. Liste des valeurs :", liste_valeurs)

# 15. Utiliser la méthode get pour obtenir la valeur de la clé 'prenom', avec une valeur par défaut 'Inconnu'.

prenom = mon_dict.get("prenom", "Inconnu")
print("15. prenom :", prenom)

# 16. Créer un dictionnaire à partir de deux listes : cles = ['x', 'y'], valeurs = [10, 20].
cles = ['x', 'y']
valeurs = [10, 20]
dict_from_lists = dict(zip(cles, valeurs))
print("16.", dict_from_lists)

# 17. Inverser les clés et valeurs d'un dictionnaire {'a': 1, 'b': 2} -> {1: 'a', 2: 'b'}
original = {'a': 1, 'b': 2}
inverse = {v: k for k, v in original.items()}
print("17.", inverse)

# 18. Supprimer toutes les paires du dictionnaire.
mon_dict.clear()
print("18.", mon_dict)

# 19. Compter le nombre d'éléments dans un dictionnaire.
print("19. Nombre d'éléments :", len(mon_dict))

# 20. Créer un dictionnaire de fréquences à partir d'une chaîne "abracadabra".
# un dictionnaire où les clés sont les caractères et les valeurs sont le nombre d'occurrences de chaque caractère.

chaine = "abracadabra"
frequences = {}

for lettre in chaine:
    frequences[lettre] = frequences.get(lettre, 0) + 1

print("20. Fréquences :", frequences)