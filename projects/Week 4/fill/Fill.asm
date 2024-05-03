// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.

//// Replace this comment with your code.


// LOOP
//  if keyboard = 0
//    print 00000000000000000
//  if keyboard != 0
//    print 01010101010101010
//  
//
//
//
//
//
//
//
//scraddr now saves screeen address
@SCREEN
D=A
@scraddr
M=D
//main loop check keyboard
(LOOP)
  @KBD
  D=M
  //if whit jump to whit if blck jump to blck
  @WHITE
  D;JEQ
  @BLACK
  D;JNE

(WHITE)
// set n to 8000
  @8192
  D = A
  @n
  M=D
  (WHITELOOP)
    @scraddr
    D=M
    @n
    A=D+M
    M=0
    @n
    M=M-1
    D = M
    @WHITELOOP
    D;JGE
    @LOOP
    0;JMP
(BLACK)
  @8192
  D = A
  @n
  M=D
  (BLACKLOOP)
    @scraddr
    D=M
    @n
    A=D+M
    M=-1
    @n
    M=M-1
    D=M
    @BLACKLOOP
    D;JGE
    @LOOP
    0;JMP



