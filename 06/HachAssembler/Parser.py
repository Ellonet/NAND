"""
this class receives a path and reads its lines one by one. it ignores spaces and comments
"""

"""magic numbers"""
COMMAND_MARK = "//"
SPACE = " "
TAB = "\t"
EMPTY_STR = ""
READ_ONLY = "r"


class Parser:
    """
    the init function of the class. saves the path, builds an empty list for the commands and starts reading the file
    """

    def __init__(self, path):
        self.path = path
        self.all_commands = []
        self._read_commands()

    def _read_commands(self):
        """
        this function reads the lines of the file given in the path and saves the wanted info in the commands list
        :return: no return value
        """
        with open(self.path, READ_ONLY) as file:
            all_lines = file.read().splitlines()
        for line in all_lines:
            line = line.replace(SPACE, EMPTY_STR)
            line = line.replace(TAB, EMPTY_STR)
            if not (line.startswith(COMMAND_MARK)) and line != EMPTY_STR:
                in_line_command = line.find(COMMAND_MARK)
                if in_line_command >= 0:
                    line = line[0:in_line_command]
                self.all_commands.append(line)

    def get_all_commands(self):
        """
        this function returns the list of the commands it reads from the file
        :return: the commands list
        """
        return self.all_commands
