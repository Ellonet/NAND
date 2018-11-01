// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.


(OUTERLOOP)

@KBD	// getting input from the keyboard
D=M
@BLACK
D;JNE

(WHITE) // in case of no input
@color
M=0
@INITIALIZE
0;JMP

(BLACK)	// in case of any input
@color
M=-1

(INITIALIZE)	// intialize the iteration counter 
@8192
D=A
@iter
M=D

@SCREEN		// intialize the screen address to be colored
D=A
@address
M=D

(LOOP)		// the screen coloing loop
@color
D=M
@address
A=M
M=D	// coloring the relevant byte
@address
M=M+1	// moving to the next byte
@iter
M=M-1	// reducing the iteration counter by 1
D=M

@LOOP	
D;JNE

@OUTERLOOP	// return to the beginning for next input
0;JMP