# operators = {"ADD": "add\n", "SUB": "sub\n","NEG":, "EQ":, "GT":, "LT":, "AND":, "OR":, "NOT":}
import Syntax


class VMWriter:
	def __init__(self, output_path):
		"""
		notice! the user is responsible to close the file using close_file method when he finishes writing to it.
		"""
		self.out_file = output_path
		self.VM_file = self.open_file()

	def open_file(self):
		"""
		Opens the file in which the VM code is written.
		:return:
		"""
		return open(self.out_file, "w")

	def write_push(self, segment, index):
		"""
		Writes a VM push command
		:param segment: CONST, ARG, LOCAL, STATIC, THIS, THAT, POINTER, TEMP
		:param index:
		:return:
		"""
		self.VM_file.write("push" + " " + segment + " " + str(index) + "\n")
		return

	def write_pop(self, segment, index):
		"""
		Writes a VM pop command
		:param segment: CONST, ARG, LOCAL, STATIC, THIS, THAT, POINTER, TEMP
		:param index:
		:return:
		"""
		self.VM_file.write("pop" + " " + segment + " " + str(index) + "\n")
		return

	def write_arithmetic(self, command):
		"""
		Writes a VM arithmetic command
		:param command: ADD, SUB, NEG, EQ, GT, LT, AND, OR, NOT
		:return:
		"""
		self.VM_file.write(Syntax.op_name[command] + "\n")

	def write_label(self, label):
		"""
		Writes a VM label command
		:param label:
		:return:
		"""
		self.VM_file.write("label" + " " + label + "\n")

	def write_goto(self, label):
		"""
		Writes a VM label command
		:param label:
		:return:
		"""
		self.VM_file.write("goto" + " " + label + "\n")

	def write_if(self, label):
		"""
		Writes a VM If-goto command
		:param label:
		:return:
		"""
		self.VM_file.write("if-goto" + " " + label + "\n")

	def write_call(self, name, nArgs):
		"""
		Writes a VM call command
		:param name:
		:param nArgs:
		:return:
		"""
		self.VM_file.write("call" + " " + name + " " + str(nArgs) + "\n")
		return

	def write_function(self, name, nLocals):
		"""
		Writes a VM function command
		:param name:
		:param nLocals:
		:return:
		"""
		self.VM_file.write("function" + " " + name + " " + str(nLocals) + "\n")

	def write_return(self):
		"""
		Writes a VM return command
		:return:
		"""
		self.VM_file.write("return" + "\n")

	def close(self):
		"""
		Closes the output file
		:return:
		"""
		self.VM_file.close()
		return
