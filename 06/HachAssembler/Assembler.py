from Parser import Parser


class Assembler:
	def __init__(self, in_path, out_path):
		self.symbol_table = {"SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4, "R1": 1, "R2": 2, "R3": 3, "R4": 4,
							 "R5": 5, "R6": 6, "R7": 7, "R8": 8, "R9": 9, "R10": 10, "R11": 11, "R12": 12, "R13": 13,
							 "R14": 14, "R15": 15, "SCREEN": 16384, "KBD": 24576}
		self.commands = Parser(in_path).get_all_commands()
		self.line_counter = 0
		self.next_var_address = 16

	def extract_lables(self):
		for command in self.commands:
			if (command.startswith("(") and command.endswith(")")):
				self.symbol_table[command[1:-1]] = (self.line_counter + 1)
			else:
				self.line_counter += 1


	