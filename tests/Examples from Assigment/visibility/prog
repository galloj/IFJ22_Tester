<?php
declare(strict_types=1);

$y = 10;  // local variable in main body

function foo(int $x) : void {
  $y = "hello";  // local variable in this function
  if (1 === 1) {
    $y = 42;     // not new local variable, rewrites $y from line 7
    write($y);  // prints 42
  } else {
    write($y);
  }
  write($y); // prints 42, because $y on line 9 is not new local variable, just overwrites the one from line 7
  
  $i = 1;
  while ($i <= 10) {
    $i = 5; // not new local variable just for this block, but local variable of the whole function is used 
    $i = $i + 1;
    write($i);  // looping condition is always true (always prints 6)
    write("Insert non-empty input for quiting, otherwise next iteration.\n");
    $x = reads();  // formal parameter behave in the function body as local variable (can be modified)
    $inp = strlen($x);
    if ($inp !== 0) { write($x); return; } else {}  // explicitly stops looping by exiting foo
  }
}

foo(7);
write($y);  // prints 10, $y in main body is different from $y in foo

// whitespaces and comment possible since now end-mark here
    