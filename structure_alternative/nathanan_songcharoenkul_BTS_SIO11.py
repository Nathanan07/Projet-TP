#ex1
"""liste1 = list(range(10,15))
var = 0
var2 = 10
print(liste1[2])
print(liste1[var])
print(liste1[var2])
print(liste1["var"])"""

#ex2
"""liste_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
print(liste_semaine[0])
print(liste_semaine[-7])
print(liste_semaine[5:7])
print(liste_semaine[-2:])
liste_semaine.reverse()
print(liste_semaine)"""

#ex3
"""liste = list(range(11))
print(liste)

liste3 = [i for i in range(11)]
print(liste3)

liste2 = []
for i in range(11):
    liste2.append(i)
print(liste2)

liste.remove(3)
print(liste)

liste.insert(3 ,3)
print(liste)

liste.append(11)
print(liste)

liste.reverse()
print(liste)

liste.sort(reverse = True)
print(liste)

print(min(liste))
print(max(liste))
print(sum(liste))

print(5 in liste)

liste.clear()
print(liste)"""

#ex4
"""Année = [["Janvier", 1],
    ["Février", 2],
    ["Mars", 3],
    ["Avril", 4],
    ["Mai", 5],
    ["Juin", 6],
    ["Juillet", 7],
    ["Août", 8],
    ["Septembre", 9],
    ["Octobre", 10],
    ["Novembre", 11],
    ["Décembre", 12]
]

print(Année[3])

print(Année[3][0])"""

#ex5
"""lettres = ["a","a","b","d","e","a","c","b","e","d"]

occurence_a = lettres.count("a")
print(occurence_a)

lettres_string = ":".join(lettres)
print(lettres_string)

lettres_reconverties = lettres_string.split(":")
print(lettres_reconverties)

# exo 6
hiver = ["Décembre", "Janvier", "Février"]
print("hiver:", hiver)

printemps = ["Mars", "Avril", "Mai"]
print("printemps:", printemps)

été = ["Juin", "Juillet", "Août"]
print("été:", été)

automne = ["Septembre", "Octobre", "Novembre"]
print("automne:", automne)

saisons = [hiver, printemps, été, automne]
print("saisons:", saisons)

print(saisons[2])
print(saisons[1][0])
print(saisons[1:2])
print(saisons[:][1])"""

#exo 7
"""print(list(range(9,82,9)))"""

#exo 8
"""nombres_pairs = list(range(2,10000,2))
print(len(nombres_pairs))"""

# exo 10
chiens = ["labrador", "rottweiler", "dalmatien", "caniche"]
print(chiens)
print(chiens[0])
print(chiens[1])
print(chiens[-1])
print(chiens[2 : 4])
print(chiens[0 : 3 : 2])

 
chat = []
chat = ["persan", "siamois", "ragdoll"]
chat.insert(3, "bengal")
chat.remove("siamois")
chat.insert(2, "sphynx")
del chat[1]
print(chat)

 

animaux = chiens + chat 
print(animaux)
animaux.reverse()
print(animaux)
animaux.sort(reverse = True)
print(animaux)
indice_dalmatien = animaux.index("dalmatien")
print(indice_dalmatien)
print("persan" in animaux)
racesChiens = ";" .join(chiens)
Chien = racesChiens.split(";")
animaux.clear()
print(animaux)
print(racesChiens)
print(Chien)


liste1 = list(range(6))
print(liste1)

liste2 = list(range(1,8,2))
print(liste2)

liste3 = list(range(4,7))
print(liste3)

chiffres = liste1 + liste2 + liste3
print(chiffres) 

print(len(chiffres))
print(max(chiffres))
print(sum(chiffres))
print(chiffres.count(5))

Capitales = [["France","Paris"],["Espagne","Madrid"],["Angleterre","Londres"]]
print(Capitales[2])

print(Capitales[1][0])

