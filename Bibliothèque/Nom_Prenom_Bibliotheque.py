#### Bibliotheque

## Exercice 1
def creer_livre(titre, auteur, annee):
    return [titre, auteur, annee]

# Exemple
print(f"\n  1. Création de deux livres")
livre1 = creer_livre("Les Misérables", "Victor Hugo", 1862)
livre2 = creer_livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
print(livre1)
print(livre2)

## Exercice 2
def ajouter_livre(bibliotheque, livre):
    bibliotheque.append(livre)
    return bibliotheque

# Exemple

print(f"\n  2. Ajout de deux livres dans la bibliotheque")

livre1 = ["Le Petit Prince", "Antoine de Saint-Exupéry", 1943]
livre2 = ["1984", "George Orwell", 1949]

bibliotheque = []
bibliotheque = ajouter_livre(bibliotheque, livre1)
bibliotheque = ajouter_livre(bibliotheque, livre2)

print(bibliotheque)



## Exercice 3
def afficher_livre(livre):
    print(f"Titre : {livre[0]}, Auteur : {livre[1]}, Année : {livre[2]}")
    

# Exemple
print(f"\n  3. Afficher les deux livres")
afficher_livre(livre1)
afficher_livre(livre2)


## Exercice 4
def afficher_bibliotheque(bibliotheque):
    for livre in bibliotheque:
        afficher_livre(livre)

# Exemple 
print(f"\n  4. Afficher la bibliothèque")
afficher_bibliotheque(bibliotheque)


## Exercice 5
def rechercher_par_titre(bibliotheque, titre):
    for livre in bibliotheque:
        if livre[0] == titre:
            return livre
    return None

# Exemple
print(f"\n  5. Rechercher un livre par son titre")
livre_recherche = rechercher_par_titre(bibliotheque, titre="Les Misérables")
print(livre_recherche)
livre_recherche = rechercher_par_titre(bibliotheque, titre="Zola")
print(livre_recherche)



## Exercice 6
def supprimer_par_titre(bibliotheque, titre):
    nouvelle_bibliotheque = []
    for livre in bibliotheque:
        if livre[0] != titre:
            nouvelle_bibliotheque.append(livre)
    return nouvelle_bibliotheque

# Exemple
print(f"\n  6. Supprimer un livre par son titre")
print(supprimer_par_titre(bibliotheque, titre="Zola"))
print(supprimer_par_titre(bibliotheque, titre="Le Petit Prince"))


## Exercice 7
def modifier_livre(bibliotheque, titre, champ,
nouvelle_valeur):
    champs = {"titre": 0, "auteur": 1, "annee": 2}

    if champ not in champs:
        print("Erreur : champ invalide (utilisez 'titre', 'auteur' ou 'annee').")
        return bibliotheque

    for livre in bibliotheque:
        if livre[0] == titre:
            livre[champs[champ]] = nouvelle_valeur
            return bibliotheque

    print("Erreur : livre non trouvé.")
    return bibliotheque

# Exemple 
print(f"\n  7. Modifier un livre")
bibliotheque_modifiee = modifier_livre(bibliotheque, "Les Misérables", "annee", 1865)
biblibibliotheque_modifieeotheque = modifier_livre(bibliotheque, "Les Misérables", "auteur", "Victor hugo")
print(bibliotheque_modifiee)


## Exercice 8
def compter_livres_par_auteur(bibliotheque, auteur):
    compteur = 0
    for livre in bibliotheque:
        if livre[1] == auteur:
            compteur += 1
    return compteur

# Exemple
print(f"\n  8. Compter livres d'un auteur")
nombre_livres = compter_livres_par_auteur(bibliotheque, "Antoine de Saint-Exupéry")
print(nombre_livres)




## Exercice 9
def lister_auteurs(bibliotheque):
    auteurs = []
    for livre in bibliotheque:
        auteur = livre[1]
        if auteur not in auteurs:
            auteurs.append(auteur)
    return auteurs

# Exemple
print(f"\n  9. Liste des auteurs")
auteurs = lister_auteurs(bibliotheque)
print(auteurs)



## Exercice 10
def livres_par_auteur(bibliotheque, auteur):
    livres_auteur = []
    for livre in bibliotheque:
        if livre[1] == auteur:
            livres_auteur.append(livre)
    return livres_auteur

# Exemple 
print(f"\n  10. Liste des livres d'un auteur")
livres_hugo = livres_par_auteur(bibliotheque, auteur="Victor Hugo")
print(livres_hugo)



## Exercice 11
def nombre_total_de_livres(bibliotheque):
    return len(bibliotheque)

# Exemple 
print(f"\n  11. Nombre de livres dans la bibliothèque")
total_livres = nombre_total_de_livres(bibliotheque)
print(total_livres)



## Exercice 12
def trier_bibliotheque(bibliotheque, critere):
    criteres = {
        "titre": 0,
        "auteur": 1,
        "annee": 2
    }

    if critere not in criteres:
        print("Erreur : critère invalide (utilisez 'titre', 'auteur' ou 'annee').")
        return bibliotheque

    return sorted(bibliotheque, key=lambda livre: livre[criteres[critere]])


# Exemple
print(f"\n  12. Tries de la bibliothèque")
bibliotheque_triee = trier_bibliotheque(bibliotheque, "titre")
print(bibliotheque_triee)

