EnteredFilename = input("Please enter file, that you want to be assembled: ")
try:
    # Get file and read lines from it
    OpenedAsmFile = open(EnteredFilename, 'r')    
    OpenedAsmFileLines = OpenedAsmFile.readlines()
    # Open/create file with the name of asm file
    OutputFile = open(EnteredFilename.split(".")[0]+"My.hack", "w")
    # Initialization of Symbol table with pre-defined symbols
    SymbolTable = {
        "THIS":"3",
        "THAT":"4",
        "SP":"0",
        "LCL":"1",
        "ARG":"2",
        "SCREEN":"16384",
        "KBD":"24576",
        "R0":"0",
        "R1":"1",
        "R2":"2",
        "R3":"3",
        "R4":"4",
        "R5":"5",
        "R6":"6",
        "R7":"7",
        "R8":"8",
        "R9":"9",
        "R10":"10",
        "R11":"11",
        "R12":"12",
        "R13":"13",
        "R14":"14",
        "R15":"15",
    }
    # Table for computation part of C instruction
    CompTable = {
        "0":"0101010",
        "1":"0111111",
        "-1":"0111010",
        "D":"0001100",
        "A":"0110000",
        "!D":"0001101",
        "!A":"0110001",
        "-D":"0001111",
        "-A":"0110011",
        "D+1":"0011111",
        "A+1":"0110111",
        "D-1":"0001110",
        "A-1":"0110010",
        "D+A":"0000010",
        "D-A":"0010011",
        "A-D":"0000111",
        "D&A":"0000000",
        "D|A":"0010101",
        "M":"1110000",
        "!M":"1110001",
        "-M":"1110011",
        "M+1":"1110111",
        "M-1":"1110010",
        "D+M":"1000010",
        "D-M":"1010011",
        "M-D":"1000111",
        "D&M":"1000000",
        "D|M":"1010101"
    }
    # Table for destination part of C instruction
    DestTable = {
        "null":"000",
        "M":"001",
        "D":"010",
        "MD":"011",
        "A":"100",
        "AM":"101",
        "AD":"110",
        "AMD":"111"
    }
    # Table for jump part of C instruction
    JmpTable = {
        "null":"000",
        "JGT":"001",
        "JEQ":"010",
        "JGE":"011",
        "JLT":"100",
        "JNE":"101",
        "JLE":"110",
        "JMP":"111",
    }


    # Parser first pass (check for all lables)
    current_command = 0
    for LineDirty in OpenedAsmFileLines:
        line = LineDirty.strip()
        # check if line start with // or with empty, then skip it
        if(line.startswith("//") or not line):
            continue        
        # check if is label
        elif(line.startswith("(")):
            # Add label to SymbolTable
            SymbolTable.setdefault(line.replace("(", "").replace(")", ""), str(current_command))
        else:
            current_command += 1
    # From what address to start replacing unique symbols with
    free_address = 16
    

    # Main parser loop
    for LineDirty in OpenedAsmFileLines:
        line = LineDirty.strip()
        # check if line start with // or with empty or labels(we already handled them), then skip it
        if(line.startswith("//") or line.startswith("(") or not line):
            continue
        # handle A instructions
        elif(line.startswith("@")):
            # if is not number it means it is some kind of symbol, if it is label or pre-dfeined symbol it is 
            # already in symbol table and will not be added another time, if it is not it will be added with free memory address
            if not (line[1].isdigit()):
                if line[1:] not in SymbolTable:
                    SymbolTable.setdefault(line[1:].strip(),str(free_address))
                    free_address += 1
                OutputFile.write("0" + "0" * (15-len(str(bin(int(SymbolTable[line[1:].strip()]))[2:]))) + bin(int(SymbolTable[line[1:].strip()]))[2:] + "\n")
            else:
                OutputFile.write("0" + "0" * (15-len(str(bin(int(line[1:].strip()))[2:]))) + bin(int(line[1:].strip()))[2:] + "\n")
        # handle labels
        elif(line[0].strip() == "("):
            OutputFile.write(line.replace("(", "").replace(")", ""))
        # handle C instructions dest = comp; jump
        else:
            # destination is part before =
            dest = line.split("=")[0]
            # try to take part between = and ;, if you cannot do this, it means that instruction is something like
            # D;JMP or A+M;JMP, so there is no destination
            try:
                comp = line.split(";")[0].split("=")[1]
            except IndexError:
                # if there is no destination, it means destination is null, but everything on the left to ; is computation
                dest = "null"
                comp = line.split(";")[0]
            # try to take last 3 letters after ;, like JMP or JGT
            try:
                jmp = line.split(";")[1][:3]
            # if you cannot do this, it means there is no jump
            except IndexError:
                jmp = "null"
            OutputFile.write("111" + CompTable[comp] + DestTable[dest] + JmpTable[jmp] + "\n")
                
    # Close output file        
    OutputFile.close()

except FileNotFoundError:
    print("Sorry, your file was not found in this directory, try placing HackAssembler.py in the same directory as source file")