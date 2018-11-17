"""drives the process"""
import sys
import os
import glob
from CodeWriter import CodeWriter

if __name__ == '__main__':
	user_input = sys.argv[1]
	counter = 0
	if os.path.isdir(user_input):
		os.chdir(user_input)
		final_file = []
		for file in glob.glob("*.vm"):
			code_writer = CodeWriter(os.path.abspath(file), False, counter)
			final_file.extend(code_writer.get_all_commands())
			counter = code_writer.label_counter
		# print(os.path.basename(user_input))
		with open(os.path.basename(user_input) + ".asm", "w") as file:
			# file.writelines(final_file)
			for asm in final_file:
				file.writelines(asm + "\n")
		file.close()

	else:
		code_writer = CodeWriter(os.path.abspath(user_input), True, counter)
