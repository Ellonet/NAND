// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/06/pong/PongL.asm

// Symbol-less version of the Pong.asm program.

(firstlable)
@256
D=A
@0
(label-4)
M=D
@133
0;JMP
@15
M=D
@0
AM=M-1
D=M
A=A-1
D=M-D
M=0
@19
D;JNE
(blabla-17)
@0
A=M-1
M=-1
@15
A=M
0;JMP
@15
M=D
@0
AM=M-1
D=M
A=A-1
D=M-D
M=0
@35
D;JLE
@0
A=M-1
M=-1
@15				// bla bla bla
A=M
0;JMP//testing
@15	// bla
M=D // fdfdf
@0
AM=M-1