// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/07/StackArithmetic/StackTest/StackTest.tst

load MultiTest.vm,

set RAM[0] 256,
set RAM[1] 4096,
set RAM[2] 4196,
set RAM[3] 4226,
set RAM[4] 4246,

repeat 172 {
  vmstep;
}
