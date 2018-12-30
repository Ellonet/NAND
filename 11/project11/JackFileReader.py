import re

# ________________________constants___________________________
COMMENT_MARK = "//"
QUOTE_MARK = '"'
DOC_START = "/*"
DOC_END = "*/"
SPACE = " "
TAB = "\t"
NEW_LINE = "\n"


class JackFileReader:
	"""
	given a jack file path - it reads the file and generates a one liner containing the pure jack code.
	"""
	def __init__(self, path):
		self._path = path
		self.__allLines = []
		self.__oneLiner = ""
		self._read_file()

	def _read_file(self):
		"""
		The main method running this class.
		:return:
		"""
		with open(self._path, "r") as file:
			for line in file:
				self.__oneLiner += line
		self._remove_documentation()
		self._clean_spaces()

	def _remove_documentation(self):
		"""
		Removes all the possible documentations from the one liner holding the code.
		:return:
		"""
		string_flag = False
		comment_flag = False
		length = len(self.__oneLiner)
		i = 0
		while (i < length):
			curr = self.__oneLiner[i]
			if curr is QUOTE_MARK and not comment_flag: # got " out side a comment
				string_flag = not string_flag

			if not string_flag: # not in string
				if self.__oneLiner[i:].startswith(COMMENT_MARK):
					new_line = self.__oneLiner[i:].find(NEW_LINE)
					self.__oneLiner = self.__oneLiner[:i] + self.__oneLiner[i + new_line + 1:]
					length -= new_line + 1

				elif self.__oneLiner[i:].startswith(DOC_START):
					doc = self.__oneLiner[i:].find(DOC_END)
					self.__oneLiner = self.__oneLiner[:i] + SPACE + self.__oneLiner[i + doc + 2:]
					length -= doc + 2
				else:
					i += 1
			# case of string "..."
			else:
				i += 1
		self.__oneLiner = self.__oneLiner.replace(NEW_LINE, SPACE)

	def _clean_spaces(self):
		"""
		Cleans all the unnecessary white spaces and tabs.
		:return:
		"""
		split_by_quotes = self.__oneLiner.split(QUOTE_MARK)
		for i in range(len(split_by_quotes)):
			if (not i % 2):
				split_by_quotes[i] = " ".join(split_by_quotes[i].split())
		self.__oneLiner = QUOTE_MARK.join(split_by_quotes)

	def get_one_liner(self):
		"""
		getter for the big string holding the "pure" parsed code with no documentation and unnecessary spaces.
		:return: a string
		"""
		return self.__oneLiner
