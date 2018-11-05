"""imports"""
import glob
import os
import sys
from Assembler import Assembler

"""constants"""
ASM_PREFIX = "*.asm"

"""this is the main function that runs the program"""
if __name__ == '__main__':
    program_input = sys.argv[1]
    if os.path.isdir(program_input):
        os.chdir(program_input)
        for file in glob.glob(ASM_PREFIX):
            path = os.getcwd() + "\\" + file
            asm_compiler = Assembler(path)

    else:
        asm_compiler = Assembler(program_input)
