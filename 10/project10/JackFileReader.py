import re
COMMAND_MARK = "//"
DOCUMENTATION = ".*(\/\*\*[^\n]*\*\/)"
SPACE = " "
TAB = "\t"
EMPTY_STR = ""

class JackFileReader:
	def __init__(self, path):
		self._path = path
		self.__allLines = []
		self.__oneLiner = ""
		self.readFile()
		self.removeDocumentation()

	def readFile(self):
		with open(self._path, "r") as file:
			allLines = file.read().splitlines()
		for line in allLines:
			line = line.replace(SPACE, EMPTY_STR)
			line = line.replace(TAB, EMPTY_STR)
			if not (line.startswith(COMMAND_MARK)) and line != EMPTY_STR:
				## removing all comments
				in_line_command = line.find(COMMAND_MARK)
				if in_line_command >= 0:
					line = line[0:in_line_command]
				self.__allLines.append(line)
		self.__oneLiner = "".join(self.__allLines)


	def removeDocumentation(self):
		DocumentationReg = re.compile(DOCUMENTATION)
		matching = re.match(DocumentationReg, self.__oneLiner)
		while (matching):
			self.__oneLiner = self.__oneLiner.replace(matching.group(1), "")
			matching = re.match(DocumentationReg, self.__oneLiner)

	def getLines(self):
		return self.__allLines

	def geOneLiner(self):
		return self.__oneLiner
