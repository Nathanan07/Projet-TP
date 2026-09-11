# Exercice 1 :

"""code_pin=4567
cd=int(input("Entrer le code PIN : "))
if cd != code_pin :
    print("code incorrect")
else:
    print("code correct")"""

# Exercice 2 :

"""nbr=int(input("Saisissez un nombre entier : "))
if nbr > 0 :
    print("Positif")
if nbr < 0 :
    print("Négatif")
if nbr == 0 :
    print("Nul")"""

# Exercice 3 :

"""nbr_entier = int(input("Entrez un nombre entier : "))
if nbr_entier % 2 == 0 :
    print("pair")
else:
    print("impair")"""

# Exercice 4 :

"""age = int(input("Saisissez votre age : "))
if age < 12 :
    print("enfant")
elif age < 18 :
    print("adolescent")
if age >= 18 :
    print("adulte")"""

# Exercice 5 :

"""Prix_de_fabrication = float(input("Entrez le prix de fabrication : "))
Prix_de_vente = float(input("Entrez le prix de vente : "))
if Prix_de_fabrication > Prix_de_vente :
    print("perte")
else:
    print("profit")"""

# Exercice 6 :

"""pn = float(input("Saisir le premier nombre : "))
dn = float(input("Saisir le deuxieme nombre : "))
tn = float(input("Saisir le troisième nombre : "))

if pn >= dn and pn >= tn:
    print("Le maximum est le pn nombre", pn)
elif dn >= pn and dn >= tn:
    print("Le maximum est le dn nombre", dn)
else:
    print("Le maximum est le troisième nombre", tn)"""

# Exercice 7 :

"""cote1 = int(input("côté 1 : "))
cote2 = int(input("côté 2 : "))
cote3 = int(input("côté 3 : "))

if cote1 <= cote2 and cote2 <= cote3 :
    if cote3**2 == (cote1**2 + cote2**2) :
        print("triangle rectangle")
    else:
        print("triangle non rectangle")
else:
    print("N'est pas dans ordre croissant")"""

# Exercice 8 :

"""année = int(input("Saisir une année : "))

if (année % 4 == 0 and année % 100 != 0) or (année % 400 == 0):
    print("Année bissextile")
else:
    print("Année non bissextile")"""

# Exercice 9 :

"""ages = int(input("Saisir votre âge : "))
if ages > 21 and ages < 51 :
    print("Le prix du transport est de 10 euro.")
elif ages >= 51 :
    print("Le prix du transport est de 9 euro.")
elif ages >= 16 and ages <= 21 :
    print("Le prix du transport est de 6 euros.")
elif ages >= 6 and ages < 16 :
    print("Le prix du transport est de 5 euros.")
elif ages < 6 and ages >= 0 :
    print("Le prix du transport est gratuit.")"""
