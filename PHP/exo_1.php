
<?php
    // ==================== Hello World ==================== //
    #echo ("Hellow world");


# ========================= Variables et Conditions ========================= # 
    // ==================== Bonjour ==================== // 
    # Bonjour… qui ?
    /*   
    $name = (string)readline( "Votre nom : ");
    echo"bonjour $name";*/

    # Élémentaire mon cher
    /*
    $x = (float)readline("x = ");
    $y = (float)readline("y = ");

    echo"Somme "."$x + $y = ".($x+$y)."\n";
    echo"Produit "."$x * $y = ".($x*$y)."\n";
    if ($x > $y) {
        echo"Différence "."$x - $y = ".($x-$y)."\n";
    }    
    else { 
        echo"Différence "."$y + $x = ".($y-$x)."\n";
    }

    if ($y == 0){
        echo "Ce n'est pas possible de diviser par 0";
    }
    else {
        echo"Quotient "."$x / $y = ".($x/$y)."\n";
    }*/



    // ====================  tarif réduit ==================== // 
    /*
    $age = (int)readline("Veuillez saisir votre age : ");

    if ($age < 26 or $age > 65) {
        echo "Vous avez droit au tarif réduit". "\n";
    }
    else {
        echo "Vous ne pouvez pas béneficier du tarif". "\n";
    }*/



    // ====================  départements ==================== // 
    /*
    $idf = [75,  77, 78, 91, 92, 93, 94];
    $dmd_dprt =(int)readline("N° Departement : ");

    if ($dmd_dprt >= 1 and $dmd_dprt<=99){
        if (in_array($dmd_dprt, $idf)){
            echo "Cet département fait parti d'IDF"."\n";
        }
        else {
            echo "Cet département est hors d'IDF"."\n";
        }
    }
    else{
        echo "Veuillez saisir un département valide (1-99)"."\n";
    }*/

    
    
    // ====================  produit ==================== // 
    /*
    $nb_1 = (int)readline("Nombre 1 : ");
    $nb_2 = (int)readline("Nombre 2 : ");

    if ($nb_1 < 0 and $nb_2 < 0) {
        echo "chiffre 1 ---> ".$nb_1." chiffre 2 ---> ".$nb_2." produit négatif";
    }
    elseif ($nb_1 >= 0 and $nb_2 >= 0) {
        echo "chiffre 1 ---> ".$nb_1." chiffre 2 ---> ".$nb_2." produit positif";
    }
    elseif ($nb_1 >= 0 and $nb_2 >= 0) {
        echo "chiffre 1 ---> ".$nb_1." chiffre 2 ---> ".$nb_2." produit positif";
    }*/


    
    // ====================  racine carrée ==================== //
    /*
    $a = (int)readline("a = ");
    $b = (int)readline("b = ");

    if ($a >= 0 and $b >= 0) {
        $calcul = ($a*$b);
        echo sqrt($calcul);
    }
    else {
        echo "Erreur";
    }*/

    // ====================  bissextile ==================== //
    /*
    $annee = (int)readline("Saisissez votre année : ");

    if ($annee%100 == 0 ) {
        echo "L'année n'est pas bissextile";
    }
    elseif ($annee%4 == 0 or $annee%400 == 0) {
        echo "L'année est bissextile";
    }
    else {
        echo "L'année n'est pas bissextile";
    }*/


# ========================= Les boucles ========================= #    
    // ====================  Compteur ==================== //
    /*
    $max = (int)readline("nb max : ");
    # $min = (int)readline("nb min : ");

    for ($i=1; $i<=$max; $i++) {
        echo $i."\n";
    }*/

    


    // ====================  pair ou impair ==================== //
    /*
    $nb = (int)readline("Saisissez un nombre entier : ");

    if ($nb%2 == 0){
        echo $nb." est nombre paire.";
    }
    else{
        echo $nb." est nombre impaire.";
    }*/



    // ====================  multiple ==================== //
    
