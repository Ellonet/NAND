// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/mult/Mult.tst

load Sort.asm,
output-file Sort.out,
compare-to Sort2.cmp,
output-list RAM[2048]%D2.10.1 RAM[2049]%D2.10.1 RAM[2050]%D2.10.1
RAM[2051]%D2.10.1 RAM[2052]%D2.10.1;

set RAM[14] 2048,   // All positive
set RAM[15] 5,
set RAM[2048] 2333,
set RAM[2049] 2,
set RAM[2050] 101,
set RAM[2051] 5000,
set RAM[2052] 56
;
repeat 1000 {
  ticktock;
}
output;

set PC 0,
set RAM[14] 2048,   // Sorted
set RAM[15] 5,
set RAM[2048] 2333,
set RAM[2049] 245,
set RAM[2050] 10,
set RAM[2051] 5,
set RAM[2052] -56
; 
repeat 1000 {
  ticktock;
}
output;

set PC 0,
set RAM[14] 2048,   // Increasing order
set RAM[15] 5,
set RAM[2048] -56,
set RAM[2049] 5,
set RAM[2050] 10,
set RAM[2051] 245,
set RAM[2052] 2333
; 
repeat 1000 {
  ticktock;
}
output;

set PC 0,
set RAM[14] 2048,   // Negative, Positive and zero 
set RAM[15] 5,
set RAM[2048] -56,
set RAM[2049] 245,
set RAM[2050] 0,
set RAM[2051] -245,
set RAM[2052] 2333
; 
repeat 1000 {
  ticktock;
}
output;

set PC 0,
set RAM[14] 2048,   // Duplicates
set RAM[15] 5,
set RAM[2048] 0,
set RAM[2049] -5,
set RAM[2050] -5,
set RAM[2051] 245,
set RAM[2052] 245
; 
repeat 1000 {
  ticktock;
}
output;

set PC 0,
set RAM[14] 2048,   // Very big numbers 1
set RAM[15] 5,
set RAM[2048] -16384,
set RAM[2049] 16384,
set RAM[2050] 0,
set RAM[2051] 16382,
set RAM[2052] -1
; 
repeat 1000 {
  ticktock;
}
output;

set PC 0,
set RAM[14] 2048,   // Very big numbers 2
set RAM[15] 5,
set RAM[2048] -16383,
set RAM[2049] -16384,
set RAM[2050] 0,
set RAM[2051] 16383,
set RAM[2052] 16384
; 
repeat 1000 {
  ticktock;
}
output;

set PC 0,
set RAM[14] 2048,   // Very big numbers 3
set RAM[15] 5,
set RAM[2048] 0,
set RAM[2049] -16384,
set RAM[2050] -2,
set RAM[2051] 16384,
set RAM[2052] 16383
; 
repeat 1000 {
  ticktock;
}
output;