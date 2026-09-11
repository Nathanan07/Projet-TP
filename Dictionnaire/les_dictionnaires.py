# Cours sur les dictionnaires en Python

# 1. Définition
# Un dictionnaire est une structure de données qui associe des clés à des valeurs.

# 2. Création d'un dictionnaire
mon_dictionnaire = {
    "nom": "Dupont",
    "age": 30,
    "ville": "Paris"
}

# 3. Accès à une valeur
print(mon_dictionnaire["nom"])  # Affiche 'Dupont'

# 4. Ajout ou modification d'une entrée
mon_dictionnaire["profession"] = "Ingénieur"
mon_dictionnaire["age"] = 31  # Modifie la valeur associée à la clé 'age'

# 5. Suppression d'une entrée
del mon_dictionnaire["ville"]

# 6. Parcourir un dictionnaire
for cle, valeur in mon_dictionnaire.items():
    print(f"{cle} : {valeur}")

# 7. Méthodes utiles
cles = mon_dictionnaire.keys()      # Liste des clés
valeurs = mon_dictionnaire.values() # Liste des valeurs
items = mon_dictionnaire.items()    # Liste des paires (clé, valeur)

# 8. Vérifier la présence d'une clé
if "nom" in mon_dictionnaire:
    print("La clé 'nom' existe.")

# 9. Dictionnaire imbriqué
etudiants = {
    "alice": {"age": 22, "note": 15},
    "bob": {"age": 23, "note": 17}
}
print(etudiants["alice"]["note"])   # Affiche 15

# 10. Créer un dictionnaire vide
dico_vide = {}

# 11. Exemples d'utilisation
# Compter les occurrences de lettres dans un mot
mot = "python"
compte = {}
for lettre in mot:
    if lettre in compte:
        compte[lettre] += 1
    else:
        compte[lettre] = 1
print(compte)

