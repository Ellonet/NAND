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
        """
        this function receives a path of a file and opens the file. it reads the lines and arranges them into an array.
        it ignores white spaces
        :param in_path: the path of the file
        :return: None
        """
        with open(in_path) as file:
            lines = file.read().splitlines()
            for line in lines:
                line = line.strip()
                if not line.startswith(COMMENT) and line != EMPTY_STR:
                    comment_index = line.find(COMMENT)
                    if comment_index != -1:
                        line = line[:comment_index]
                        line = line.strip()
                    self.__commands.append(line)

    def get_commands(self):
        """
        returns the commands list
        :return: the commands list
        """
        return self.__commands
