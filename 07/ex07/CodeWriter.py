"""writes the assembler code that implements the parsed command"""

"""imports"""
import os
from Parser import Parser
import help_tables

"""constants"""
PUSH = "push"
POP = "pop"
ADD = "add"
SUB = "sub"
NEG = "neg"
label_arithmetic = ["eq", "gt", "lt"]
AND = "and"
OR = "or"
NOT = "not"
VM_ENDING = "vm"
ASM_ENDING = "asm"
COMMENT = "// "
SPACE = " "
STATIC = "static"
CONNECTOR = "_"
TEMP = "temp"
POINTER = "pointer"
GET_NUM = "get_i"
CONSTANT = "constant"


class CodeWriter:
    """
    this class performs the translation of the vm file into a asm file
    """

    def __init__(self, in_path):
        self.all_commands = Parser(in_path).get_commands()
        self.all_asm_commands = []
        self.file_name = os.path.basename(in_path).split(".")[0]
        self.out_path = in_path.replace(VM_ENDING, ASM_ENDING)
        self.label_counter = 0
        self.handle_commands()

    def handle_commands(self):
        """
        this function goes throw all the commands in vm language and converts them into assembles
        thats with using the single command translator helper function
        :return: None
        """
        for command in self.all_commands:
            self.all_asm_commands.append(COMMENT + command)
            self.all_asm_commands.extend(self.handle_single_command(command))
            # write to file - the command in comment, and then the array of asm commands
            self.write_to_file()

    def handle_single_command(self, command):
        """
        this function handles a single command. translates it to assembler and returns a list of strings with
        the new command
        :param command: the command we want to translate
        :return: the command in assembler language
        """
        if command.startswith(PUSH):
            return self.push_command(command)
        elif command.startswith(POP):
            return self.pop_command(command)
        elif command in label_arithmetic:
            self.label_counter += 1
            return help_tables.asm_commands[command](self.label_counter)
        else:
            return help_tables.asm_commands[command]

    def push_command(self, command):
        """
        this function handles only commands from type: "push segment i".
        :param command: the vm command
        :return: None
        """
        order, segment, i = command.split()
        new_command = []
        if segment == STATIC:
            new_command.extend(help_tables.asm_commands[segment + CONNECTOR + order](self.file_name, i))
        elif segment == TEMP or segment == POINTER:
            new_command.extend(help_tables.asm_commands[segment + CONNECTOR + order](i))
        # elif segment == POINTER:
        #     new_command.extend(help_tables.asm_commands[segment + CONNECTOR + order](i))
        # new_command.extend(help_tables.asm_commands[order])
        else:
            # addr = i
            new_command.extend(help_tables.asm_commands[GET_NUM](i))

            if segment != CONSTANT:
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
        elif segment == "temp":
            new_command.extend(help_tables.asm_commands["temp_pop"](i))
        elif segment == "pointer":
            new_command.extend(help_tables.asm_commands["pointer_pop"](int(i)))
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
