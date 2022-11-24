<?php
declare(strict_types=1);
$data = "";
$ptr = 0;
$program = reads();
$program_length = strlen($program);
$pc = 0;

function setData(string $data, int $ptr, int $value) : string {
    $dataLen = strlen($data);
    $data1 = ssubstr($data, 0, $ptr);
    $ptrCont = $ptr + 1;
    $data2 = ssubstr($data, $ptrCont, $dataLen);
    $chr = chr($value);
    $out = $data1 . $chr . $data2;
    return $out;
}

function ssubstr(string $str, int $start, int $end) : string {
    $out = substring($str, $start, $end);
    if($out !== null) {
        return $out;
    } else {
        return "";
    }
}

while($pc<$program_length) {
    $pcPlusOne = $pc + 1;
    $c = ssubstr($program, $pc, $pcPlusOne);
    if($c) {} else {$c=chr(0);}
    if($c==="+") {
        $ptrPlusOne = $ptr + 1;
        $oldByte = ssubstr($data, $ptr, $ptrPlusOne);
        $newByte = ord($oldByte);
        $newByte = $newByte + 1;
        if($newByte>255) {$newByte=0;} else {}
        if($newByte<0) {$newByte=255;} else {}
        $data = setData($data, $ptr, $newByte);
    } else {
        if($c==="-") {
            $ptrPlusOne = $ptr + 1;
            $oldByte = ssubstr($data, $ptr, $ptrPlusOne);
            $newByte = ord($oldByte);
            $newByte = $newByte - 1;
            if($newByte>255) {$newByte=0;} else {}
            if($newByte<0) {$newByte=255;} else {}
            $data = setData($data, $ptr, $newByte);
        } else {
            if($c===">") {
                $ptr = $ptr + 1;
            } else {
                if($c==="<") {
                    $ptr = $ptr - 1;
                } else {
                    if($c===".") {
                        $ptrPlusOne = $ptr + 1;
                        $out = ssubstr($data, $ptr, $ptrPlusOne);
                        write($out);
                    } else {
                        if($c==="[") {
                            $ptrPlusOne = $ptr + 1;
                            $oldByte = ssubstr($data, $ptr, $ptrPlusOne);
                            $newByte = ord($oldByte);
                            if($newByte===0) {
                                $pc = $pc + 1;
                                $nesting = 1;
                                while($nesting>0) {
                                    $pcPlusOne = $pc + 1;
                                    $c = ssubstr($program, $pc, $pcPlusOne);
                                    if($c) {} else {$c=chr(0);}
                                    if($c==="[") {
                                        $nesting = $nesting + 1;
                                    } else {
                                        if($c==="]") {
                                            $nesting = $nesting - 1;
                                        } else {}
                                    }
                                    $pc = $pc + 1;
                                }
                            } else {}
                        } else {
                            if($c==="]") {
                                $ptrPlusOne = $ptr + 1;
                                $oldByte = ssubstr($data, $ptr, $ptrPlusOne);
                                $newByte = ord($oldByte);
                                if($newByte===0) {
                                } else {
                                    $pc = $pc - 1;
                                    $nesting = 1;
                                    while($nesting>0) {
                                        $pcPlusOne = $pc + 1;
                                        $c = ssubstr($program, $pc, $pcPlusOne);
                                        if($c) {} else {$c=chr(0);}
                                        if($c==="[") {
                                            $nesting = $nesting - 1;
                                        } else {
                                            if($c==="]") {
                                                $nesting = $nesting + 1;
                                            } else {}
                                        }
                                        $pc = $pc - 1;
                                    }
                                }
                            } else {}
                        }
                    }
                }
            }
        }
    }
    $pc = $pc + 1;
}