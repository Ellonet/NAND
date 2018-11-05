"""imports"""
from Parser import Parser
import BinaryTables

"""magic numbers"""
NOT_FOUND = -1
EQUAL = "="
SEMI_COLON = ";"
DEFAULT = "null"
OFF = "0"
ON = "1"
FORMAT15 = '{0:015b}'
A_INSTRUCTION = "@"
OPEN_PARENTHESES = "("
CLOSE_PARENTHESES = ")"


class Assembler:

    def __init__(self, in_path):
        """
        this is the init function. we crate the new symbol table with the constant symbols, extract from the file
        all the commands, initializing the variable address counter and building a binary commands empty list.
        :param in_path: the path of the file we want to read from
        :param out_path: the path where we want to write the new binary code file
        """
        self.symbol_table = {"SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4, "R0": 0, "R1": 1, "R2": 2, "R3": 3,
                             "R4": 4,
                             "R5": 5, "R6": 6, "R7": 7, "R8": 8, "R9": 9, "R10": 10, "R11": 11, "R12": 12, "R13": 13,
                             "R14": 14, "R15": 15, "SCREEN": 16384, "KBD": 24576}
        self.commands = Parser(in_path).get_all_commands()
        self.out_path = in_path.replace(".asm", ".hack")
        self.next_var_address = 16
        self.binary_commands = []
        self.read_commands()

    def extract_labels(self):
        """
        this function goes throw all the commands and only finds the labels. adds each label and gives it a new address
        :return: No return value
        """
        line_counter = 0
        for command in self.commands:
            if command.startswith(OPEN_PARENTHESES) and command.endswith(CLOSE_PARENTHESES):
                self.symbol_table[command[1:-1]] = line_counter
            else:
                line_counter += 1

    def read_commands(self):
        """
        this function reads the commands one by one and translates them to binary language
        :return: no return value
        """
        self.extract_labels()
        for command in self.commands:
            if command.startswith(A_INSTRUCTION):
                self.case_a_command(command[1:])
            elif command.startswith(OPEN_PARENTHESES):
                continue
            else:
                self.case_c_command(command)

        with open(self.out_path, "w") as hack_file:
            for line in self.binary_commands:
                hack_file.write(line + "\n")

    def case_a_command(self, command):
        """
        this function receives an a command in user writing and translates it to binary code
        :param command: the a command
        :return: no return value
        """
        if command.isdigit():
            # add the line in binary writing
            binary = FORMAT15.format(int(command))
            self.binary_commands.append(OFF + binary)
        else:
            address = self.symbol_table.get(command)
            if address is None:  # the variable is not in the table
                address = self.next_var_address  # get the next available address
                self.next_var_address += 1
                self.symbol_table[command] = address  # add the variable to the dictionary
            address_binary = FORMAT15.format(int(address))
            self.binary_commands.append(OFF + address_binary)

    def c_command_parser(self, command):
        """
        this function splits the command to its 3 parts: dest, comp and jump and returns them

        :param command: the command we want to parse
        :return: 3 parameters- dest, comp, jump
        """
        equal_sign = command.find(EQUAL)
        semi_colon_sign = command.find(SEMI_COLON)

        if equal_sign != NOT_FOUND and semi_colon_sign != NOT_FOUND:
            dest = command[:equal_sign]
            comp = command[equal_sign + 1:semi_colon_sign]
            jump = command[semi_colon_sign + 1:]
        elif equal_sign != NOT_FOUND:
            dest = command[:equal_sign]
            comp = command[equal_sign + 1:]
            jump = DEFAULT
        else:
            dest = DEFAULT
            comp = command[:semi_colon_sign]
            jump = command[semi_colon_sign + 1:]
        return dest, comp, jump

    def case_c_command(self, command):
        """
        this function receives a c command ain user writing and translates it to binary code
        :param command:
        :return:
        """
        dest, comp, jump = self.c_command_parser(command)
        binary_dest = BinaryTables.DTable.get(dest)
        a = OFF
        binary_comp = BinaryTables.CTable_a0.get(comp)
        if binary_comp is None:
            binary_comp = BinaryTables.CTable_a1.get(comp)
            a = ON
        binary_jump = BinaryTables.JTable.get(jump)
        if comp.find("<<") != -1 or comp.find(">>") != -1:
            prefix = "101"
        else:
            prefix = "111"
        self.binary_commands.append(prefix + a + binary_comp + binary_dest + binary_jump)
