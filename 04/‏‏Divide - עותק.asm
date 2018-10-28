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

(CONTINUE)
@counter
M=M>>  // counter /= 2
@temp
M=M>>  // temp /= 2


@counter
D=M
@END
D;JEQ  // the case that R14 > R13 (the result is 0 )

@R13
D=M
@temp
D=M-D
@remainder
M=D  // remainder = temp - divident (when: temp > divident )

@R14
D=M
@temp
M=D  // temp = R14 (divisor)

(REMINDER_WHILE)
@temp
D=M
@remainder
D=D-M
@END
D;JGT  // in case that temp > remainder

@counter
M=M<<  // counter += 1
@temp
M=M<<  // temp = temp * 2

@REMINDER_WHILE
0;JMP

(END)
@counter
D=M
@R15
M=D  // R15 = counter


(FINALE)
@FINALE
0;JMP