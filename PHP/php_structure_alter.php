<?php
# Exercice 1 :

function calculerPrixBillet(int $age) {
    if ($age < 5) {
        return "Gratuit";
    } elseif ($age >= 5 && $age <= 12) {
        return "Tarif réduit : 10€";
    } elseif ($age >= 13 && $age <= 59) {
        return "Tarif normal : 20€";
    } elseif ($age >= 60) {
        return "Tarif senior : 15€";
    }
}

echo(calculerPrixBillet(3)."\n");
echo(calculerPrixBillet(6)."\n");
echo(calculerPrixBillet(30)."\n");
echo(calculerPrixBillet(80)."\n");

# Exercice 2 

function calculerPrixLocation($jours) {
    if ($jours >= 1 && $jours <= 3) {
        return "50€\jour";
    } elseif ($jours >= 4 && $jours <= 7) {
        return "45€\jour";
    }elseif ($jours <= 8) {
        return "40€\jour";
    }elseif($jours >= 10) {
        return "réduction de 10% sur le total";
    }
}

echo(calculerPrixLocation(3)."\n");
echo(calculerPrixLocation(6)."\n");
echo(calculerPrixLocation(8)."\n");
echo(calculerPrixLocation(11)."\n");

# Exercice 3

function calculerBonus(int $anciennete,int $performance,int $salaire) {
    if ($anciennete < 2) {
        return "Aucun bonus salaire = $salaire.";
    } elseif ($anciennete < 5) {
        if ($performance < 4){
            return "Salaire total avec bonus  de 6% : " . $salaire+$salaire*0.06;
        }
        elseif ($performance <= 5) {
            return "Salaire total avec bonus  de 9% : " . $salaire+$salaire*0.09;
        }
    } elseif ($anciennete >= 5) {
        if ($performance < 4) {
            return "Salaire total avec bonus  de 8% : " . $salaire+$salaire*0.08;
        }
        elseif ($performance <= 5) {
            return "Salaire total avec bonus  de 12% : " . $salaire+$salaire*0.12;
        }
    }
}

echo(calculerBonus(1,2,1800)."\n");
echo(calculerBonus(2,1,2000)."\n");
echo(calculerBonus(3,4,2400)."\n");
echo(calculerBonus(5,5,2800)."\n");
echo(calculerBonus(7,3,3000)."\n");

# Exercice 4 
function calculer(int $a, int $b, string $operation) {
    if ($operation == "add") {
        return "$a + $b = ".($a+$b);
    }
    elseif ($operation == "sub") {
        return "$a - $b = ".($a-$b);
    }
    elseif ($operation == "mul") {
        return "$a x $b = ".($a*$b);
    }
    elseif ($operation == "div") {
        if ($b != 0) {
            return "$a / $b = ".($a/$b);
        } else {
            return "Erreur : division par 0 ";
            }
    }
    else {
        return "Opération invalide.";
    }
}

echo(calculer(5,8,'add')."\n");
echo(calculer(5,8,'sub')."\n");
echo(calculer(5,8,'mul')."\n");
echo(calculer(5,8,'div')."\n");
echo(calculer(5,0,'div')."\n");
echo(calculer(5,8,'ok')."\n");

# Exercice 5
function calculerFraisLivraison($mode, $montantTotal) {
    if ($mode == "standard") {
        return "5€";
    } elseif ($mode == "express") {
        return "10€";
    } elseif ($mode == "premium") {
        return "15€";
    } elseif ($mode == "gratuit") {
        if ($montantTotal >= 100) {
            return "Gratuit";
        } else {
            return "Commande insuffisante pour la livraison gratuite.";
        }
    } else {
        return "Mode de livraison invalide.";
    }
}

echo(calculerFraisLivraison('standard',15)."\n");
echo(calculerFraisLivraison('express',22)."\n");
echo(calculerFraisLivraison('premium',37)."\n");
echo(calculerFraisLivraison('gratuit',120)."\n");
echo(calculerFraisLivraison('gratuit',89)."\n");
echo(calculerFraisLivraison('mzegoat',15)."\n");

?>