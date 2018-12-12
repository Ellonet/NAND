// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/mult/Mult.tst

load Divide.asm,
output-file Divide.out,
compare-to Divide.cmp,
output-list RAM[13]%D2.8.2 RAM[14]%D2.8.2 RAM[15]%D2.8.2;

set RAM[13] 4,   // Set test arguments
set RAM[14] 2,
set RAM[15] 0;	//2
repeat 200 {
  ticktock;
}
output;

set PC 0,
set RAM[13] 5,   // Set test arguments
set RAM[14] 2,
set RAM[15] 0;	//2
repeat 200 {
  ticktock;
}
output;

set PC 0,
set RAM[13] 5,   // Set test arguments
set RAM[14] 3,
set RAM[15] 0;	//1
repeat 200 {
  ticktock;
}
output;

set PC 0,
set RAM[13] 9,   // Set test arguments
set RAM[14] 3,
set RAM[15] 0;	//3
repeat 200 {
  ticktock;
}
output;

set PC 0,
set RAM[13] 4,   // Set test arguments
set RAM[14] 3,
set RAM[15] 0;	//1
repeat 200 {
  ticktock;
}
output;

set PC 0,
set RAM[13] 1,   // Set test arguments
set RAM[14] 1,
set RAM[15] 0;  // 1
repeat 200 {
  ticktock;
}
output;

set PC 0,
set RAM[13] 7,   // Set test arguments
set RAM[14] 1,
set RAM[15] 0;	//7
repeat 200 {
  ticktock;
}
output;

set PC 0,
set RAM[13] 3,   // Set test arguments
set RAM[14] 5,
set RAM[15] 0;  // 0
repeat 200 {
  ticktock;
}
output;

set PC 0,
set RAM[13] 16383,   // Set test arguments
set RAM[14] 85,
set RAM[15] 0;  // 192
repeat 2000 {
  ticktock;
}
output;

set PC 0,
set RAM[13] 32767,   // Set test arguments
set RAM[14] 11,
set RAM[15] 0;  // 2978
repeat 2000 {
  ticktock;
}
output;

set PC 0,
set RAM[13] 32767,   // Set test arguments
set RAM[14] 32000,
set RAM[15] 0;  // 1
repeat 1000 {
  ticktock;
}
output;

set PC 0,
set RAM[13] 32000,   // Set test arguments
set RAM[14] 32767,
set RAM[15] 0;  // 0
repeat 1000 {
  ticktock;
}
output;


set PC 0,
set RAM[13] 32767,   // Set test arguments
set RAM[14] 1,
set RAM[15] 0;  // 32767
repeat 2000 {
  ticktock;
}
output;

set PC 0,
set RAM[13] 32767,   // Set test arguments
set RAM[14] 32767,
set RAM[15] 0;  // 1
repeat 1000 {
  ticktock;
}
output;


set PC 0,
set RAM[13] 1,   // Set test arguments
set RAM[14] 32767,
set RAM[15] 0;  // 0
repeat 1000 {
  ticktock;
}
output;