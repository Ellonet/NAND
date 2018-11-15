asm_commands = {
    "pointer_push": lambda i: ["@THAT", "D=M"] if i else ["@THIS", "D=M"],
    "pointer_pop": lambda i: ["@SP", "AM=M-1", "D=M", "@THAT", "M=D"] if i else ["@SP", "AM=M-1", "D=M",
                                                                                 "@THIS", "M=D"],
    "push": ["@SP", "AM=M+1", "A=A-1", "M=D"],
    "static_push": lambda file_name, i: ["@" + file_name + "." + i, "D=M", "@SP", "A=M", "M=D", "@SP", "M=M+1"],
    "static_pop": lambda file_name, i: ["@SP", "AM=M-1", "D=M", "@" + file_name + "." + i, "M=D"],
    "pop": ["@R13", "M=D", "@SP", "AM=M-1", "D=M", "@R13", "A=M", "M=D"],
    "temp_push": lambda i: ["@" + str(5 + int(i)), "D=M", "@SP", "AM=M+1", "A=A-1", "M=D"],
    "temp_pop": lambda i: ["@SP", "AM=M-1", "D=M", "@" + str(5 + int(i)), "M=D"],
    "get_i": lambda i: ["@" + i, "D=A"],
    "seg_i_pop": lambda seg: [memory_pointers[seg], "D=M+D"],
    "seg_i_push": lambda seg: [memory_pointers[seg], "D=M+D", "A=D", "D=M"],
    "add": ["@SP", "AM=M-1", "D=M", "A=A-1", "M=D+M"],
    "sub": ["@SP", "AM=M-1", "D=M", "A=A-1", "M=M-D"],
    "neg": ["@SP", "A=M-1", "M=-M"],
    "eq": ["@SP", "AM=M-1", "D=M", "A=A-1", "D=D-M", "@EQUAL", "D;JEQ", "@SP", "A=M-1", "M=0", "@END", "0;JMP",
           "(EQUAL)", "@SP", "A=M-1", "M=-1", "(END)"],
    "gt": ["@SP", "AM=M-1", "@NEG_Y", "M;JLT", "A=A-1", "@NEG_X_POS_Y", "M;JLT", "@SP", "A=M", "D=M", "A=A-1", "D=M-D",
           "@GREATER", "D;JGT", "@SMALLER", "0;JMP", "(NEG_Y)", "@SP", "A=M-1", "@NEG_Y_POS_X", "M;JGT", "@SP", "A=M",
           "D=M", "A=A-1", "D=M-D", "@GREATER", "D;JLT", "@SMALLER", "0;JMP", "(NEG_X_POS_Y)", "@SMALLER", "0;JMP",
           "(NEG_Y_POS_X)", "@GREATER", "0;JMP", "(GREATER)", "@SP", "A=M-1", "M=-1", "@END", "0;JMP", "(SMALLER)",
           "@SP", "A=M-1", "M=0", "(END)"],
    "lt": ["@SP", "AM=M-1", "D=M", "A=A-1", "D=M-D", "@LOWER", "D;JLT", "@SP", "A=M-1", "M=0", "@END", "0;JMP",
           "(LOWER)", "@SP", "A=M-1", "M=-1", "(END)"],
    "or": ["@SP", "AM=M-1", "D=M", "A=A-1", "D=M|D", "@SP", "A=M", "M=D"],
    "and": ["@SP", "AM=M-1", "D=M", "A=A-1", "D=M&D", "@SP", "A=M", "M=D"],
    "not": ["@SP", "A=M-1", "M=!M"]
}

memory_pointers = {
    "local": "@LCL", "argument": "@ARG", "this": "@THIS", "that": "@THAT"
}
