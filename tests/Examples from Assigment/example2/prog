<?php
declare(strict_types=1);
// Program 2: Vypocet faktorialu (rekurzivne)

// Hlavni telo programu
write("Zadejte cislo pro vypocet faktorialu: ");
$a = readi();

// Definice funkce pro vypocet hodnoty faktorialu
function factorial(int $n) : int {
	if ($n < 2) {
		$result = 1;
	} else {
		$decremented_n = $n - 1;
		$temp_result = factorial($decremented_n);
		$result = $n * $temp_result;
	}
	return $result;
}

if ($a !== null) {
	if ($a < 0)	{ // Pokracovani hlavniho tela programu
		write("Faktorial nelze spocitat\n");
	} else {
		$vysl = factorial($a);
		write("Vysledek je: ", $vysl, "\n");
	}
} else {
	write("Chyba pri nacitani celeho cisla!\n");
}