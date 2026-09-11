<?php
    // ====================  Exercice 1  ==================== //
/*     $typePhrase = (string)readline("Saisissez une phrase : ");

    if (strlen($typePhrase) <= 20){
        echo "Phrase courte"."\n";
    }
    elseif (strlen($typePhrase) < 50) {
        echo "Phrase moyenne"."\n";
    }
    elseif ((strlen($typePhrase)) >= 50){
        echo "Phrase longue"."\n";
    }

    // ====================  Exercice 2  ==================== //
    $mot = (string)readline("Saisissez un mot : ");
    echo "la première lettre de ce mot est : ".$mot[0]."\n";
    echo "la dernière lettre de ce mot est : ".$mot[-1]."\n";
    echo "le nombre de lettres de ce mot est : ".strlen($mot)."\n";

        // ====================  Exercice 3  ==================== //

    $nom = (string)readline("Nom: ");
    $prenom = (string)readline("Prenom: ");

    echo strtoupper($nom)." (". strlen($nom).") ". ucfirst(strtolower($prenom))." (". strlen($prenom).") \n";

    // ====================  Exercice 4  ==================== //
    
    $phrase = (string)readline("Entrer une phrase : ");

    if (strlen($phrase) > 10){
        echo substr($phrase, 0, 10)." ..."."\n";
    }
    else{
        echo $phrase;
    }

       // ====================  Exercice 5  ==================== //
    
$mot = readline("Entrez un mot : ");

// Mettre le mot en minuscule pour éviter les erreurs de casse
$mot = strtolower($mot);

// Inverser le mot
$motInverse = strrev($mot);

// Vérification
if ($mot === $motInverse) {
    echo "Le mot \"$mot\" est un palindrome." . "\n";
} else {
    echo "Le mot \"$mot\" n'est pas un palindrome." . "\n";
}
 */
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

1 - Installer et tester la plateforme LAMP
foreach ($tab as $i) {
        if ($i % 2 == 0) {
            $tabPaire[] = $i;
        } else {
            $tabImpaire[] = $i;
        }
    }

echo "Voici les valeur de la table Paire ".json_encode($tabPaire)."\n";
echo "Voici les valeur de la table Impaire ".json_encode($tabImpaire)."\n";

// ====================  tableau associatif  ==================== //
$eleves = array(
    "Mzé"  => 12,
    "Harin"  => 8,
    "Sany" => 18,
    "Natan"   => 4,
    "Ulrick"   => 15,
    "Raken"   => 10,
    "Thomas"    => 14,
    "Mustafa"    => 9,
    "Edwin"    => 17,
    "Noah"    => 11
);

foreach($eleves as $nomNote => $note){
echo $nomNote . " : " . $note . "\n";
}

$somme = array_sum($eleves);      // somme des notes
$nombreEleves = count($eleves);  // nombre d'élèves
$moyenne = $somme / $nombreEleves;

echo "La moyenne de la classe est : " . round($moyenne, 2)."\n"."\n";

$eleves = array(
    "Adrien"  => array(12, 10, 8),
    "Jemuel"  => array(8, 9, 11),
    "Tristan" => array(18, 17, 19),
    "Natan"   => array(4, 6, 5),
    "Sarah"   => array(15, 14, 16)
);

foreach ($eleves as $nom => $notes) {

    // Afficher le nom
    echo "Élève : $nom\n";

    // Afficher les notes
    echo "Notes : ";
    foreach ($notes as $note) {
        echo $note . " ";
    }

    // Calcul de la moyenne
    $moyenne = array_sum($notes) / count($notes);

    echo "\nMoyenne : " . round($moyenne, 2) . "\n\n";
}

// ====================  Pays - Chômage  ==================== //
$pays = array(
    "France"   => 7,
    "USA"      => 4,
    "Belgique" => 8,
    "Espagne"  => 12,
    "Allemagne"=> 5,
    "Italie"   => 9,
    "Portugal" => 6,
    "Canada"   => 5,
    "Maroc"    => 10,
    "Japon"    => 3
);

foreach ($pays as $nomPays => $taux) {
    if ($taux > 6) {
        echo $nomPays . " : " . $taux . "%\n";
    }
}
*/
# ========================= Les fonctions ========================= #

//                         fonction serie
function serie($n) {
    $tableau = array();

    for ($i = 1; $i <= $n; $i++) {
        $tableau[] = $i;
    }

    return $tableau;
}

$resultat = serie(5);
print_r($resultat);

# fonction serieInverse

function serieInverse($n) {
    $tableau = array();

    for ($i = 1; $i <= $n; $i++) {
        $tableau[] = ($n+1) - $i;
    }

    return $tableau;
}

$resultat = serieInverse(5);
print_r($resultat);

# fonction somme()

function somme(int $n): int {
    $somme = 0;
    for ($i = 1; $i <= $n; $i++) {
        $somme += $i;
    }

    return $somme;
}


echo "\n".somme(5). "\n". "\n";

# fonction sommeCube
function sommeCube(int $n): int {
    $sommeC = 0;
    for ($i = 1; $i <= $n; $i++) {
        $sommeC += $i**3;
    }

    return $sommeC;
}

echo sommeCube(5). "\n". "\n";

# fonction produit
function produit(int $n): int {
    $prdt = 1;
    for ($i = 1; $i <= $n; $i++) {
        $prdt *= $i;
    }

    return $prdt;
}

echo produit(5). "\n". "\n";

#  pair

function tabPair(int $n): array {
    $tab = [];
    $pairs = [];

    for ($i=1; $i<=$n; $i++){
        $tab[] = $i;
    }
    foreach ($tab as $valeur) {
        if ($valeur % 2 == 0) {
            $pairs[] = $valeur;
        }
    }

    return $pairs;
}

print_r(tabPair(10));

# impair
function tabImpair(int $n): array {
    $tab = [];
    $impair = [];

    for ($i=1; $i<=$n; $i++){
        $tab[] = $i;
    }
    foreach ($tab as $valeur) {
        if ($valeur % 2 == 1) {
            $impair[] = $valeur;
        }
    }

    return $impair;
}

// Exemple d'utilisation

print_r(tabImpair(10));

# parité

function tabParite($n) {
    $resultat = [
        'pair' => [],
        'impair' => []
    ];

    foreach ($n as $valeur) {
        if ($valeur % 2 == 0) {
            $resultat['pair'][] = $valeur;
        } else {
            $resultat['impair'][] = $valeur;
        }
    }

    return $resultat;
}

$tab = [1, 2, 3, 4, 5, 6, 7, 8];

$resultat = tabParite($tab);
print_r($resultat);

# 3.5.9. droitPrime
function droitPrime($nb_enfants, $ressources) {
    if ($nb_enfants == 1) {
        return $ressources <= 33044;
    } elseif ($nb_enfants == 2) {
        return $ressources <= 38045;
    } elseif ($nb_enfants >= 3) {
        return $ressources <= 44046;
    } else {
        return false;
    }
}

var_dump(droitPrime(1, 28046));
var_dump(droitPrime(2, 50046));
var_dump(droitPrime(3, 45046));

?>