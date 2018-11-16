// This file was created by Evyatar.


load EQ2.asm,
output-file EQ2.out,
compare-to EQ2.cmp,
output-list RAM[0]%D2.6.2 RAM[256]%D2.6.2;

set RAM[0] 256,  // initializes the stack pointer 

repeat 200 {      // enough cycles to complete the execution
  ticktock;
}

output;          // the stack pointer and the stack base
