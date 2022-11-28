<?php
declare(strict_types=1);

// source: https://rosettacode.org/wiki/Sierpinski_triangle#Python

function append(string $in, string $s) : string {
    return $in . $s . ";";
}

function get(string $in, int $id) : ?string {
    $i = 0;
    $pos = 0;
    while ($i < $id) {
        $p1 = $pos + 1;
        $ch = substring($in, $pos, $p1);
        while($ch !== ";") {
            $pos = $pos + 1;
            $p1 = $pos + 1;
            $ch = substring($in, $pos, $p1);
        }
        $pos = $pos + 1;
        $i = $i + 1;
    }
    $pos_end = $pos;
    $p1 = $pos_end + 1;
    $ch = substring($in, $pos_end, $p1);
    while($ch !== ";") {
        $pos_end = $pos_end + 1;
        $p1 = $pos_end + 1;
        $ch = substring($in, $pos_end, $p1);
    }
    $ret = substring($in, $pos, $pos_end);
    return $ret;
}

function set(string $in, int $id, string $s) : string {
    $i = 0;
    $pos = 0;
    while ($i < $id) {
        $p1 = $pos + 1;
        $ch = substring($in, $pos, $p1);
        while($ch !== ";") {
            $pos = $pos + 1;
            $p1 = $pos + 1;
            $ch = substring($in, $pos, $p1);
        }
        $pos = $pos + 1;
        $i = $i + 1;
    }
    $pos_end = $pos;
    $p1 = $pos_end + 1;
    $ch = substring($in, $pos_end, $p1);
    while($ch !== ";") {
        $pos_end = $pos_end + 1;
        $p1 = $pos_end + 1;
        $ch = substring($in, $pos_end, $p1);
    }
    $before = substring($in, 0, $pos);
    $slen = strlen($in);
    $after = substring($in, $pos_end, $slen);
    return $before . $s . $after;
}

function length(string $in) : int {
    $i = 0;
    $pos = 0;
    $p1 = $pos + 1;
    $ch = substring($in, $pos, $p1);
    while($ch !== null) {
        $pos = $pos + 1;
        $p1 = $pos + 1;
        $ch = substring($in, $pos, $p1);
        if ($ch === ";") {
            $i = $i + 1;
        } else {}
    }
    return $i;
}

function pow(int $x, int $y) : int {
    $i = 0;
    $ret = 1;
    while($i < $y) {
        $ret = $ret * $x;
        $i = $i + 1;
    }
    return $ret;
}

function sierpinski(int $n) : string {
    $d = "";
    $d = append($d, "*");
    $i = 0;
    while($i < $n) {
        $j = 0;
        $sp = "";
        $p = pow(2, $i);
        while($j < $p) {
            $sp = $sp . " ";
            $j = $j + 1;
        }
        $j = 0;
        $len = length($d);
        $d2 = "";
        while($j < $len) {
            $s = get($d, $j);
            $t2 = $sp . $s . $sp;
            $d2 = append($d2, $t2);
            $j = $j + 1;
        }
        $j=0;
        $d3 = "";
        while($j < $len) {
            $s = get($d, $j);
            $t3 = $s . " " . $s;
            $d3 = append($d3, $t3);
            $j = $j + 1;
        }
        $d = $d2 . $d3;
        $i = $i + 1;
    }
    return $d;
}

$tri = sierpinski(4);
$i = 0;
$len = length($tri);
while($i < $len) {
    $res = get($tri, $i);
    write($res);
    write("\n");
    $i = $i + 1;
    $len = length($tri);
}