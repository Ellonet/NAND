// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/07/StackArithmetic/StackTest/StackTest.tst

load StaticDirTest.asm,
output-file StaticDirTest.out,
compare-to StaticDirTest.cmp,

set RAM[0] 256,


repeat 2000 {
  ticktock;
}

output-list RAM[0]%D2.6.2;
output;
output-list RAM[16]%D2.6.2 RAM[17]%D2.6.2 RAM[18]%D2.6.2 RAM[19]%D2.6.2 RAM[20]%D2.6.2 RAM[21]%D2.6.2 RAM[22]%D2.6.2 ;
output;
output-list RAM[23]%D2.6.2 RAM[24]%D2.6.2 RAM[25]%D2.6.2 RAM[26]%D2.6.2 RAM[27]%D2.6.2 RAM[28]%D2.6.2 RAM[29]%D2.6.2 ;
output;
output-list RAM[30]%D2.6.2 RAM[31]%D2.6.2 RAM[32]%D2.6.2 RAM[33]%D2.6.2 RAM[34]%D2.6.2 RAM[35]%D2.6.2 RAM[36]%D2.6.2 ;
output;
output-list RAM[37]%D2.6.2 RAM[38]%D2.6.2 RAM[39]%D2.6.2 RAM[40]%D2.6.2 RAM[41]%D2.6.2 RAM[42]%D2.6.2 RAM[43]%D2.6.2 ;
output;
output-list RAM[44]%D2.6.2 RAM[45]%D2.6.2 RAM[46]%D2.6.2 RAM[47]%D2.6.2 RAM[48]%D2.6.2 RAM[49]%D2.6.2 RAM[50]%D2.6.2 ;
output;
output-list RAM[51]%D2.6.2 RAM[52]%D2.6.2 RAM[53]%D2.6.2 RAM[54]%D2.6.2 RAM[55]%D2.6.2 RAM[256]%D2.6.2 RAM[257]%D2.6.2 ;
output;
output-list RAM[258]%D2.6.2 RAM[259]%D2.6.2 RAM[260]%D2.6.2 RAM[261]%D2.6.2 RAM[262]%D2.6.2 RAM[263]%D2.6.2 RAM[264]%D2.6.2 ;
output;
output-list RAM[265]%D2.6.2 RAM[266]%D2.6.2;
output;

