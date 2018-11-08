"""writes the assambly code that implements the parsed command"""
import os

from Parser import Parser
import help_tables

PUSH = "push"
POP = "pop"
ADD = "add"
SUB = "sub"
NEG = "neg"
EQ = "eq"
GT = "gt"
LT = "lt"
AND = "and"
OR = "or"
NOT = "not"


class CodeWriter:
    def __init__(self, in_path):
        self.all_commands = Parser(in_path).get_commands()
        self.all_asm_commands = []
        self.file_name = os.path.basename(in_path).split(".")[0]
        # self.file_name = os.path.splitext(in_path)[0]
        print(self.file_name)
        self.out_path = in_path.replace(".vm", ".asm")
        self.handle_commands()

    def handle_commands(self):
        for command in self.all_commands:
            self.all_asm_commands.append("// " + command)
            self.all_asm_commands.extend(self.handle_single_command(command))
            # write to file - the command in comment, and then the array of asm commands
            self.write_to_file()

    def handle_single_command(self, command):
        if command.startswith(PUSH):
            return self.push_command(command)
        elif command.startswith(POP):
            return self.pop_command(command)
        else:
            return []

    def push_command(self, command):
        order, segment, i = command.split(" ")
        new_command = []
        if segment == "static":
            new_command.extend(help_tables.asm_commands["static_push"](self.file_name, i))
        else:
            # addr = i;
            new_command.extend(help_tables.asm_commands["get_i"](i))

            if segment != "constant":
                # addr = i + segment pointer;
                new_command.extend(help_tables.asm_commands["seg_i_push"](segment))

            # *sp = *addr; SP ++
            new_command.extend(help_tables.asm_commands["push"])
        return new_command

    def pop_command(self, command):
        order, segment, i = command.split(" ")
        new_command = []
        if segment == "static":
            new_command.extend(help_tables.asm_commands["static_pop"](self.file_name, i))
        else:
            # addr = seg + i;`
            new_command.extend(help_tables.asm_commands["get_i"](i))
            new_command.extend(help_tables.asm_commands["seg_i_pop"](segment))
            # SP --; *sp = *addr
            new_command.extend(help_tables.asm_commands["pop"])
        return new_command

    def write_to_file(self):
        with open(self.out_path, "w") as out_file:
            for line in self.all_asm_commands:
                out_file.write(line + "\n")
