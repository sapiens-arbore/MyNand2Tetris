//Store 2 numbers in register R0 and R1 in R2 will be the result ,R3 is 4
// R2=0
// R0 IS A COUNTER !!!!!!!!!!!!!!!!!!!!!!!!!!!
// IF R0=0 JUMP TO END
// ELSE
//   D=R2
//   D += R1
//   R2 = D
//   LOOP

//start, set sum to 0
@R2
M=0


(LOOP)
  //check if counter R0 is zero
  @R0
  D=M
  //if it is jump to end
  @END
  D;JEQ
  //add R1 to sum
  @R2
  D=M
  @R1
  D=D+M
  //return result to R2
  @R2
  M=D
  //counter -= 1
  @R0
  M=M-1
  @LOOP
  0;JMP


(END)
@end
0;JMP