/*     $nb_1 = (int)readline("Saisissez un nombre à multiplier : ");
    $nb_2 = (int)readline("saisissez un nombre max : ");

    for ($i = 1; $i<=$nb_2; $i++){
        echo "$nb_1 * $i = ".($nb_1 * $i)."\n";
    }
 */

    
    // ====================  devinette ==================== //
    
 /*    $nbAleatoire = rand(1,100);
    $compteur = 1;
   
    for ($i=1; $i<=7;$i++){
        $nb = (int)readline("Entrer un nombre entre 1 à 100 : ");

        if ($nb > 100){
            echo "Veuillez saisir un nombre en entre 1 et 100"."\n";
        }
        else{
            if ($nb == $nbAleatoire){
                echo "TROUVER"."\n"."Gagné en ".$compteur." essais"."\n";
                break;
            }
            elseif ($nb > $nbAleatoire){
                echo "Trop grand"."\n";
                $compteur = $i;
            }
            elseif ($nb < $nbAleatoire){
                echo "Trop petit"."\n";
                $compteur = $i;
            }
        }
        if ($compteur == 7 && $nb != $nbAleatoire) {
            echo "Le nombre d’essais a été dépassé\nPERDU\n";
    }
} */

/* $nbAleatoire = rand(0,100);
$compteur = 1;

for ($i=1; $i<=7; $i++){
    $nb = (int)readline("Saisissez un nombre entre 1 et 100 : ");

    if ($nb > 100){
        echo "Saisissez un nombre entre 1 et 100"."\n";
    }
        else{
            if ($nb == $nbAleatoire){
                echo "Trouver"."\n"."Vous avez gagné en ".$compteur." essaie"."\n";
                break;
            }
            elseif ($nb > $nbAleatoire){
                echo "Trop grand"."\n";
                $compteur = $i;
            }
            elseif ($nb < $nbAleatoire){
                echo "Trop petit"."\n";
                $compteur = $i;
            }
        }
        if ($compteur == 7 && $nb != $nbAleatoire){
            echo "Le nombre d'essaie a été dépassé\nPerdu vous êtes trop faible réessayer si vous y tenez\n";
        }
    }
   
 */

# ========================= Trouver les bonnes fonctions ========================= #
    // ====================  Exercice 1  ==================== //
    /*
    $phrase = (string)readline("Saisir une phrase : ");

    if (strlen($phrase) <= 20){
        echo "phrase courte"."\n";
    }
    elseif (strlen($phrase) <= 50){
        echo "phrase de longueur moyenne"."\n";
    }
    else{
        echo "phrase longue"."\n";
    }*/

    // ====================  Exercice 2  ==================== //
    /*
    $mot = (string)readline("Saisir une phrase : ");

    echo "la première lettre de ce mot est : ".$mot[0]."\n";
    echo "la dernière lettre de ce mot est : ".$mot[-1]."\n";
    echo "le nombre de lettres de ce mot est : ".strlen($mot)."\n";
    */# ========================= Trouver les bonnes fonctions ========================= #


    // ====================  Exercice 3  ==================== //
    /*
    $nom = (string)readline("Nom: ");
    $prenom = (string)readline("Prenom: ");

    echo strtoupper($nom)." (". strlen($nom).") ". ucfirst(strtolower($prenom))." (". strlen($prenom).") \n"
    */


    // ====================  Exercice 4  ==================== //
    /*
    $phrase = (string)readline("Entrer une phrase : ");

    if (strlen($phrase) > 10){
        echo substr($phrase, 0, 10)." ..."."\n";
    }
    else{
        echo $phrase;
    }*/



    // ====================  Exercice 5  ==================== //
    /*
    $mot = (string)readline("Saisissez un mot : ");

    if ($mot == strrev($mot)) {
        echo "Le mot '".$mot."' est un palindrome"."\n";
    }
    else{
        echo "Le mot '".$mot."' n'est pas un palindrome"."\n";
    }*/




# ========================= Les collections ========================= #
    // ====================  déclaration de tableaux  ==================== //
    /*
    $tab = [];
    $tabPaire = [];
    $tabImpaire = [];

    for ($i = 0 ; $i < 10 ; $i++ ) {
        $tab[] = rand(1,100);
    }
    
    echo "Voici les valeur de la table ".json_encode($tab)."\n";
    echo "La somme de la table est ".json_encode(array_sum($tab))."\n";
    echo "Le nombre minimum est ".json_encode(min($tab))."\n";
    echo "Le nombre maximum est ".json_encode(max($tab))."\n";


    foreach ($tab as $i) {
        if ($i % 2 == 0) {
            $tabPaire[] = $i;
        } else {
            $tabImpaire[] = $i;
        }
    }

    echo "Voici les valeur de la table Paire ".json_encode($tabPaire)."\n";
    echo "Voici les valeur de la table Impaire ".json_encode($tabImpaire)."\n";
    */



    // ====================  tableau associatif  ==================== //







?> 