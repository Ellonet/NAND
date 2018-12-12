// This file was created by Evyatar.


load EQ1.asm,
output-file EQ1.out,
compare-to EQ1.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2;

set RAM[0] 256,  // initializes the stack pointer 

repeat 200 {      // enough cycles to complete the execution
  ticktock;
}

output;          // the stack pointer and the stack base
