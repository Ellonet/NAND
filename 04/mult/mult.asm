// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

@sum
M=0  //sum=0

@i
M=0  // set iterations counter to zero

@R2  
M=0  // initialize R2

@R0
D=M   // get R0  

@R1
D=D-M  //get difference (R0-R1)

@NEGATIVE
D;JLT  // jump if R1>R0

(POSITIVE) // the case that R0>R1 
@R0
D=M
@biggerNum // set biggerNum=R0
M=D

@R1  
D=M
@n  // set n=R1 (num of iterations)
M=D

@LOOP // continue to the LOOP 
0;JMP

(NEGATIVE)  //the case that R1>R0 
@R1
D=M
@biggerNum  //set biggerNum to R1
M=D

@R0
D=M
@n  //set num of iterations to R0
M=D

(LOOP)
@i
D=M
@n
D=D-M  // while i<n
@STOP
D;JEQ // (if i-n = 0) stop the loop

@sum
D=M
@biggerNum
D=D+M
@sum   //sum += biggerNum
M=D

@i
M=M+1  //i=i+1
@LOOP
0;JMP

(STOP)
@sum
D=M
@R2  //R2 = R0*R1
M=D

(END)
@END
0;JMP
