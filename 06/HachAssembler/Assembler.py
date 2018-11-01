from Parser import Parser
from BinaryTables import BinaryTables


class Assembler:
	def __init__(self, in_path, out_path):
		self.symbol_table = {"SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4, "R1": 1, "R2": 2, "R3": 3, "R4": 4,
							 "R5": 5, "R6": 6, "R7": 7, "R8": 8, "R9": 9, "R10": 10, "R11": 11, "R12": 12, "R13": 13,
							 "R14": 14, "R15": 15, "SCREEN": 16384, "KBD": 24576}
		self.commands = Parser(in_path).get_all_commands()
		self.next_var_address = 16
		self.binary_commands = []
		self.binary_Table = BinaryTables

	def extract_labels(self):
		line_counter = 0
		for command in self.commands:
			if command.startswith("(") and command.endswith(")"):
				self.symbol_table[command[1:-1]] = (line_counter + 1)
			else:
				line_counter += 1

	def read_commands(self):

		for command in self.commands:
			if command.startswith("@"):
				self.case_A_command(command[1:])
			else:
				self.case_C_command(command)
		for line in self.binary_commands:
			print(line)

	def case_A_command(self, command):
		if command.isdigit():
			# add the line in binary writing
			binary = '{0:015b}'.format(int(command))
			self.binary_commands.append("0" + binary)
		else:
			address = self.symbol_table.get(command)
			if address is None:  # the variable is not in the table
				address = self.next_var_address  # get the next available address
				self.next_var_address += 1
				self.symbol_table[command] = address  # add the variable to the dictionary
			address_binary = '{0:015b}'.format(int(address))
			self.binary_commands.append("0" + address_binary)

	def case_C_command(self, command):
		# bla = self.binary_Table.DTable
		return
