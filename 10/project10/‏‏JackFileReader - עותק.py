import re

# ________________________constants___________________________
COMMAND_MARK = "//"
QUOTE_MARK = '"'
DOCUMENTATION = ".*(\/\*\*[^\n]*\*\/)"
SPACE = " "
TAB = "\t"
EMPTY_STR = ""


class JackFileReader:
    """
    reads the file while ignoring spaces and comments
    """

    def __init__(self, path):
        self._path = path
        self.__allLines = []
        self.__oneLiner = ""
        self.read_file()
        self.remove_documentation()

    def read_file(self):
        """
        the main function of the class
        :return:
        """
        with open(self._path, "r") as file:
            all_lines = file.read().splitlines()
        for line in all_lines:
            quote = line.find(QUOTE_MARK)
            if quote >= 0:
                temp = line.split('"')
                temp[0] = " ".join(temp[0].split())
                # temp[0] = temp[0].replace(TAB, EMPTY_STR)
                temp[2] = " ".join(temp[2].split())
                # temp[2] = temp[2].replace(TAB, EMPTY_STR)
                line = '"'.join(temp)
            else:
                # line = line.replace(SPACE, EMPTY_STR)
                # line = line.replace(TAB, EMPTY_STR)
                line = " ".join(line.split())
            if not (line.startswith(COMMAND_MARK)) and line != EMPTY_STR:
                in_line_command = line.find(COMMAND_MARK)
                if in_line_command >= 0:
                    line = line[0:in_line_command]
                self.__allLines.append(line)
        self.__oneLiner = "".join(self.__allLines)

    def remove_documentation(self):
        """
        cleans the input from comments
        :return:
        """
        documentation_reg = re.compile(DOCUMENTATION)
        matching = re.match(documentation_reg, self.__oneLiner)
        while matching:
            self.__oneLiner = self.__oneLiner.replace(matching.group(1), "")
            matching = re.match(documentation_reg, self.__oneLiner)

    def get_lines(self):
        """
        getter for the parsed lines of the file
        :return:
        """
        return self.__allLines

    def get_one_liner(self):
        """
        getter for the big string holding all the lines one after the other
        :return:
        """
        return self.__oneLiner
