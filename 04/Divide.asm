// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, M.I.T Press.
// File name: projects/04/Divide.asm

// The program input will be at R13,R14 while the result R13/R14 will '
// be stored at R15. Don't change the input registers.
// The remainder should be discarded.


@counter
M=1  // init the counter to zero

@R15
M=0  // init the answer register

@R14
D=M
@temp 
M=D  // set the temp value to the value of the divisor

(WHILE)
@temp
D=M
@R13
D=D-M
@CONTINUE
D;JGT  // in case that temp > R13 (the divident)

@counter
M=M<<  // counter *= 2
@temp
M=M<<  // temp = temp * 2

@WHILE
0;JMP

(CONTINUE)  // return the counter and the temp to the biggest legal value
@counter
M=M>>  // counter /= 2
@temp
M=M>>  // temp /= 2

@counter
D=M
@R15
M=D  // result = counter 

@R13
D=M
@temp
D=D-M
@remainder
M=D  // remainder = divident - temp (when: temp > divident )

(WHILE_REMINDER)
@temp
M=M>>  // temp /= 2
@counter
M=M>>  // counter /= 2

@remainder
D=M
@temp
D=M-D  // temp - remainder
@counter
@WHILE_REMINDER
D;JGT  // remainder < temp

@temp
D=M
@remainder
M=M-D  // remainder = remainder - temp
@counter
D=M
@R15
M=M+D  // result += counter

@WHILE_REMINDER
D;JGT  // while the counter > 0

