from CompilationEngine import CompilationEngine
import sys
import os
import glob

if __name__ == '__main__':
    given_path = sys.argv[1]
    # in case a directory is given
    if os.path.isdir(given_path):
        os.chdir(given_path)
        for file in glob.glob("*.jack"):
            input_file = os.path.abspath(file)
            output_file = input_file.replace(".jack", ".vm")
            compilation_engine = CompilationEngine(input_file, output_file)
    else:
        # in case a single file path is given
        input_file = given_path
        output_file = input_file.replace(".jack", ".vm")
        compilation_engine = CompilationEngine(input_file, output_file)
