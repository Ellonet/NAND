"""parses each VM command into its lexical elements"""

SPACE = " "
TAB = "\t"
EMPTY_STR = ""
COMMENT = "//"


class Parser:
    def __init__(self, in_path):
        self.__commands = []
        self.read_file(in_path)

    def read_file(self, in_path):
        with open(in_path) as file:
            lines = file.read().splitlines()
            for line in lines:
                line.replace(SPACE, EMPTY_STR)
                line.replace(TAB, EMPTY_STR)
                if not line.startswith(COMMENT) and line != EMPTY_STR:
                    self.__commands.append(line)

    def get_commands(self):
        return self.__commands
