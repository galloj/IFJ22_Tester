<?php
declare(strict_types=1);
function f(int $x) : int {
    if($x === 0) {
        return 0;
    } else {
        if($x === 1) {
            return 1;
        } else {
            $param1 = $x - 1;
            $param2 = $x - 2;
            $res1 = f($param1);
            $res2 = f($param2);
            return $res1 + $res2;
        }
    }
}
$res = f(9);
write($res, "\n");