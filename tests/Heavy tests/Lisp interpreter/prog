<?php
declare(strict_types=1);

// example code in this test taken from https://stackoverflow.com/questions/5206266/factorial-function-with-just-lambda-expression
/*
 a value is represented as a single char representing the type
 i = int
 c = cons
 s = string
 f = float (not implemented, fuck parsing that)
 then, for strings and ints, the data;
 for cons, we have the char length of car, c, car, cdr
 */

// a perfectly sane cons cell
function seeksep(string $q, int $s): int {
    $SEP = "c";
    $i = $s;
    $i1 = $i + 1;
    $ss = substring($q, $i, $i1);
    while($ss !== $SEP) {
        $i = $i1;
        $i1 = $i + 1;
        $ss = substring($q, $i, $i1);
    }
    return $i1;
}

function car(string $s): string {
    $f = substring($s, 0, 1);
    if ($f !== "c") {
        write("FATAL:car called on non-cons:", $s, "\n");
        $_ = 1 / 0;
    } else {}
    $i = seeksep($s, 1);
    $i1 = $i - 1;
    $carl = substring($s, 1, $i1);
    $carl = s2i($carl);
    $care = $i + $carl;
    $car = substring($s, $i, $care);
    return $car;
}

function cdr(string $s): string { 
    $f = substring($s, 0, 1);
    if ($f !== "c") {
        write("FATAL:cdr called on non-cons:", $s, "\n");
        $_ = 1 / 0;
    } else {}
    $i = seeksep($s, 1);
    $i1 = $i - 1;
    $carl = substring($s, 1, $i1);
    $carl = s2i($carl);
    $care = $i + $carl;
    $cdre = strlen($s);
    $cdr = substring($s, $care, $cdre);
    return $cdr;
}

function cons(string $car, string $cdr): string {
    $l = strlen($car);
    $l = i2s($l);
    return "c".$l . "c" . $car . $cdr;
}

function i2s(int $i): string {
    if($i === 0) {
        return "0";
    } else {}
    $ret = "";
    if($i < 0) {
        $ret = "-";
        $i = 0 - $i;
    } else {}
    $id = $i / 10;
    $ir = intval($id);
    if ($ir === 0) {
        $before = "";
    } else {
        $before = i2s($ir);
    }
    $digit = $i - $ir * 10;
    $d1 = $digit + 1;
    $Ds = "0123456789";
    $d = substring($Ds, $digit, $d1);
    return $ret . $before . $d;
}

function d2i(string $d):int {
    if($d === "0") {return 0;} else {}
    if($d === "1") {return 1;} else {}
    if($d === "2") {return 2;} else {}
    if($d === "3") {return 3;} else {}
    if($d === "4") {return 4;} else {}
    if($d === "5") {return 5;} else {}
    if($d === "6") {return 6;} else {}
    if($d === "7") {return 7;} else {}
    if($d === "8") {return 8;} else {}
    if($d === "9") {return 9;} else {}
    $ret = 0 - 1;
    return $ret;
}

function s2i(string $s):int {
    $f = substring($s, 0, 1);
    if($f === "-") {
        $i = 1;
        $mul = 0 - 1;
    } else {
        $i = 0;
        $mul = 1;
    }
    $ret = 0;
    $l = strlen($s);
    while($i < $l) {
        $i1 = $i + 1;
        $d = substring($s, $i, $i1);
        $d = d2i($d);
        $ret = $ret * 10 + $d;
        $i = $i1;
    }
    return $ret * $mul;
}

function drop_first(string $s): string {
    $l = strlen($s);
    $r = substring($s, 1, $l);
    $r = strval($r);
    return $r;
}

function wrapi(int $i): string {
    $SEP = chr(0);
    $s = i2s($i);
    return "i".$s;
}


function unwrapi(string $s): int {
    $f = substring($s, 0, 1);
    if ($f !== "i") {
        write("FATAL:unwrapi called on non-int:", $s, "\n");
        $_ = 1 / 0;
    } else {}
    $s = drop_first($s);
    $s = s2i($s);
    return $s;
}

function wraps(string $s): string {
    $SEP = chr(0);
    return "s".$s;
}

