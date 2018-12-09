// File name: VMTest.tst

load VMTest.asm,
output-file VMTest.out,
compare-to VMTest.cmp,
output-list RAM[256]%D2.6.2 RAM[257]%D2.6.2 RAM[258]%D2.6.2 RAM[259]%D2.6.2 RAM[260]%D2.6.2 RAM[261]%D2.6.2;

set RAM[0] 256,  // initializes the stack pointer
set RAM[1] 600,
set RAM[2] 700,

repeat 650 {    // enough cycles to complete the execution
  ticktock;
}

output;
output-list RAM[262]%D2.6.2 RAM[263]%D2.6.2 RAM[264]%D2.6.2 RAM[265]%D2.6.2 RAM[266]%D2.6.2 RAM[267]%D2.6.2;
output;
output-list RAM[0]%D2.6.2 RAM[600]%D2.6.2 RAM[700]%D2.6.2 RAM[16]%D2.6.2 RAM[4000]%D2.6.2 RAM[5000]%D2.6.2 RAM[8]%D2.6.2;
output;
