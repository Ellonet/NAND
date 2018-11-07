// push constant 7
@7
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 3
@3
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local 1
@1
D=A
@LCL
D=M+D
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// pop local 2
@2
D=A
@LCL
D=M+D
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// pop local 3
@3
D=A
@LCL
D=M+D
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// push local 1
@1
D=A
@LCL
D=M+D
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 100
@100
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 100
@100
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 100
@100
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 99
@99
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop static 1
@SP
M=M-1
A=M
D=M
@testing.1
M=D
// push static 1
@testing.1
D=M
@SP
A=M
M=D
@SP
M=M+1
// push static 1
@testing.1
D=M
@SP
A=M
M=D
@SP
M=M+1
