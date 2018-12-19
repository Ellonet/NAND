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
NEG = "neg"
NOT = "~"


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
        self.label_count = 0
        self.file_reader = JackFileReader(input_file)
        self.jack_tokens = JackTokenizer(self.file_reader.get_one_liner())
        self.curr_token = self.jack_tokens.advance()
        self.to_output_file = []
        self.symbol_table = SymbolTable()
        self.vm_writer = VMWriter(output_file)
        self.depth = 0
        self.class_name = None
        self.compile_class()
        print(self.symbol_table.class_symbol_table)
        print(self.symbol_table.subroutine_symbol_table)
        self.vm_writer.close()

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
        self.symbol_table.start_subroutine()
        self.symbol_table.define("this", self.class_name, ARG)

        # constructor \ function \ method
        subroutine_type = self.next_token()
        # advance the return type
        self.next_token()
        # subroutine name
        self.next_token()
        # advance the left brackets
        self.next_token()

        if subroutine_type == "constructor":
            field_vars_num = self.get_num_of_field_vars()
            self.vm_writer.write_push("constant", field_vars_num)
            self.vm_writer.write_call("Memory.alloc", 1)
            self.vm_writer.write_pop("pointer", 0)

        elif subroutine_type == "method":
            self.vm_writer.write_push("argument", 0)
            self.vm_writer.write_pop("pointer", 0)

        self.compile_parameters_list()
        # advance the right brackets
        self.next_token()
        self.compile_subroutine_body()

    def get_num_of_field_vars(self):
        field_vars_num = 0
        for var in self.symbol_table.class_symbol_table.values():
            if var[1] == "field":
                field_vars_num += 1
        return field_vars_num

    def compile_parameters_list(self):
        """
        Compiles a (possibly empty) parameter list, not including the enclosing ().
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

    def compile_subroutine_body(self):
        """
        compiles the subroutine body
        :return:
        """
        # pass the left curly brackets
        self.next_token()
        while self.curr_token.split()[1] == "var":
            self.compile_var_dec()
        self.compile_statements()
        # pass the right curly brackets
        self.next_token()

    def compile_var_dec(self):
        """
        Compiles a var declaration.
        :return:
        """
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
        Compiles a sequence of statements, not including the enclosing {}.
        :return:
        """
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

    def compile_let(self):
        """
        Compiles a let statement.
        :return:
        """
        # advances passed let
        self.next_token()
        # var name
        var_name = self.next_token()
        var_kind = self.symbol_table.kind_of(var_name)
        if var_kind == "field":
            var_kind = "this"
        var_index = self.symbol_table.index_of(var_name)

        # for varName[] case
        list_flag = False
        if self.curr_token.split()[1] == LEFT_SQUARE_BRACKETS:
            list_flag = True
            # advance brackets
            self.next_token()
            self.vm_writer.write_push(var_kind, var_index)
            self.compile_expression()
            self.vm_writer.write_arithmetic("add")
            # advance brackets
            self.next_token()

        # advance equal sign
        self.next_token()
        self.compile_expression()
        if list_flag:
            # the value of expression 2
            self.vm_writer.write_pop("temp", 0)
            self.vm_writer.write_pop("pointer", 1)
            self.vm_writer.write_push("temp", 0)
            self.vm_writer.write_pop("that", 0)
        else:
            self.vm_writer.write_pop(var_kind, var_index)

        # advance semi colon
        self.next_token()

    def compile_if(self):
        """
        Compiles a if statement.
        :return:
        """
        # advance the if
        self.next_token()
        # advance the left brackets
        self.next_token()
        self.compile_expression()
        self.vm_writer.write_arithmetic(NEG)
        label_1 = self.next_label()
        self.vm_writer.write_if(label_1)
        # advance the right brackets
        self.next_token()

        # advance the left curly brackets
        self.next_token()

        self.compile_statements()

        # advance the right curly brackets
        self.next_token()

        if self.curr_token.split()[1] == "else":
            # advance the else
            self.next_token()
            label_2 = self.next_label()
            self.vm_writer.write_goto(label_2)
            self.vm_writer.write_label(label_1)
            # advance the left curly brackets
            self.next_token()
            self.compile_statements()
            self.vm_writer.write_label(label_2)
            # advance the right curly brackets
            self.next_token()

    def compile_while(self):
        """
        Compiles a while statement.
        :return:
        """
        # advance the while
        self.next_token()
        # advance the left brackets
        self.next_token()
        label_1 = self.next_label()
        self.vm_writer.write_label(label_1)
        self.compile_expression()
        self.vm_writer.write_arithmetic(NEG)
        label_2 = self.next_label()
        self.vm_writer.write_if(label_2)
        # advance the right brackets
        self.next_token()
        # advance the left curly brackets
        self.next_token()
        self.compile_statements()
        self.vm_writer.write_goto(label_1)
        self.vm_writer.write_label(label_2)
        # advance the right curly brackets
        self.next_token()

    def compile_do(self):
        """
        Compiles a do statement.
        :return:
        """
        # advance the do
        self.next_token()

        # subroutine call:
        subroutine_name = self.next_token()
        if self.curr_token.split()[1] == ".":
            # advance the dot
            self.next_token()
            subroutine_name = subroutine_name + "." + self.next_token()
        # advance the brackets
        self.next_token()
        num_of_arguments = self.compile_expression_list()
        # advance the brackets
        self.next_token()
        # advance the semi colon
        self.next_token()
        self.vm_writer.write_call(subroutine_name, num_of_arguments)
        self.vm_writer.write_pop("temp", 0)

    def compile_return(self):
        """
        Compiles a return statement.
        :return:
        """
        # advance the return
        self.next_token()

        if self.curr_token.split()[1] != SEMI_COLON:
            if self.curr_token.split()[1] == "this":
                self.vm_writer.write_push("pointer", 0)
                self.next_token()
            else:
                self.compile_expression()
        else:
            # default
            self.vm_writer.write_push("constant", 0)
        self.vm_writer.write_return()
        # advance the semi colon
        self.next_token()

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
		self.vm_writer.write_arithmetic(op)

	def compile_term(self):
		"""
		Compiles a term. This routine is faced with a slight difficulty when trying to decide between
		some of the alternative parsing rules. Specifically, if the current token is an
		identifier, the routine must distinguish between a variable, an array entry, and a
		subroutine call. A single look-ahead token, which may be one of [, (, or .  suffices to distinguish
		between the three possibilities. Any other token is not part of this term and should not be advanced over.
		:return:
		"""
		all = self.curr_token.split()
		header = all[0]
		val = all[1]
		# handle case of stringConstant, integerConstant, keyword
		if header == "<integerConstant>":
			self.vm_writer.write_push("constant", val)
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
			self.next_token()
			self.compile_term()
			if val == "-":
				self.vm_writer.write_arithmetic(NEG)
			else:
				self.vm_writer.write_arithmetic(NOT)
		elif header == IDENTIFIER:
			next_token = self.jack_tokens.peek().split()[1]
			if next_token == LEFT_SQUARE_BRACKETS:
				print("[", self.curr_token)
				print("[", self.curr_token)
				self.__eat(val)
				self.__eat(LEFT_SQUARE_BRACKETS)
				self.compile_expression()
				self.__eat(RIGHT_SQUARE_BRACKETS)
			# subroutine call: subroutineName(expressionList)
			elif next_token == LEFT_BRACKETS:
				print("(", self.curr_token)
				print("(", self.curr_token)
				self.__eat(val)
				self.__eat(LEFT_BRACKETS)
				self.compile_expression_list()
				self.__eat(RIGHT_BRACKETS)
			# subroutine call: (className|varName).subroutineName(expressionList)
			elif next_token == ".":
				print(".", self.curr_token)
				print(".", self.curr_token)
				self.__eat(val)
				self.__eat(".")
				self.__eat_by_type(IDENTIFIER)
				self.__eat(LEFT_BRACKETS)
				self.compile_expression_list()
				self.__eat(RIGHT_BRACKETS)
			else:
				self.vm_writer.write_push(self.symbol_table.kind_of(val), self.symbol_table.index_of(val))
				self.next_token()
		return

	def compile_expression_list(self):
		"""
		Compiles a (possibly empty) comma separated list of expressions.
		:return:
		"""
		num_of_arguments = 0
		if self.curr_token.split()[1] != RIGHT_BRACKETS:
			num_of_arguments += 1
			self.compile_expression()
			while self.curr_token.split()[1] == COMMA:
				num_of_arguments += 1
				# advance comma
				self.next_token()
				self.compile_expression()
		return num_of_arguments

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

    def next_label(self):
        count = self.label_count
        self.label_count += 1
        return "LABEL" + str(count)
