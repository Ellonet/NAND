import re

# ________________________constants___________________________
COMMENT_MARK = "//"
QUOTE_MARK = '"'
DOCUMENTATION1 = ".*((\/\*\*)[^\n].*?(\*\/))"
DOCUMENTATION2 = ".*((\/\*)[^\n].*?(\*\/))"

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
            if line.startswith(COMMENT_MARK):
                continue
            quote = line.find(QUOTE_MARK)
            if quote >= 0:
                temp = line.split('"')
                if len(temp) < 3:
                    print(self._path)
                    print(line)
                    print(temp)
                temp[0] = " ".join(temp[0].split())
                temp[2] = " ".join(temp[2].split())
                qoute_2 = temp[2].find(COMMENT_MARK)
                if qoute_2 >= 0:
                    temp[2] = temp[2][:qoute_2]

                qoute_1 = temp[0].find(COMMENT_MARK)
                if qoute_1 >= 0:
                    line = temp[0][:qoute_1]

                else:
                    line = '"'.join(temp)

            else:
                temp = line.find(COMMENT_MARK)
                if temp >= 0:
                    line = line[:temp]
                line = " ".join(line.split())

            semi = line.rfind(";")
            if semi >= 0:
                ender = line.rfind("}")
                if ender > semi:
                    line = line[:ender + 1]
                else:
                    line = line[:semi + 1]

            if not (line.startswith(COMMENT_MARK)) and line != EMPTY_STR:
                self.__allLines.append(line)

        self.__oneLiner = "".join(self.__allLines)

    def remove_documentation(self):
        """
        cleans the input from comments
        :return:
        """
        documentation_reg = re.compile(DOCUMENTATION1)
        documentation_reg2 = re.compile(DOCUMENTATION2)

        matching = re.match(documentation_reg, self.__oneLiner)
        while matching:
            self.__oneLiner = self.__oneLiner.replace(matching.group(1), "")
            matching = re.match(documentation_reg, self.__oneLiner)

        matching = re.match(documentation_reg2, self.__oneLiner)
        while matching:
            self.__oneLiner = self.__oneLiner.replace(matching.group(1), "")
            matching = re.match(documentation_reg2, self.__oneLiner)

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
