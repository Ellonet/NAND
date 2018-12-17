class VMWriter:
	def __init__(self, output_path):
		self.out_file = output_path
		self.open_file()

	def open_file(self):
		"""
		Opens the file in which the VM code is written.
		:return:
		"""
		return

	def writePush(self, segment, index):
		"""
		Writes a VM push command
		:param Segment: CONST, ARG, LOCAL, STATIC, THIS, THAT, POINTER, TEMP
		:param index:
		:return:
		"""
		return

	def writePop(self, Segment, index):
		"""
		Writes a VM pop command
		:param Segment: CONST, ARG, LOCAL, STATIC, THIS, THAT, POINTER, TEMP
		:param index:
		:return:
		"""
		return

	def WriteArithmetic(self, command):
		"""
		Writes a VM arithmetic command
		:param command: ADD, SUB, NEG, EQ, GT, LT, AND, OR, NOT
		:return:
		"""

	def WriteLabel(self, label):
		"""
		Writes a VM label command
		:param label:
		:return:
		"""
		return


	def WriteGoto(self, label):
		"""
		Writes a VM label command
		:param label:
		:return:
		"""
		return

	def WriteIf(self, label):
		"""
		Writes a VM If-goto command
		:param label:
		:return:
		"""
		return

	def writeCall(self, name, nArgs):
		"""
		Writes a VM call command
		:param name:
		:param nArgs:
		:return:
		"""
		return

	def writeFunction(self, name, nLocals):
		"""
		Writes a VM function command
		:param name:
		:param nLocals:
		:return:
		"""
		return

	def writeReturn(self):
		"""
		Writes a VM return command
		:return:
		"""

	def close(self):
		"""
		Closes the output file
		:return:
		"""
		return
