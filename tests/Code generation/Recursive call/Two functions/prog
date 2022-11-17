<?php
declare(strict_types=1);
function f(int $x) : int {
    if($x === 0) {
        return 0;
    } else {
        $inp = $x - 1;
        $res = g($inp);
        return $res + $x;
    }
}
function g(int $x) : int {
    $res = f($x);
    return $res + 1;
}
$res = g(10);
write($res, "\n");