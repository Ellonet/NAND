from CompilationEngine import CompilationEngine
import sys

if __name__ == '__main__':
    input_file = sys.argv[1]
    # todo make xml
    output_file = input_file.replace(".jack", ".txt")
    compilation_engine = CompilationEngine(input_file, output_file)