function unwraps(string $s): string {
    $f = substring($s, 0, 1);
    if ($f !== "s") {
        write("FATAL:unwraps called on non-string:", $s, "\n");
        $_ = 1 / 0;
    } else {}
    $s = drop_first($s);
    return $s;
}

function putsexpr(string $s): void {
    $f = substring($s, 0, 1);
    if($f === "c") {
        write("(");
        $car = car($s);
        putsexpr($car);
        write(" . ");
        $cdr = cdr($s);
        putsexpr($cdr);
        write(")");
    } else {}
    if ($f === "s") {
        $us = unwraps($s);
        write("s:", $us);
    } else {}
    if ($f === "i") {
        $ui = unwrapi($s);
        write("i:", $ui);
    } else {}
}

function dbg(?string $v): void {
    if ($v === null) {
        write("(null)\n");
    } else {
        write($v, "!\n");
    }
}

function revlist(string $c): string {
    $ret = "s";
    while($c !== "s") {
        $car = car($c);
        $cdr = cdr($c);
        $ret = cons($car, $ret);
        $c = $cdr;
    }
    return $ret;
}

function process_term(string $t): string {
    $l  = strlen($t);
    $snd = substring($t, 1, 2);
    if($snd === "-") {
        $i = 2;
        if($l === 2) {
            return $t; // - should remain a string
        } else {}
    } else {
        $i = 1;
    }
    while($i < $l) {
        $i1 = $i + 1;
        $c = substring($t, $i, $i1);
        $d = d2i($c);
        if($d < 0) {
            return $t;
        } else {}
        $i = $i1;
    }
    $rt = unwraps($t);
    $ret = "i" . $rt;
    return $ret;
}
// string starting with (
function readcons(string $s): ?string {
    $s = drop_first($s);
    $lastrem = " ";
    $rcons = "s";
    while($lastrem !== ")") {
        $trem = readsexpr($s);
        if ($trem === null) {
            return null;
        } else {}
        $rem = cdr($trem);
        $t = car($trem);
        $rcons = cons($t, $rcons);
        $s = unwraps($rem);
        $i = 0;
        $x = 0;
        $lastrem = substring($s, 0, 1);
        $l = strlen($s);
        while($i + $x < $l) {
            $i1 = $i + 1;
            $lastrem = substring($s, $i, $i1);
            if($lastrem === " ") {
                $i = $i1;
            } else {
                if($lastrem === "\n") {
                    $i = $i1;
                } else {
                    $x = $l;
                }
            }
        }
        $s = substring($s, $i, $l);
    }
    $s = drop_first($s);
    $s = wraps($s);
    $rcons = revlist($rcons);
    $ret = cons($rcons, $s);
    return $ret;
}

// return a cons of the read term and the rest of the input, or null if there was no term
function readsexpr(string $s): ?string {
    $l = strlen($s);
    $x = 0;
    $start = 0;
    while($start + $x < $l) {
        $s1 = $start + 1;
        $sp = substring($s, $start, $s1);
        if ($sp === " ") {
            $start = $s1;
        } else {
            if ($sp === "\n") {
                $start = $s1;
            } else {
                $x = $l;
            }
        }
    } // skip leading spaces
    if ($x === 0) {
        return null; // trailing whitespace
    } else {}
    if ($sp === "(") {
        $s = substring($s, $start, $l);
        $s2 = $s1 + 1;
        $sp1 = substring($s, $s1, $s2);
        if($sp1 === ")") {
            $s = drop_first($s);
            $s = drop_first($s);
            $s = wraps($s);
            $ret = cons("s", $s);
            return $ret;
        } else {}
        $ret = readcons($s);
        return $ret;
    } else {}
    $end = $start;
    while($end < $l) {
        $e1 = $end + 1;
        $ss = substring($s, $end, $e1);
        if ($ss !== " ") {
            if ($ss !== "\n") {
                if ($ss !== ")") {
                    $end = $e1;
                } else {
                    $term = substring($s, $start, $end);
                    $rest = substring($s, $end, $l);
                    $term = wraps($term);
                    $term = process_term($term);
                    $rest = wraps($rest);
                    $ret = cons($term, $rest);
                    return $ret;
                }
            } else {
                $term = substring($s, $start, $end);
                $rest = substring($s, $end, $l);
                $term = wraps($term);
                $term = process_term($term);
                $rest = wraps($rest);
                $ret = cons($term, $rest);
                return $ret;
            }
        } else {
            $term = substring($s, $start, $end);
            $rest = substring($s, $end, $l);
            $term = wraps($term);
            $term = process_term($term);
            $rest = wraps($rest);
            $ret = cons($term, $rest);
            return $ret;
        }
    }
    if ($start === $end) {
        return null;
    } else {
        $term = substring($s, $start, $end);
        $term = wraps($term);
        $term = process_term($term);
        $ret = cons($term, "s");
        return $ret;
    }
}

