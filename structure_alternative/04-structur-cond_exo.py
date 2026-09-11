# ------------------------- EXERCICE 01 --------------------------------------------
# Exercice Python : Gestion de données pour une entreprise tech

# CONTEXTE :
# La société TechNova gère une liste de produits technologiques avec leurs prix et leur disponibilité.
# Vous allez manipuler ces données à travers plusieurs parties, en utilisant des variables, des listes et des conditions.

# PARTIE 1 : Initialisation des données
# On dispose de trois listes : noms des produits, prix, et disponibilité (True = en stock, False = rupture).

# produits: "Clavier sans fil", "Souris ergonomique", "Écran 27 pouces", "Webcam HD"
# prix : 49.99, 35.50, 229.90, 59.99
# disponibilite

# PARTIE 2 : Affichage d'informations sur un produit donné
# Choisissez un produit (par son indice) et affichez son nom, son prix et sa disponibilité.

# On choisit la souris ergonomique

# PARTIE 3 : Vérification d'un panier client
# Un client souhaite acheter un écran et une webcam.
# Vérifiez si les deux produits sont disponibles et affichez le montant total si c'est possible.


# PARTIE 4 : Application d'une remise spéciale
# Si le prix total du panier dépasse 250 euros, appliquez une remise de 10% et affichez le nouveau montant.


# ----------------------------- EXERCICE 02 -----------------------------------------
# Exercice Python : Gestion d'une bibliothèque en ligne (version sans boucles ni fonctions)

# CONTEXTE :
# La bibliothèque BookWorld souhaite gérer ses livres, leurs auteurs, leur disponibilité et permettre aux clients d'emprunter ou de rendre des livres.
# Vous allez manipuler des listes, des dictionnaires et des conditions, mais sans utiliser de boucles ni de fonctions.

# PARTIE 1 : Initialisation des données
# "1984", "Le Petit Prince", "Python pour les Nuls", "L'Étranger", "Le Seigneur des Anneaux"
# "George Orwell", "Antoine de Saint-Exupéry", "John Paul Mueller", "Albert Camus", "J.R.R. Tolkien"
# disponibilite des livres

# PARTIE 2 : Affichage de tous les livres disponibles (sans boucle)


# PARTIE 3 : Emprunt d'un livre par un client


# PARTIE 4 : Retour d'un livre


# PARTIE 5 : Affichage du catalogue complet avec statut (sans boucle)


# PARTIE 6 : Recherche de livres par auteur (exemple avec "George Orwell")


# PARTIE 7 : Statistiques (sans boucle)

# -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ Exercice 1 -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Exercice Python : Gestion de données pour une entreprise tech

# CONTEXTE :
# La société TechNova gère une liste de produits technologiques avec leurs prix et leur disponibilité.
# Vous allez manipuler ces données à travers plusieurs parties, en utilisant des variables, des listes et des conditions.

# PARTIE 1 : Initialisation des données
# On dispose de trois listes : noms des produits, prix, et disponibilité (True = en stock, False = rupture).

# produits: "Clavier sans fil", "Souris ergonomique", "Écran 27 pouces", "Webcam HD"
# prix : 49.99, 35.50, 229.90, 59.99
# disponibilite

# PARTIE 2 : Affichage d'informations sur un produit donné
# Choisissez un produit (par son indice) et affichez son nom, son prix et sa disponibilité.

# On choisit la souris ergonomique

# PARTIE 3 : Vérification d'un panier client
# Un client souhaite acheter un écran et une webcam.
# Vérifiez si les deux produits sont disponibles et affichez le montant total si c'est possible.


# PARTIE 4 : Application d'une remise spéciale
# Si le prix total du panier dépasse 250 euros, appliquez une remise de 10% et affichez le nouveau montant.

nom_des_produits = [["Clavier sans file",49.99, False], 
                    ["Souris ergonomique",35.50,True], 
                    ["Écran 27 pouces",229.90,True], 
                    ["Webcam HD",59.99,True]
                    ]
print(nom_des_produits)

aff = int(input("Saisisez vos articles : "))
if aff == 0 :
    print(nom_des_produits[0])
if aff == 1 :
    print(nom_des_produits[1])
if aff == 2 :
    print(nom_des_produits[2])
if aff == 3 :
    print(nom_des_produits[3])
if aff == disponible :
    print(nom_des_produits[1:4])


panier_client = 
