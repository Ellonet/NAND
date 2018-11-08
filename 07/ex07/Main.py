"""drives the process"""
import sys
import os
import glob
from CodeWriter import CodeWriter

if __name__ == '__main__':
    user_input = sys.argv[1]
    if os.path.isdir(user_input):
        os.chdir(user_input)
        for file in glob.glob("*.vm"):
            code_writer = CodeWriter(os.path.abspath(file))

    else:
        code_writer = CodeWriter(os.path.abspath(user_input))
