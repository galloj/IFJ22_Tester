<?php
declare(strict_types=1);
// Program 1: Vypocet faktorialu (iterativne)

// Hlavni telo programu
write("Zadejte cislo pro vypocet faktorialu\n");
$a = readi();

if ($a === null) {
	write("Chyba pri nacitani celeho cisla!\n");
} else {}

if ($a < 0) {
	write("Faktorial nelze spocitat\n");
} else {
	$vysl = 1;
	while ($a > 0) {
		$vysl = $vysl * $a;
		$a = $a - 1;
	}
	write("Vysledek je: ", $vysl, "\n");
}
