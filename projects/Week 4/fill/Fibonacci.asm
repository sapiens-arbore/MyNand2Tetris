// place in R0 your desired fibonacci's number 1
//fibpev previous fib 0
//fibcur current fib 1

//zero previous values
@fibcur
M=0
@fibprev
M=0
@fibsum
M=0
// Set to first value fibcur 1 and fibprev 0
@fibcur
M=M+1
//if == 1 jmp to end
@R0
D=M-1
@END
D;JEQ
(LOOP)
  @R0
  D=M-1
  @END
  D;JEQ
  //calculate next fibonacci put it in fibsum
  @fibcur
  D=M
  @fibprev
  D=D+M
  @fibsum
  M=D
  //fibprev = fibcur, fibcur = fibsum
  @fibcur
  D=M
  @fibprev
  M=D
  @fibsum
  D=M
  @fibcur
  M=D
  //coutner R0 -= 1
  @R0
  M=M-1
  //loop
  @LOOP
  0;JMP
(END)
  @END
  0;JMP
  

