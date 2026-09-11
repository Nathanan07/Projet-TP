# Exercice 1
def dividende(dividende, diviseur ):
    if diviseur == 0:
    print("Erreur : division par zéro impossible.")
    else:
        # Vérification de la divisibilité
        if dividende % diviseur == 0:
            print(dividende,"est divisible par",diviseur)
        else:
            print(dividende,"n’est pas divisible par",diviseur)

# Exercice 2
"""nbr_eleves = int(input("Entrez le nombre d'élèves : "))
jour = int(input("Entrez le nombre de jours : "))
if nbr_eleves <= 25:
    ct = 110
else:
    ct = 100
cn = 3.50 * jour

if nbr_eleves < 20 :
    ch = 4.20 * jour 
elif 20 <= nbr_eleves <= 35 :
    ch = 3.80 * jour
else:
    ch = 4.00 * jour
co_to = ct + ch + cn

print("Le prix du voyage revient à",co_to,"euros à par élève.")"""

# Exercice 3
"""seance = int(input("Entrez le nombre de séance : "))
tarif_A = 145 + 10.50 * seance
tarif_B = 15.50 * seance
if tarif_A < tarif_B :
    avantage = "A"
    mess = print("Pour",seance,"séances le tarif A est le plus avantageux.")
elif tarif_B < tarif_A :
    avantage = "B"
    mess = print("Pour",seance,"séances le tarif B est le plus avantageux.")
else:
    avantage = "egal"
    mess = print("Pour",seance,"aucun tarif n'est plus avantageux que l'autre.")

print(mess)

detail = input("Souhaitez-vous plus de détails? (yes/no) : ")
if detail == "yes" :
    print("Tarif A : ",tarif_A,"euro.")
    print("Tarif B : ",tarif_B,"euro.")"""

# Exercice 4 
"""
AB = float(input("Premier côté : "))
BC = float(input("Deuxième côté : "))
AC = float(input("Troisième côté : "))

if AB != BC != AC or BC != AC != AB or AB != AC != BC:
    print("> Les longueurs fournies ne forment pas un triangle valide.")

if AB == BC == AC :
    print("> C'est un triangle équilatéral.")

if AB == BC != AC or BC == AC != AB or AB == AC != BC:
    print("> C'est un triangle isocèle.")

if AB != BC and BC != AC and AB != AC : 
    print("> C'est un triangle scalène.")
"""
# Exercice 5

"""type_de_client = input("Type de client (nouveau, standard ou fidèle) : ")
montant = float(input("Montant du panier : "))
Periode_de_soldes = input("Période de soldes ? (oui ou non) : ")
reduction = 1
if type_de_client == "nouveau" :
    reduction = 0.95
elif type_de_client == "standard" :
    reduction = 0
elif type_de_client == "fidèle" :
    reduction = 0.90
else :
    print("Vous avez du faire une erreur d'orthographe")"""

"""total_p = 

if total_p<100:
    reduction =reduction
elif 100<=total_p<=250:
    reduction=reduction-0.05
elif total_p>250:
    reduction =reduction-0.15

if solde=="oui":
    reduction = reduction -0.2
elif solde=="non":
    reduction = reduction 
else :
    print("vous avec du faire une erreur d'orthographe")


pf = total_p*  reduction

if pf<150 :
    pf+=10


print("le prix a payer est de",round(pf) ,"vous avez obtenu",round(100-reduc*100),"% de reduction et votre montant de base était de",total_p,"euro")
"""