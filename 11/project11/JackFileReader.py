import re

# ________________________constants___________________________
COMMENT_MARK = "//"
QUOTE_MARK = '"'
SPACE = " "
TAB = "\t"
NEW_LINE = "\n"
DOC_START = "/*"
DOC_END = "*/"


class JackFileReader:
	"""
	reads the file while ignoring spaces and comments
	"""

	def __init__(self, path):
		self._path = path
		self.__allLines = []
		self.__oneLiner = ""
		self.__final = ""
		self.read_file()
		self.remove_documentation()
		self.clean_spaces()

	def read_file(self):
		"""
		the main function of the class
		:return:
		"""
		with open(self._path, "r") as file:
			for line in file:
				self.__oneLiner += line

	def remove_documentation(self):
		string_flag = False
		comment_flag = False
		length = len(self.__oneLiner)
		i = 0
		while (i < length):
			curr = self.__oneLiner[i]
			if curr is QUOTE_MARK and not comment_flag:
				string_flag = not string_flag

			if not string_flag:
				if self.__oneLiner[i:].startswith(COMMENT_MARK):
					new_line = self.__oneLiner[i:].find("\n")
					self.__oneLiner = self.__oneLiner[:i] + self.__oneLiner[i + new_line + 1:]
					length -= new_line + 1

				elif self.__oneLiner[i:].startswith(DOC_START):
					doc = self.__oneLiner[i:].find(DOC_END)
					self.__oneLiner = self.__oneLiner[:i] + SPACE + self.__oneLiner[i + doc + 2:]
					length -= doc + 2

				else:
					i += 1
			else:
				i += 1

		self.__oneLiner = self.__oneLiner.replace(NEW_LINE, SPACE)

	def get_one_liner(self):
		"""
		getter for the big string holding all the lines one after the other
		:return:
		"""
		return self.__oneLiner

	def clean_spaces(self):
		bla = self.__oneLiner.split(QUOTE_MARK)
		for i in range(len(bla)):
			if(not i%2):
				bla[i] = " ".join(bla[i].split())
		self.__oneLiner = QUOTE_MARK.join(bla)
