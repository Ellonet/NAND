import sys, os, glob
from Assembler import Assembler

if __name__ == '__main__':
	progrm_input = sys.argv[1]
	if (os.path.isdir(progrm_input)):
		os.chdir(progrm_input)
		for file in glob.glob("*.asm"):
			bla = Assembler(file, "output")
	else:
		bla = Assembler(progrm_input, "output")
		bla.extract_labels()
		bla.read_commands()
