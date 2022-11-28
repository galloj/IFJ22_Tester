<?php
declare(strict_types=1);

// source: https://rosettacode.org/wiki/Mandelbrot_set#Fixed_point_16_bit_arithmetic

/**
  ascii Mandelbrot using 16 bits of fixed point integer maths with a selectable fractional precision in bits.

  This is still only 16 bits mathc and allocating more than 6 bits of fractional precision leads to an overflow that adds noise to the plot..

  This code frequently casts to short to ensure we're not accidentally benefitting from GCC promotion from short 16 bits to int.

  gcc fixedPoint.c  -lm

 */

// convenient casting
function si(int $i) : int {
    $ret = intval($i);
    $param = $ret / 65536;
    $intval = intval($param);
    $ret = $ret - $intval * 65536;
    return $ret;
  }

  function sf(float $i) : int {
    $ret = intval($i);
    $param = $ret / 65536;
    $intval = intval($param);
    $ret = $ret - $intval * 65536;
    return $ret;
  }

function pow(int $x, int $y) : int {
    $ret = 1;
    $i = 0;
    while($i < $y) {
        $ret = $ret * $x;
        $i = $i + 1;
    }
    return $ret;
}

function toPrec(float $f, int $bitsPrecision) : int {
    $p = pow(2,$bitsPrecision);
    $i = intval($f);
    $whole = $i * $p;
    $r = ($f-$i)* $p;
    $part = intval($r);
    $ret = $whole + $part;
    return $ret;
}

function shiftRight(int $n, int $bits) : int {
    $i = 0;
    $ret = $n;
    while($i < $bits) {
        $ret = $ret / 2;
        $i = $i + 1;
    }
    $ret = intval($ret);
    return $ret;
}

// chosen to match https://www.youtube.com/watch?v=DC5wi6iv9io
$width = 32; // basic width of a zx81
$height = 22; // basic width of a zx81
$zoom=1;  // bigger with finer detail ie a smaller step size - leave at 1 for 32x22

// params
$bitsPrecision = 6;
write("PRECISION=", $bitsPrecision, "\n");

$p = toPrec(3.5,$bitsPrecision);
$val = $p / $zoom;
$X1 = intval($val);
$X2 = toPrec(2.25,$bitsPrecision) ;
$p = toPrec(3.0,$bitsPrecision);
$val = $p/$zoom;
$Y1 = intval($val) ;   // horiz pos
$Y2 = toPrec(1.5,$bitsPrecision) ; // vert pos
$LIMIT = toPrec(4.0,$bitsPrecision);


// fractal
//char * chr = ".:-=X$#@.";
$chr = "abcdefghijklmnopqr ";
//char * chr = ".,'~=+:;[/<&?oxOX#.";
$maxIters = strlen($chr);

$py=0;
$runy = 1;
while ($py < $height*$zoom) {
$px=0;
while ($px < $width*$zoom) {
    $six_arg = $px*$X1;
    $siy_arg = $py*$Y1;
    $six = si($six_arg);
    $siy = si($siy_arg);
    $sfx_arg = $six / $width;
    $sfy_arg = $siy / $height;
    $sfx = sf($sfx_arg);
    $sfy = sf($sfy_arg);
    $x0 = $sfx - $X2;
    $y0 = $sfy - $Y2;

    $x=0;
    $y=0;

    $i=0;

    $xSqr = 0;
    $ySqr = 0;
    $maxItersT = $maxIters;
    while ($i < $maxItersT) {
        $six_arg = $x * $x;
        $siy_arg = $y * $y;
        $six = si($six_arg);
        $siy = si($siy_arg);
        $xSqr = shiftRight($six, $bitsPrecision);
        $ySqr = shiftRight($siy, $bitsPrecision);

        // Breakout if sum is > the limit OR breakout also if sum is negative which indicates overflow of the addition has occurred
        // The overflow check is only needed for precisions of over 6 bits because for 7 and above the sums come out overflowed and negative therefore we always run to maxIters and we see nothing.
        // By including the overflow break out we can see the fractal again though with noise.
        if (($xSqr + $ySqr) >= $LIMIT) {
            $maxItersT = 0;
        } else {}
        if(($xSqr+$ySqr) < 0) {
            $maxItersT = 0;
        } else {}

        if($maxItersT !== 0) {
            $xt = $xSqr - $ySqr + $x0;
            $xy = $x * $y;
            $si = si($xy);
            $sr = shiftRight($si, $bitsPrecision);
            $si = si($sr);
            $si = $si * 2;
            $si = si($si);
            $si = $si + $y0;
            $y = si($si);
            $x=$xt;

            $i = $i + 1;
        } else {}
    }
    $i = $i - 1;
    $i2 = $i+1;
    $substr = substring($chr, $i, $i2);
    write($substr);

    $px = $px + 1;
}

write("\n");
$py = $py + 1;
}