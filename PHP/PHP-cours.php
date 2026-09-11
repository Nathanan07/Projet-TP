# 3.1. Exercices : variables et conditions
# 3.1.1. bonjour
# a

<?php
$name = (string)readline("Bonjour ")
?>

# b

<?php
$a = (int)readline("Entrez un nombre : ") ;
$b = (int)readline("Entrez un nombre : ") ;

echo("$a+$b=".($a+$b)."\n") ; 
echo("$a-$b=".($a-$b)."\n") ; 
echo("$a*$b=".($a*$b)."\n") ; 
echo("$a/$b=".($a/$b)."\n") ; 

?>

# 3.1.2. tarif réduit

<?php
$age = (int)readline("Entrez votre age : ") ;
if ($age < 26) {
    echo("Vous avez droit au tarif réduit \n");
}
elseif ($age > 65) {
    echo("Vous avez droit au tarif réduit également \n");
}
else {
    echo("Vous n'avez pas pas droit au tarif réduit \n");
}
?>

# 3.1.3. départements

<?php
$departementsIdf = array(75, 77, 78, 91, 92, 93, 94);
$departement = (int)readline("Veuillez entrer un numéro de département (entre 1 et 99) : ");
if ($departement < 1 || $departement > 99) {
    echo "Le numéro de département doit être compris entre 1 et 99. Veuillez réessayer.\n";
}

if (in_array($departement, $departementsIdf)) {
    echo "Le département $departement fait partie de l'Île-de-France.\n";
} 
else {
    echo "Le département $departement ne fait pas partie de l'Île-de-France.\n";
}
?>

# 3.1.4. produit

<?php

// Saisie des deux nombres
$nombre1 = (int) readline("Entrez le premier nombre : ");
$nombre2 = (int) readline("Entrez le deuxième nombre : ");

// Vérification du signe du produit (sans calculer le produit)
if (
    ($nombre1 > 0 && $nombre2 > 0) ||
    ($nombre1 < 0 && $nombre2 < 0)
) {
    echo "Le produit est positif.\n";
} else { 
    echo "Le produit est négatif.\n";
}

?>

# 3.1.5. racine carrée

<?php
$nbr1 = (float) readline("Entrez le premier nombre positif: ");
$nbr2 = (float) readline("Entrez le deuxième nombre positif: ");

if ($nbr1 > 0 || $nbr2 > 0) {
    echo("$nbr1*$nbr2=".sqrt(($nbr1*$nbr2))."\n") ;
}
else {
    echo "Erreur. \n";
}
?>

# 3.1.6. bissextile

<?php
$année = (int) readline("Saisir une année : ");

if ( ($année % 4 == 0 && $année % 100 != 0) || ($année % 400 == 0) ) {
    echo "Année bissextile";
}
else {
    echo "Année non bissextile";
}
?>

# 3.2. Les boucles

