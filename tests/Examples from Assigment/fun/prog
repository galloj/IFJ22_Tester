<?php
declare(strict_types=1);

function f  // jmeno funkce
(int$x)     // seznam parametru
:
int  /* deklarace funkce */ {
  if($x<10){return $x-1;}else{$x = $x - 1;
    write("calling g with ", $x, "\n");
    $res = g($x);
    return $res;
  }
}

function g(int $x):int{
  if ($x > 0) {
    write("calling f with ", $x, "\n");
    $x = f($x);// modifikace parametru x, ale az po zavolani funkce f
    return $x;
  } else {
  
  return 200;
  
  }
}

$res = g(10);
write("res: ", $res, "\n");

// konec zdrojaku IFJ22
?>