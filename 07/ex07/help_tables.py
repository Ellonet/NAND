asm_commands = {
    "push": ["@SP", "A=M", "M=D", "@SP", "M=M+1"],
    "static_push": lambda file_name, i: ["@" + file_name + "." + i, "D=M", "@SP", "A=M", "M=D", "@SP", "M=M+1"],
    "pop": ["@R13", "M=D", "@SP", "M=M-1", "A=M", "D=M", "@R13", "A=M", "M=D"],
    "static_pop": lambda file_name, i: ["@SP", "M=M-1", "A=M", "D=M", "@" + file_name + "." + i, "M=D"],
    "get_i": lambda i: ["@" + i, "D=A"],
    "seg_i_pop": lambda seg: [memory_pointers[seg], "D=M+D"],
    "seg_i_push": lambda seg: [memory_pointers[seg], "D=M+D", "A=D", "D=M"],
    # "static":
}

memory_pointers = {
    "local": "@LCL", "argument": "@ARG", "this": "@THIS", "that": "@THAT"
}
