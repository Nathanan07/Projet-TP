# 3.2.1. 1 : Compteur

<?php
$x = 1 ;
while ($x <= 20) {
echo("x a pour valeur $x \n");
$x = $x + 1 ;
}

$x = 1 ;
$y = (int) readline("Entrez un nombre : ");
while ($x <= $y) {
echo("x a pour valeur $x \n");
$x = $x + 1 ;
}
?>

# 3.2.2. 2 : pair ou impair
<?php
$pi= (int) readline("Saisir un nombre : ");
if ($pi % 2 == 0) {
    echo"Nombre pair $pi \n";
}
else {
    echo"Nombre impair $pi \n";
}

echo $pi;

$compteur = $pi;
for ($i = 0; $i < 10; $i++) {
    $compteur += 2;
    echo " - " . $compteur;
}
?>

# 3.2.3. 3 : multiple

<?php
for ($i = 5; $i <= 50; $i += 5) {
    echo $i . " ";
}

$deb = (int) readline("Saisissez un nombre : ");
$fin = (int) readline("Saisissez un nombre : ");




// Saisie des valeurs
echo "Saisir un nombre : ";
$nombre = intval(trim(fgets(STDIN)));

echo "Saisir le nombre maximum : ";
$max = intval(trim(fgets(STDIN)));

// Affichage des multiples
for ($i = $nombre; $i <= $max; $i += $nombre) {
    echo $i . " ";
}
?>