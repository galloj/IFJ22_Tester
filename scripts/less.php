<?php

$vars_sets =
    [
        [-1, 0, 1, -1.0, -0.5, 0.0, 0.5, 1.0],
        ["", "aa", "ab"],
    ];

// strnum
// $vars_sets =
//     [
//         [-1, 0, 1, -1.0, -0.5, 0.0, 0.5, 1.0, "", "aa", "ab"],
//     ];

function convert($var)
{
    if (is_numeric($var)) {
        return $var < 0 ? '0' . var_export($var, true) : var_export($var, true);
    } else {
        $var = var_export($var, true);
        $var = str_replace("NULL", "null", $var);
        $var = str_replace("'", "\"", $var);
        return $var;
    }
}

function escape($var)
{
    return str_replace("\"", "\\\"", $var);
}

print_r("<?php\ndeclare(strict_types=1);\n");
foreach ($vars_sets as $vars) {
    foreach ($vars as $var1) {
        foreach ($vars as $key => $var2) {
            $a = convert($var1, true);
            $b = convert($var2, true);
            $a_e = escape($a);
            $b_e = escape($b);
            if ($var1 < $var2) {
                print_r(sprintf("if (%s < %s) {} else { write(\"fail %s < %s\\n\"); }\n", $a, $b, $a_e, $b_e));
            } else {
                print_r(sprintf("if (%s < %s) { write(\"fail %s < %s\\n\"); } else {}\n", $a, $b, $a_e, $b_e));
            }
        }
    }
}
print_r("write(\"done\");\n");
