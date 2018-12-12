from JackTokenizer import JackTokenizer
from JackFileReader import JackFileReader
import Syntax

VAR_DECS = ["static", "field"]
SUB_ROUTINES = ["constructor", "function", "method"]
IDENTIFIER = "<identifier>"


# generates the compilers output


class CompilationEngine:
    def __init__(self, input_file, output_file):
        self.file_reader = JackFileReader(input_file)
        self.jack_tokens = JackTokenizer(self.file_reader.get_one_liner())
        self.curr_token = self.jack_tokens.advance()
        self.to_output_file = []
        self.depth = 0
        self.compile_class()

        # self.output_file = self.create_file(output_file)

    def compile_class(self):
        self.to_output_file.append("<class>")
        self.depth += 1
        self.__eat('class')
        # class name
        self.__eat_by_type(IDENTIFIER)
        self.__eat("{")
        # zero or more times
        while self.curr_token.split()[1] in VAR_DECS:
            self.compile_class_var_dec()
        # zero or more times
        while self.curr_token.split()[1] in SUB_ROUTINES:
            self.compile_subroutine_dec()
        self.__eat("}")
        self.depth -= 1
        self.to_output_file.append("</class>")
        return

    def compile_class_var_dec(self):
        # compiles a static variable declaration, or a field declaration
        # ('static' | 'field' ) type varName (',' varName)* ';'
        self.to_output_file.append("\t" * self.depth + "<classVarDec>")
        self.depth += 1
        self.__eat(self.curr_token.split()[1])
        # take the type as is
        self.__eat(self.curr_token.split()[1])
        self.__eat_by_type(IDENTIFIER)
        while self.curr_token.split()[1] == ",":
            self.__eat(",")
            self.__eat_by_type(IDENTIFIER)
        self.__eat(";")
        self.depth -= 1
        self.to_output_file.append("\t" * self.depth + "</classVarDec>")
        return

    def compile_subroutine_dec(self):
        # ('constructor' | 'function' | 'method') ('void' | type) subroutineName '(' parameterList ')' subroutineBody
        self.to_output_file.append("\t" * self.depth + "<subroutine>")
        self.depth += 1
        self.__eat(self.curr_token.split()[1])
        # take the return type as is (or void)
        self.__eat(self.curr_token.split()[1])
        # subroutine name
        self.__eat_by_type(IDENTIFIER)
        self.__eat("(")
        self.compile_parameters_list()
        self.__eat(")")
        self.compile_subroutine_body()
        self.depth -= 1
        self.to_output_file.append("\t" * self.depth + "</subroutine>")
        return

    def compile_parameters_list(self):
        # ( (type varName) (',' type varName)*)?
        self.to_output_file.append("\t" * self.depth + "<parameterList>")
        self.depth += 1
        if self.curr_token.split()[1] != ")":
            # type
            self.__eat(self.curr_token.split()[1])
            # var mane
            self.__eat_by_type(IDENTIFIER)
            while self.curr_token.split()[1] == ",":
                self.__eat(",")
                # type
                self.__eat(self.curr_token.split()[1])
                # var mane
                self.__eat_by_type(IDENTIFIER)
        self.depth -= 1
        self.to_output_file.append("\t" * self.depth + "</parameterList>")
        return

    def compile_subroutine_body(self):
        # '{' varDec* statements '}'
        self.to_output_file.append("\t" * self.depth + "<subroutineBody>")
        self.depth += 1
        self.__eat("{")
        while self.curr_token.split()[1] == "var":
            self.compile_var_dec()
        self.compile_statements()
        self.__eat("}")
        self.depth -= 1
        self.to_output_file.append("\t" * self.depth + "</subroutineBody>")
        return

    def compile_var_dec(self):
        # 'var' type varName (',' varName)* ';'
        self.to_output_file.append("\t" * self.depth + "<varDec>")
        self.depth += 1
        self.__eat("var")
        # type
        self.__eat(self.curr_token.split()[1])
        # var mane
        self.__eat_by_type(IDENTIFIER)
        while self.curr_token.split([1]) == ",":
            self.__eat(",")
            # type
            self.__eat(self.curr_token.split()[1])
            # var mane
            self.__eat_by_type(IDENTIFIER)
        self.depth -= 1
        self.to_output_file.append("\t" * self.depth + "</varDec>")
        return

    def compile_statements(self):
        self.to_output_file.append("\t" * self.depth + "<statements>")
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
        self.to_output_file.append("\t" * self.depth + "</statements>")
        return

    def compile_let(self):
        self.to_output_file.append("\t" * self.depth + "<letStatement>")
        self.depth += 1
        self.__eat("let")
        # var name
        self.__eat_by_type(IDENTIFIER)
        if self.curr_token.split()[1] == "[":
            self.__eat("[")
            self.compile_expression()
            self.__eat("]")
        self.__eat("=")
        self.compile_expression()
        self.__eat(";")
        self.depth -= 1
        self.to_output_file.append("\t" * self.depth + "</letStatement>")
        return

    def compile_if(self):
        self.to_output_file.append("\t" * self.depth + "<ifStatement>")
        self.depth += 1
        self.__eat("if")
        self.__eat("(")
        self.compile_expression()
        self.__eat(")")
        self.__eat("{")
        self.compile_statements()
        self.__eat("}")
        if self.curr_token.split()[1] == "else":
            self.__eat("else")
            self.__eat("{")
            self.compile_statements()
            self.__eat("}")
        self.depth -= 1
        self.to_output_file.append("\t" * self.depth + "</ifStatement>")
        return

    def compile_while(self):
        self.to_output_file.append("\t" * self.depth + "<whileStatement>")
        self.depth += 1
        self.__eat('while')
        self.__eat('(')
        self.compile_expression()
        self.__eat(')')
        self.__eat('{')
        self.compile_statements()
        self.__eat('}')
        self.depth -= 1
        self.to_output_file.append("\t" * self.depth + "</whileStatement>")
        return

    def compile_do(self):
        # 'do' subroutineCall ';'
        self.to_output_file.append("\t" * self.depth + "<doStatement>")
        self.depth += 1
        self.__eat("do")

        # subroutine call:
        # subroutine name
        self.__eat(IDENTIFIER)
        if self.curr_token.split()[1] == ".":
            self.__eat(".")
            self.__eat(IDENTIFIER)
        self.__eat("(")
        self.compile_expression_list()
        self.__eat(")")

        self.__eat(";")
        self.depth -= 1
        self.to_output_file.append("\t" * self.depth + "</doStatement>")
        return

    def compile_return(self):
        # 'return' expression? ';'
        self.to_output_file.append("\t" * self.depth + "<returnStatement>")
        self.depth += 1
        self.__eat("return")
        if self.curr_token.split()[1] != ";":
            self.compile_expression()
        self.__eat(";")
        self.depth -= 1
        self.to_output_file.append("\t" * self.depth + "</returnStatement>")
        return

    def compile_expression(self):
        self.to_output_file.append("\t" * self.depth + "<expression>")
        self.depth += 1
        self.compile_term()
        while self.curr_token.split()[1] in Syntax.operators:
            # op
            self.__eat(self.curr_token.split()[1])
            self.compile_term()
        self.depth -= 1
        self.to_output_file.append("\t" * self.depth + "</expression>")
        return

    def compile_term(self):
        self.to_output_file.append("\t" * self.depth + "<term>")
        self.depth += 1
        if self.curr_token.split()[0] == IDENTIFIER:
            pass
        else:
            pass
        self.depth -= 1
        self.to_output_file.append("\t" * self.depth + "</term>")
        return

    def compile_expression_list(self):
        self.to_output_file.append("\t" * self.depth + "<expressionList>")
        self.depth += 1
        if self.curr_token.split()[1] != ")":
            self.compile_expression()
            while self.curr_token.split([1]) == ",":
                self.__eat(",")
                self.compile_expression()
        self.depth -= 1
        self.to_output_file.append("\t" * self.depth + "</expressionList>")
        return

    def __eat(self, param):
        token = self.curr_token.split()
        if token[1] != param:
            print("bad line!")
            print("expected:", param)
            print("got:", self.curr_token)
            raise Exception
        else:
            self.to_output_file.append("\t" * self.depth + self.curr_token)
            self.curr_token = self.jack_tokens.advance()

    def __eat_by_type(self, param):
        type_ = self.curr_token.split()[0]
        if type_ != param:
            raise Exception
        else:
            self.to_output_file.append("\t" * self.depth + self.curr_token)
            self.curr_token = self.jack_tokens.advance()