function checklen(string $l, int $n): void {
    if ($n === 0) {
        if ($l === "s") { }
        else {
            write("ERROR:too many arguments");
            $_ = 1 / 0;
        }
    } else {
        if($l === "s") {
            write("ERROR:too few arguments");
            $_ = 1/0;
        } else {
            $cdr = cdr($l);
            $n1 = $n - 1;
            checklen($cdr, $n1);
        }
    }
}

function listlen(string $l) : int {
    if ($l === "s") {
        return 0;
    } else {
        $cdr = cdr($l);
        $r = listlen($cdr);
        return $r + 1;
    }
}

function typeof(string $x): string {
    $r = substring($x, 0, 1);
    return $r;
}

function lookup_env(string $env, string $key): ?string {
    if ($env === "s") {
        return null;
    } else {
        $car = car($env);
        $cdr = cdr($env);
        $k = car($car);
        if($k === $key) {
            $v = cdr($car);
            return $v;
        } else {
            $rest = lookup_env($cdr, $key);
            return $rest;
        }
    }
}

// returns (new_env.result)
function eval(string $env, string $code): string {
    $ct = typeof($code);
    if($ct === "i") {
        $result = cons($env, $code);
        return $result; // ints evaluate as themselves
    } else {}
    if($ct === "s") {
        $assoc = lookup_env($env, $code);
        if($assoc === null) {
            write("ERROR:undefined variable: ", $code);
            $_ = 1/0;
        } else {
            $ret = cons($env, $assoc);
            return $ret;
        }
    } else {}
    // cons
    $head = car($code);
    $ht = typeof($head);
    if($ht === "c") {
        $result = eval($env, $head);
        $env = car($result);
        $head = cdr($result);
    } else {}
    $ht = typeof($head);
    $userf = null;
    if($ht !== "s") {
        if($ht === "c") {
            $userf = $head;
        } else {
            write("ERROR:call to non-callable:", $head);
            $_ = 1/0;
        }
    } else {}
    $tail = cdr($code);
    if ($userf === null) {
        $userf = lookup_env($env, $head);
    } else {}
    if ($userf !== null) {
        $head = $userf;
        $callenv = car($head);
        $head = cdr($head);
        $argl = car($head);
        $head = cdr($head);
        $body = car($head);
        $tail = cdr($code);
        $argn = listlen($argl);
        checklen($tail, $argn);
        while($argl !== "s") {
            $argname = car($argl);
            $argcode = car($tail);
            $res = eval($env, $argcode);
            $env = car($res);
            $argvalue = cdr($res);
            $entry = cons($argname, $argvalue);
            $callenv = cons($entry, $callenv);
            $argl = cdr($argl);
            $tail = cdr($tail);
        }
        while($body !== "s") {
            $instr = car($body);
            $res = eval($callenv, $instr);
            $callenv = car($res);
            $result = cdr($res);
            $body = cdr($body);
        }
        $ret = cons($env, $result);
        return $ret;
    } else {}
    $head = unwraps($head);
    if ($head === "quote") {
        checklen($tail, 1);
        $v = car($tail);
        $result = cons($env, $v);
        return $result;
    } else {}
    if ($head === "write") {
        while($tail !== "s") {
            $here = car($tail);
            $res = eval($env, $here);
            $env = car($res);
            $ret = cdr($res);
            putsexpr($ret);
            $tail = cdr($tail);
        }
        $r = cons($env, "s");
        return $r;
    } else {}
    if ($head === "car") {
        checklen($tail, 1);
        $car = car($tail);
        $ret = eval($env, $car);
        $env = car($ret);
        $car = cdr($ret);
        $car = car($car);
        $r = cons($env, $car);
        return $r;
    } else {}
    if ($head === "cdr") {
        checklen($tail, 1);
        $car = car($tail);
        $ret = eval($env, $car);
        $env = car($ret);
        $car = cdr($ret);
        $car = cdr($car);
        $r = cons($env, $car);
        return $r;
    } else {}
    if ($head === "cons") {
        checklen($tail, 2);
        $car = car($tail);

        $ret = eval($env, $car);
        $env = car($ret);
        $car = cdr($ret);

        $cdr = cdr($tail);
        $car2 = car($cdr);

        $ret = eval($env, $car);
        $env = car($ret);
        $car2 = cdr($ret);

        $cons = cons($car, $car2);
        $r = cons($env, $cons);
        return $r;
    } else {}
    if ($head === "+") {
        $acc = 0;
        while($tail !== "s") {
            $here = car($tail);
            $res = eval($env, $here);
            $env = car($res);
            $ret = cdr($res);
            $n = unwrapi($ret);
            $acc = $acc + $n;
            $tail = cdr($tail);
        }
        $acc = wrapi($acc);
        $ret = cons($env, $acc);
        return $ret;
    } else {}
    if ($head === "*") {
        $acc = 1;
        while($tail !== "s") {
            $here = car($tail);
            $res = eval($env, $here);
            $env = car($res);
            $ret = cdr($res);
            $n = unwrapi($ret);
            $acc = $acc * $n;
            $tail = cdr($tail);
        }
        $acc = wrapi($acc);
        $ret = cons($env, $acc);
        return $ret;
    } else {}
    if ($head === "-") {
        $acc = null;
        while($tail !== "s") {
            $here = car($tail);
            $res = eval($env, $here);
            $env = car($res);
            $ret = cdr($res);
            $n = unwrapi($ret);
            if ($acc === null) {
                $acc = $n;
            } else {
                $acc = $acc - $n;
            }
            $tail = cdr($tail);
        }
        if ($acc === null) {
            $acc = 0;
        } else {}
        $acc = wrapi($acc);
        $ret = cons($env, $acc);
        return $ret;
    } else {}
    if ($head === "zero?") {
        checklen($tail, 1);
        $here = car($tail);
        $res = eval($env, $here);
        $env = car($res);
        $ret = cdr($res);
        if ($ret === "i0") {
            $ret = "i1";
        } else {
            $ret = "s";
        }
        $ret = cons($env, $ret);
        return $ret;
    } else {}
    if ($head === "def") {
        checklen($tail, 2);
        $car = car($tail);
        $ct = typeof($car);
        if($ct !== "s") {
            write("ERROR: attempt to define non-string:", $ct);
            $_ = 1/0;
        } else {}
        $cdr = cdr($tail);
        $car2 = car($cdr);

        $ret = eval($env, $car2);
        $env = car($ret);
        $car2 = cdr($ret);

        $cons = cons($car, $car2);
        $env = cons($cons, $env);
        $r = cons($env, "s");
        return $r;
    } else {}
    if ($head === "lambda") {
        $args = car($tail);
        $body = cdr($tail);
        $fdef = cons($body, "s");
        $fdef = cons($args, $fdef);
        $fdef = cons($env, $fdef);
        $res = cons($env, $fdef);
        return $res;
    } else {}
    if ($head === "if") {
        $cond = car($tail);
        $tail = cdr($tail);
        $ret = eval($env, $cond);
        $env = car($ret);
        $bool = cdr($ret);
        if($bool !== "s") {
            $bod = car($tail);
            $res = eval($env, $bod);
            return $res;
        } else {
            $tail = cdr($tail);
            if($tail === "s") {
                $res = cons($env, "s");
                return $res;
            } else {
                $bod = car($tail);
                $res = eval($env, $bod);
                return $res;
            }
        }
    } else {}
    write("undefined function:", $head);
    $_ = 1/0;
}

$env = "s";

//write("? ");
$in = reads();

$rr = readsexpr($in);
while($rr !== null) {
    $x = car($rr);
    $in = cdr($rr);
    $in = unwraps($in);
    $r = eval($env, $x);
    $env = car($r);
    $res = cdr($r);
    if ($res !== "s") {
        putsexpr($res);
        write("\n");
    } else {}
    $rr = readsexpr($in);
}