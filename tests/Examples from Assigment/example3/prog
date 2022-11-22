<?php
declare(strict_types=1);
/* Program 3: Prace s retezci a vestavenymi funkcemi */

$str1 = "Toto je nejaky text v programu jazyka IFJ22";
$str2 = $str1 . ", ktery jeste trochu obohatime";
write($str1, "\n", $str2, "\n");
write("Pozice retezce \"text\" v \$str2: ", 15, "\n");
write("Zadejte serazenou posloupnost vsech malych pismen a-h, ");
$str1 = reads();
if ($str1 !== null) {
	while ($str1 !== "abcdefgh") {
		write("Spatne zadana posloupnost, zkuste znovu:\n");
		$str1 = reads();
	}
} else { }
?>