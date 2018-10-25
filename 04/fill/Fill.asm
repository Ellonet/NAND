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

@color
M=0 // init color

@8191
D=A
@iter
M=D  // the number of iterations in the loop (flaten screen size)

(INPUTLOOP)

@i
M=0  // init iterations counter

@SCREEN
D=A
@address
M=D  // init the address to the screen address

@KBD
D=M  //get input

@WHITE
D;JEQ // no input from the user

(BLACK)
@color
M=-1 // set color = black
@LOOP
0;JMP

(WHITE)
@color
M=0  //set color = 0

(LOOP)
@i
D=M
@iter
D=D-M
@INPUTLOOP
D;JEQ  // case i=n (finished coloring the screen)

@i
D=M
@address  // address += i
M=M+D

@color
D=M
@address
A=M // color 16 bit
M=D

@i
M=M+1  //i += 1

@LOOP
0;JMP
