// This file was created by Evyatar.


load LT2.asm,
output-file LT2.out,
compare-to LT2.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2;

set RAM[0] 256,  // initializes the stack pointer 

repeat 200 {      // enough cycles to complete the execution
  ticktock;
}

output;          // the stack pointer and the stack base
