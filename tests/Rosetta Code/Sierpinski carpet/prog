<?php
declare(strict_types=1);

// source: https://rosettacode.org/wiki/Sierpinski_carpet#Python

function in_carpet(int $x, int $y) : int {
    while(1===1) {
        if($x === 0) {
            return 1;
        } else {}
        if($y === 0) {
            return 1;
        } else {}
        $x3 = $x / 3;
        $ival = intval($x3);
        if($x - $ival*3 === 1) {
            $y3 = $y / 3;
            $ival = intval($y3);
            if($y - $ival * 3 === 1) {
                return 0;
            } else {}
        } else {}
        
        $x = $x / 3;
        $x = intval($x);
        $y = $y / 3;
        $y = intval($y);
    }
}

function carpet(int $n) : void {
    $i = 0;
    while($i < $n) {
        $j = 0;
        while($j < $n) {
            $inc = in_carpet($i, $j);
            if($inc) {
                write("*");
            } else {
                write(" ");
            }
            $j = $j + 1;
        }
        write("\n");
        $i = $i + 1;
    }
}

carpet(27);