bibliotheque_triee = trier_bibliotheque(bibliotheque, "annee")
print(bibliotheque_triee)



## Exercice 13
def liste_actions_bibliotheque():
    print("\n=== Actions possibles ===")
    print("1. Afficher le contenu de la bibliothèque")
    print("2. Modifier la bibliothèque")
    print("3. Rechercher un livre")

    choix = int(input("Entrez le numéro de votre choix : "))

    if choix not in [1, 2, 3]:
        print("Erreur : choix invalide.")
        return None

    return choix

# Exemple
print(f"\n  13. liste des actions")
choix = liste_actions_bibliotheque()        # Faire plusieurs tests
print(choix)



## Exercice 14

def afficher_contenu_bibliotheque(bibliotheque):
    print("\nQue souhaitez-vous afficher ?")
    print("1. Nombre de livres dans la bibliothèque")
    print("2. Liste des livres")
    print("3. Liste des auteurs")

    choix = int(input("Votre choix : "))

    # 1. Nombre total de livres
    if choix == 1:
        total = nombre_total_de_livres(bibliotheque)
        print(f"\nNombre total de livres : {total}")

    # 2. Liste des livres (avec ou sans tri)
    elif choix == 2:
        reponse = input("Souhaitez-vous trier la bibliothèque ? (oui/non) : ")

        if reponse.lower() == "oui":
            critere = input("Trier par (titre / auteur / annee) : ")
            bibliotheque_triee = trier_bibliotheque(bibliotheque, critere)
            afficher_bibliotheque(bibliotheque_triee)
        else:
            afficher_bibliotheque(bibliotheque)

    # 3. Liste des auteurs + nombre de livres par auteur
    elif choix == 3:
        auteurs = lister_auteurs(bibliotheque)
        print("\nListe des auteurs :")
        for auteur in auteurs:
            nb_livres = compter_livres_par_auteur(bibliotheque, auteur)
            print(f"- {auteur} : {nb_livres} livre(s)")

    # Choix invalide
    else:
        print("Erreur : choix invalide.")

# Exemple
print(f"\n  14. Action Afficher")
afficher_contenu_bibliotheque(bibliotheque)    # Faire plusieurs tests



## Exercice 15
def modifier_bibliotheque(bibliotheque):
    print("\n=== Modifier la bibliothèque ===")
    print("1. Ajouter un livre")
    print("2. Supprimer un livre")
    print("3. Modifier un livre")

    choix = int(input("Entrez votre choix : "))

    # 1. Ajouter un livre
    if choix == 1:
        titre = input("Titre du livre : ")
        auteur = input("Auteur du livre : ")
        annee = int(input("Année de publication : "))

        livre = creer_livre(titre, auteur, annee)
        ajouter_livre(bibliotheque, livre)
        print("📘 Livre ajouté avec succès.")

    # 2. Supprimer un livre
    elif choix == 2:
        titre = input("Titre du livre à supprimer : ")
        bibliotheque[:] = supprimer_par_titre(bibliotheque, titre)
        print("🗑️ Livre supprimé (s'il existait).")

    # 3. Modifier un livre
    elif choix == 3:
        titre = input("Titre du livre à modifier : ")
        champ = input("Champ à modifier (titre / auteur / annee) : ")
        nouvelle_valeur = input("Nouvelle valeur : ")

        # Conversion si l'année est modifiée
        if champ == "annee":
            nouvelle_valeur = int(nouvelle_valeur)

        modifier_livre(bibliotheque, titre, champ, nouvelle_valeur)

    # Choix invalide
    else:
        print("❌ Erreur : choix invalide.")

    return bibliotheque

# Exemple
print(f"\n  15. Action Modifier")
modifier_bibliotheque(bibliotheque)    # Faire plusieurs tests
print(bibliotheque)




## Exercice 16

def rechercher_livre_utilisateur(bibliotheque):
    print("\n=== Rechercher un livre ===")
    print("1. Rechercher par titre")
    print("2. Rechercher par auteur")

    choix = int(input("Votre choix : "))

    # Recherche par titre
    if choix == 1:
        titre = input("Entrez le titre du livre : ")
        livre = rechercher_par_titre(bibliotheque, titre)

        if livre:
            afficher_livre(livre)
        else:
            print("Livre non trouvé.")

    # Recherche par auteur
    elif choix == 2:
        auteur = input("Entrez le nom de l'auteur : ")
        livres = livres_par_auteur(bibliotheque, auteur)

        if livres:
            print(f"\nLivres de {auteur} :")
            for livre in livres:
                afficher_livre(livre)
        else:
            print("Aucun livre trouvé pour cet auteur.")

    else:
        print("Erreur : choix invalide.")

# Exemple
print(f"\n  16. Action Rechercher")
rechercher_livre_utilisateur(bibliotheque)    # Faire plusieurs tests




## Exercice 17
def actions_bibliotheque(bibliotheque):
    choix = liste_actions_bibliotheque()

    # 1. Afficher le contenu
    if choix == 1:
        afficher_contenu_bibliotheque(bibliotheque)

    # 2. Modifier la bibliothèque
    elif choix == 2:
        modifier_bibliotheque(bibliotheque)

    # 3. Rechercher un livre
    elif choix == 3:
        rechercher_livre_utilisateur(bibliotheque)

# Exemple
print(f"\n  17. Fonction principale")
actions_bibliotheque(bibliotheque)    # Faire plusieurs tests

