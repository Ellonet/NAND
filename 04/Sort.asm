// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, M.I.T Press.
// File name: projects/04/Sort.asm

// The program should sort the array starting at the address in R14 with length 
// as specified in R15. Don't change these registers.



@R15
D=M
@n  // get number of items in the array
M=D  

@END  // check if n=0 or n=1 then end the program (the array is sorted)
D;JEQ
D=D-1
@END
D;JEQ


(BUBBLE_SORT)
@swapFlag
M=0

@R15
D=M
@n  // get number of items in the array
M=D  

@R14
D=M
@address  // get the adress of the beginning of the array
M=D

(FOR)
@address
A=M
D=M
@first  // first = array[address]
M=D
@address
A=M+1
D=M
@second  // second = array[address+1]
M=D

@first
D=M
@second
D=D-M  // second - first
@DONT_SWAP  // in case that first > second then dont swap 
D;JGT

@swapFlag
M=1

// swaping the values in the array
@address
A=M
D=M
@temp  
M=D			// temp = array[address]
@address	
A=M+1
D=M
@address  
A=M
M=D			// put array[address+1] in to array[address]
@temp		
D=M
@address  
A=M+1
M=D			// array[address+1] = temp

(DONT_SWAP)
@address
M=M+1
@n
M=M-1
D=M

@FOR
D-1;JNE

@swapFlag
D=M
@BUBBLE_SORT
D;JNE  // in case that a swap was made go to enother round

(END)