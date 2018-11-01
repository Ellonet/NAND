class Parser:
	def __init__(self, path):
		self.path = path
		self.COMMAND_MARK = "//"
		self.all_commands = []
		self._read_commands()


	def _read_commands(self):
		with open(self.path, "r") as file:
			all_lines = file.read().splitlines()
		for line in all_lines:
			line = line.replace(" ", "")
			line = line.replace("\t", "")
			if (not (line.startswith(self.COMMAND_MARK)) and line != ""):
				in_line_command = line.find(self.COMMAND_MARK)
				if (in_line_command >= 0):
					line = line[0:in_line_command]
				self.all_commands.append(line)
		return

	def get_all_commands(self):
		return self.all_commands