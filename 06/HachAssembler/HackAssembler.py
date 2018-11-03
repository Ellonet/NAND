"""imports"""
import glob
import os
import sys
from Assembler import Assembler

"""this is the main function that runs the program"""
if __name__ == '__main__':
    program_input = sys.argv[1]
    if (os.path.isdir(program_input)):
        os.chdir(program_input)
        for file in glob.glob("*.asm"):
            bla = Assembler(file, "output")
    else:
        bla = Assembler(program_input, "output")
        bla.extract_labels()
        bla.read_commands()
