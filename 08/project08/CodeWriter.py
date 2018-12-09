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
SEG_I = "seg_i"
CALL = "call"
FUNCTION = "function"
RETURN = "return"
LABEL = "label"
IF_GOTO = "if-goto"
GOTO = "goto"
GOTO_FUNC = "goto_function"
GOTO_ADDRESS = "goto_address"
INIT_FUNC = "Sys.init"
INIT = "init"
SET_LABEL = "set_label"
PUSH_0 = "push constant 0"
SAVE_ADDRESS = "save_address"
SAVE_POINTERS = "save_pointers"
SET_ARG = "set_arg"
SET_LCL = "set_lcl"
SET_LABEL_COUNT = "set_counted_label"
RETURN_LABEL = "RETURN_ADDRESS"
SAVE_END_FRAME = "save_endFrame"
RESTORE_POINTER = "restore_pointer"
R15 = "@R15"
POP_TO_ARG = "pop_to_arg"
RETURN_SP = "return_sp"


class CodeWriter:
    """
    this class performs the translation of the vm file into a asm file
    """

    def __init__(self, in_path, write_to_file_flag=True, counter=0, is_first=False):
        self.label_counter = counter
        self.all_commands = Parser(in_path).get_commands()
        if write_to_file_flag or is_first:
            self.all_asm_commands = self.write_init()
        else:
            self.all_asm_commands = []
        self.file_name = os.path.basename(in_path).split(".")[0]
        self.out_path = in_path.replace(VM_ENDING, ASM_ENDING)
        self.handle_commands(write_to_file_flag)
        self.write_to_File_flag = write_to_file_flag

    def handle_commands(self, write_to_File_flag):
        """
        this function goes throw all the commands in vm language and converts them into assembles
        that is with using the single command translator helper function
        :return: None
        """
        for command in self.all_commands:
            self.all_asm_commands.append(COMMENT + command)
            self.all_asm_commands.extend(self.handle_single_command(command))
            # write to file - the command in comment, and then the array of asm commands
            if write_to_File_flag:
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
        elif command.startswith(CALL):
            call, function_name, n_args = command.split(SPACE)
            self.label_counter += 1
            return self.write_call(function_name, n_args)
        elif command.startswith(FUNCTION):
            call, function_name, num_vars = command.split(SPACE)
            self.label_counter += 1
            return self.write_function(function_name, num_vars)
        elif command.startswith(RETURN):
            return self.write_return()
        elif command.startswith(LABEL):
            return self.write_label(command.split(SPACE)[1])
        elif command.startswith(GOTO):
            return self.write_goto(command.split(SPACE)[1])
        elif command.startswith(IF_GOTO):
            return self.write_if(command.split(SPACE)[1])
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
        elif segment in [TEMP, POINTER]:
            new_command.extend(help_tables.asm_commands[segment + CONNECTOR + order](i))
        else:
            # adding command: addr = i
            new_command.extend(help_tables.asm_commands[GET_NUM](i))

            if segment != CONSTANT:
                # adding command: addr = i + segment pointer;
                new_command.extend(help_tables.asm_commands[SEG_I + CONNECTOR + order](segment))

            # adding command: *sp = *addr; SP ++
            new_command.extend(help_tables.asm_commands[PUSH])
        return new_command

    def pop_command(self, command):
        order, segment, i = command.split(" ")
        new_command = []
        if segment == STATIC:
            new_command.extend(help_tables.asm_commands[segment + CONNECTOR + order](self.file_name, i))
        elif segment in [TEMP, POINTER]:
            new_command.extend(help_tables.asm_commands[segment + CONNECTOR + order](i))
        else:
            # adding command: addr = seg + i;`
            new_command.extend(help_tables.asm_commands[GET_NUM](i))
            new_command.extend(help_tables.asm_commands[SEG_I + CONNECTOR + order](segment))
            # adding command: SP --; *sp = *addr
            new_command.extend(help_tables.asm_commands[POP])
        return new_command

    def write_to_file(self):
        with open(self.out_path, "w") as out_file:
            for line in self.all_asm_commands:
                out_file.write(line + "\n")

    def get_all_commands(self):
        return self.all_asm_commands

    def write_init(self):
        """
        writes the assembly introduction that effects the bootstop code that initializes the VM.
        :return:
        """
        asm_command = help_tables.extended_asm[INIT]
        asm_command.extend(self.write_call(INIT_FUNC, "0"))
        return asm_command

    def write_label(self, label):
        """
        writes assembly code that effects the label command
        :param label: the string of the label name
        :return:
        """
        return help_tables.extended_asm[SET_LABEL](label)

    def write_goto(self, label):
        """
        writes assembly code that effects the goto command
        :param label: the string of the label name
        :return:
        """
        return help_tables.extended_asm[GOTO_FUNC](label)

    def write_if(self, label):
        """
        writes assembly code that effects the if-goto command
        :param label: the string of the label name
        :return:
        """
        return help_tables.extended_asm[IF_GOTO](label)

    def write_function(self, function_name, num_vars):
        """
        writes assembly code that effects the function command
        :param function_name: the string of the function name
        :param num_vars: the number of variables givrn to the function
        :return:
        """
        asm_command = help_tables.extended_asm[SET_LABEL](function_name)
        for i in range(int(num_vars)):
            asm_command.extend(self.push_command(PUSH_0))
        return asm_command

    def write_call(self, function_name, num_args):
        """
        writes assembly code that effects the function command
        :param function_name: the string of the function name
        :param num_args: the number of arguments of the function
        :return:
        """
        asm_command = []
        # save the address of the next line
        asm_command.extend(
            help_tables.extended_asm[SAVE_ADDRESS](self.label_counter) + help_tables.asm_commands[PUSH])
        # save the pointers values
        for pointer in help_tables.pointer_list:
            asm_command.extend(help_tables.extended_asm[SAVE_POINTERS](pointer))
        # reposition ARG
        asm_command.extend(help_tables.extended_asm[SET_ARG](num_args))
        # reposition LCL
        asm_command.extend(help_tables.extended_asm[SET_LCL])
        # goto the callee function
        asm_command.extend(help_tables.extended_asm[GOTO_FUNC](function_name))
        # return address
        asm_command.extend(help_tables.extended_asm[SET_LABEL_COUNT](RETURN_LABEL, self.label_counter))
        return asm_command

    def write_return(self):
        """
        writes assembly code that effects the return command
        :return:
        """
        asm_command = help_tables.extended_asm[SAVE_END_FRAME]
        asm_command.extend(help_tables.extended_asm[RESTORE_POINTER](str(5), R15))
        asm_command.extend(help_tables.extended_asm[POP_TO_ARG])
        asm_command.extend(help_tables.extended_asm[RETURN_SP])
        for i in range(1, 5):
            asm_command.extend(help_tables.extended_asm[RESTORE_POINTER](str(i), help_tables.pointer_list[-i]))
        asm_command.extend(help_tables.extended_asm[GOTO_ADDRESS]("R15"))

        return asm_command
