<?php //Program 3: Prace s retezci a vestavenymi funkcemi 
declare(strict_types=1);

write("Ahoj\n\"Sve'te \\\042", "\n");  // 042 oktalove = 34 decimalne = znak uvozovek

$s1 = "Toto je nejaky text";
$s2 = $s1 . ", ktery jeste trochu obohatime";
write($s1, "\012", $s2, "\x0A");

$s1len = strlen($s1);
$s1_20ty_znak = $s1len;
$s1len = 4;
$s1_16ty_znak = $s1_20ty_znak - $s1len; 
$s1 = substring($s2, $s1_16ty_znak, $s1_20ty_znak); 
write($s1len, " znaky od ", 16, ". znaku (index ", $s1_16ty_znak, ") v \"", $s2, "\":", $s1, "\n");

$s1 = substring($s2, 15, 19); // vysledny retezec v s1 bude mit 4 znaky
$s1len4 = strlen($s1);
write($s1len4, " znaky od ", 16, ". znaku v \"", $s2, "\":", $s1, "\n");  
?>