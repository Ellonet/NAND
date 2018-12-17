from JackTokenizer import JackTokenizer
from JackFileReader import JackFileReader
import Syntax
from SymbolTable import SymbolTable
from VMWriter import VMWriter

# ________________________constants___________________________
VAR_DECS = ["static", "field"]
SUB_ROUTINES = ["constructor", "function", "method"]
IDENTIFIER = "<identifier>"
END_TERMS = ["<stringConstant>", "<integerConstant>", "<keyword>"]
LEFT_BRACKETS = "("
RIGHT_BRACKETS = ")"
LEFT_CURLY_BRACKETS = "{"
RIGHT_CURLY_BRACKETS = "}"
LEFT_SQUARE_BRACKETS = "["
RIGHT_SQUARE_BRACKETS = "]"
EQUAL_SIGN = "="
INDENTATION = "  "
COMMA = ","
SEMI_COLON = ";"
ONARY_OP = ["-", "~"]
ARG = "argument"
LCL = "local"


class CompilationEngine:
	"""
	generates the compilers output
	"""

	def __init__(self, input_file, output_file):
		"""
		the constructor of the class
		:param input_file: the jack file that the user want to compile
		:param output_file: the path for the output xml file
		"""
		self.file_reader = JackFileReader(input_file)
		self.jack_tokens = JackTokenizer(self.file_reader.get_one_liner())
		self.curr_token = self.jack_tokens.advance()
		self.to_output_file = []
		self.symbol_table = SymbolTable()
		# self.vm_writer = VMWriter(output_file)
		self.depth = 0
		self.class_name = None
		self.compile_class()
		# print(self.symbol_table.class_symbol_table)
		# print(self.symbol_table.subroutine_symbol_table)
		# self.vm_writer.close()

	def compile_class(self):
		"""
		Compiles a complete class.
		"""
		# advancing beyond 'class'
		self.next_token()
		# assign class name
		self.class_name = self.next_token()
		# advancing beyond '{'
		self.next_token()
		# zero or more times
		while self.curr_token.split()[1] in VAR_DECS:
			self.compile_class_var_dec()
		# zero or more times
		while self.curr_token.split()[1] in SUB_ROUTINES:
			self.compile_subroutine_dec()
		# advancing beyond '}'
		self.next_token()
		return

	def compile_class_var_dec(self):
		"""
		Compiles a static declaration or a field declaration.
		:return:
		"""
		# compiles a static variable declaration, or a field declaration
		# ('static' | 'field' ) type varName (',' varName)* ';'
		var_kind = self.next_token()
		var_type = self.next_token()
		var_name = self.next_token()
		self.symbol_table.define(var_name, var_type, var_kind)
		while self.curr_token.split()[1] == COMMA:
			# advancing the COMMA
			self.next_token()
			var_name = self.next_token()
			self.symbol_table.define(var_name, var_type, var_kind)
		# advance beyond ;
		self.next_token()
		return

	def compile_subroutine_dec(self):
		"""
		Compiles a complete method, function, or constructor.
		:return:
		"""
		# ('constructor' | 'function' | 'method') ('void' | type) subroutineName '(' parameterList ')' subroutineBody
		self.symbol_table.start_subroutine()
		self.symbol_table.define("this", self.class_name, ARG)

		# constructor \ function \ method
		subroutine_type = self.next_token()
		# take the return type
		return_type = self.next_token()
		# subroutine name
		subroutine_name = self.next_token()

		self.__eat(LEFT_BRACKETS)
		self.compile_parameters_list()
		self.__eat(RIGHT_BRACKETS)
		self.compile_subroutine_body()
		self.depth -= 1
		self.to_output_file.append(INDENTATION * self.depth + "</subroutineDec>")
		return

	def compile_parameters_list(self):
		"""
		Compiles a (possibly empty) parameter list, not including the enclosing “()”.
		:return:
		"""
		# ( (type varName) (',' type varName)*)?
		if self.curr_token.split()[1] != RIGHT_BRACKETS:
			# type
			par_type = self.next_token()
			par_name = self.next_token()
			self.symbol_table.define(par_name, par_type, ARG)
			while self.curr_token.split()[1] == COMMA:
				# advance pass the comma:
				self.next_token()
				par_type = self.next_token()
				par_name = self.next_token()
				self.symbol_table.define(par_name, par_type, ARG)
		return

	def compile_subroutine_body(self):
		"""
		compiles the subroutine body
		:return:
		"""
		# '{' varDec* statements '}'
		self.to_output_file.append(INDENTATION * self.depth + "<subroutineBody>")
		self.depth += 1
		self.__eat(LEFT_CURLY_BRACKETS)
		while self.curr_token.split()[1] == "var":
			self.compile_var_dec()
		self.compile_statements()
		self.__eat(RIGHT_CURLY_BRACKETS)
		self.depth -= 1
		self.to_output_file.append(INDENTATION * self.depth + "</subroutineBody>")
		return

	def compile_var_dec(self):
		"""
		Compiles a var declaration.
		:return:
		"""
		# 'var' type varName (',' varName)* ';'
		# advance passed "var"
		self.next_token()
		var_type = self.next_token()
		var_name = self.next_token()
		self.symbol_table.define(var_name, var_type, LCL)
		while self.curr_token.split()[1] == COMMA:
			# advance passed COMMA
			self.next_token()
			var_name = self.next_token()
			self.symbol_table.define(var_name, var_type, LCL)
		# advance passed ;
		self.next_token()
		return

	def compile_statements(self):
		"""
		Compiles a sequence of statements, not including the enclosing “{}”.
		:return:
		"""
		self.to_output_file.append(INDENTATION * self.depth + "<statements>")
		self.depth += 1
		statements = True
		while statements:
			statement_type = self.curr_token.split()[1]
			if statement_type == "let":
				self.compile_let()
			elif statement_type == "if":
				self.compile_if()
			elif statement_type == "while":
				self.compile_while()
			elif statement_type == "do":
				self.compile_do()
			elif statement_type == "return":
				self.compile_return()
			else:
				statements = False
		self.depth -= 1
		self.to_output_file.append(INDENTATION * self.depth + "</statements>")
		return

	def compile_let(self):
		"""
		Compiles a let statement.
		:return:
		"""
		# advances passed let
		self.next_token()
		# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		# var name
		var_name = self.next_token()
		var_type = self.symbol_table.type_of(var_name)
		var_kind = self.symbol_table.kind_of(var_name)
		if var_kind is "field":
			var_kind = "this"
		var_index = self.symbol_table.index_of(var_name)
		# self.vm_writer.write_push(var_kind, var_index)
		if self.curr_token.split()[1] == LEFT_SQUARE_BRACKETS:
			self.__eat(LEFT_SQUARE_BRACKETS)
			self.compile_expression()
			self.__eat(RIGHT_SQUARE_BRACKETS)
		self.__eat(EQUAL_SIGN)
		self.compile_expression()
		self.__eat(SEMI_COLON)
		self.depth -= 1
		self.to_output_file.append(INDENTATION * self.depth + "</letStatement>")
		return

	def compile_if(self):
		"""
		Compiles a if statement.
		:return:
		"""
		self.to_output_file.append(INDENTATION * self.depth + "<ifStatement>")
		self.depth += 1
		self.__eat("if")
		self.__eat(LEFT_BRACKETS)
		self.compile_expression()
		self.__eat(RIGHT_BRACKETS)
		self.__eat(LEFT_CURLY_BRACKETS)
		self.compile_statements()
		self.__eat(RIGHT_CURLY_BRACKETS)
		if self.curr_token.split()[1] == "else":
			self.__eat("else")
			self.__eat(LEFT_CURLY_BRACKETS)
			self.compile_statements()
			self.__eat(RIGHT_CURLY_BRACKETS)
		self.depth -= 1
		self.to_output_file.append(INDENTATION * self.depth + "</ifStatement>")
		return

	def compile_while(self):
		"""
		Compiles a while statement.
		:return:
		"""
		self.to_output_file.append(INDENTATION * self.depth + "<whileStatement>")
		self.depth += 1
		self.__eat('while')
		self.__eat('(')
		self.compile_expression()
		self.__eat(')')
		self.__eat('{')
		self.compile_statements()
		self.__eat('}')
		self.depth -= 1
		self.to_output_file.append(INDENTATION * self.depth + "</whileStatement>")
		return

	def compile_do(self):
		"""
		Compiles a do statement.
		:return:
		"""
		# 'do' subroutineCall ';'
		self.to_output_file.append(INDENTATION * self.depth + "<doStatement>")
		self.depth += 1
		self.__eat("do")

		# subroutine call:
		# subroutine name
		self.__eat_by_type(IDENTIFIER)
		if self.curr_token.split()[1] == ".":
			self.__eat(".")
			self.__eat_by_type(IDENTIFIER)
		self.__eat(LEFT_BRACKETS)
		self.compile_expression_list()
		self.__eat(RIGHT_BRACKETS)

		self.__eat(SEMI_COLON)
		self.depth -= 1
		self.to_output_file.append(INDENTATION * self.depth + "</doStatement>")
		return

	def compile_return(self):
		"""
		Compiles a return statement.
		:return:
		"""
		# 'return' expression? ';'
		self.to_output_file.append(INDENTATION * self.depth + "<returnStatement>")
		self.depth += 1
		self.__eat("return")
		if self.curr_token.split()[1] != SEMI_COLON:
			self.compile_expression()
		self.__eat(SEMI_COLON)
		self.depth -= 1
		self.to_output_file.append(INDENTATION * self.depth + "</returnStatement>")
		return

	def compile_expression(self):
		"""
		Compiles a do statement.
		:return:
		"""
		self.compile_term()
		while self.curr_token.split()[1] in Syntax.operators:
			op = self.curr_token.split()[1]
			self.next_token()
			self.compile_term()
			self.compile_op(op)
		return

	def compile_op(self, op):
			print(Syntax.op_name[op])

	def compile_term(self):
		"""
		Compiles a term. This routine is faced with a
		slight difficulty when trying to decide
		between some of the alternative parsing rules.
		Specifically, if the current token is an
		identifier, the routine must distinguish
		between a variable, an array entry, and a
		subroutine call. A single look-ahead token,
		which may be one of “[“, “(“, or “.”
		suffices to distinguish between the three
		possibilities. Any other token is not part of
		this term and should not be advanced over.
			:return:
		"""
		all = self.curr_token.split()
		header = all[0]
		val = all[1]
		# handle case of stringConstant, integerConstant, keyword
		if header == "<integerConstant>":
			print("push", val)
			self.next_token()
		# handle in case of (expression)
		elif val == LEFT_BRACKETS:
			# advance passed "("
			self.next_token()
			self.compile_expression()
			# advance passed ")"
			self.next_token()
		# case of  onary Op
		elif val in ONARY_OP:
			print(val)
			self.next_token()
			self.compile_term()
		elif header == IDENTIFIER:
			next_token = self.jack_tokens.peek().split()[1]
			if next_token == LEFT_SQUARE_BRACKETS:
				self.__eat(val)
				self.__eat(LEFT_SQUARE_BRACKETS)
				self.compile_expression()
				self.__eat(RIGHT_SQUARE_BRACKETS)
			# subroutine call: subroutineName(expressionList)
			elif next_token == LEFT_BRACKETS:
				self.__eat(val)
				self.__eat(LEFT_BRACKETS)
				self.compile_expression_list()
				self.__eat(RIGHT_BRACKETS)
			# subroutine call: (className|varName).subroutineName(expressionList)
			elif next_token == ".":
				self.__eat(val)
				self.__eat(".")
				self.__eat_by_type(IDENTIFIER)
				self.__eat(LEFT_BRACKETS)
				self.compile_expression_list()
				self.__eat(RIGHT_BRACKETS)
			else:
				print("push", val)
				self.next_token()
		return

	def compile_expression_list(self):
		"""
		Compiles a (possibly empty) comma separated list of expressions.
		:return:
		"""
		self.to_output_file.append(INDENTATION * self.depth + "<expressionList>")
		self.depth += 1
		if self.curr_token.split()[1] != RIGHT_BRACKETS:
			self.compile_expression()
			while self.curr_token.split()[1] == COMMA:
				self.__eat(COMMA)
				self.compile_expression()
		self.depth -= 1
		self.to_output_file.append(INDENTATION * self.depth + "</expressionList>")
		return

	def __eat(self, param):
		"""
		checks that the right token is the next one, adds it to the output file, and advances the token pointer
		:param param: the param to compare with the next token
		:return: throws exception for wrong input
		"""
		token = self.curr_token.split()
		if token[1] != param:
			raise Exception
		else:
			self.to_output_file.append(INDENTATION * self.depth + self.curr_token)
			self.curr_token = self.jack_tokens.advance()
			if not self.curr_token:
				return

	def next_token(self):
		to_return = self.curr_token.split()[1]
		self.curr_token = self.jack_tokens.advance()
		return to_return

	def __eat_by_type(self, param):
		"""
		checks that the right token is the next one- by type, adds it to the output file,
		and advances the token pointer
		:param param: the param to compare with the next token
		:return: throws exception for wrong input
		"""
		type_ = self.curr_token.split()[0]
		if type_ != param:
			raise Exception
		else:
			self.to_output_file.append(INDENTATION * self.depth + self.curr_token)
			self.curr_token = self.jack_tokens.advance()

			# def export_file(self, output_file):
			#     """
			#     exports the file with the given path
			#     :param output_file: the path
			#     :return:
			#     """
			#     with open(output_file, "w") as file:
			#         for line in self.to_output_file:
			#             file.write(line + "\n")
			#     return

