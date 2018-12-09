from JackTokenizer import JackTokenizer
from JackFileReader import JackFileReader
import Syntax


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
        self.__handle_terminal_exp("<identifier>")
        self.__eat("{")
        # todo zero or more
        self.compile_class_var_dec()
        # todo zero or more
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

        self.depth -= 1
        self.to_output_file.append("\t" * self.depth + "</classVarDec>")

        return

    def compile_subroutine_dec(self):
        # ('constructor' | 'function' | 'method') ('void' | type) subroutineName '(' parameterList ')' subroutineBody
        return

    def compile_parameters_list(self):
        # ( (type varName) (',' type varName)*)?
        return

    def compile_subroutine_body(self):
        # '{' varDec* statements '}'
        return

    # def compile_subroutine_call(self):
    #     # subroutineName '(' expressionList ')' | ( className | varName) '.' subroutineName  '(' expressionList ')'
    #     return

    def compile_var_dec(self):
        # 'var' type varName (',' varName)* ';'

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
            else:
                statements = False

        self.depth -= 1
        self.to_output_file.append("\t" * self.depth + "</statements>")
        return

    def compile_let(self):
        self.to_output_file.append("\t" * self.depth + "<letStatement>")
        self.depth += 1
        self.__eat("let")
        self.__handle_terminal_exp("<identifier>")
        self.__eat("=")
        self.compile_expression()
        self.__eat(";")
        self.depth -= 1
        self.to_output_file.append("\t" * self.depth + "</letStatement>")

        return

    def compile_if(self):
        self.to_output_file.append("\t" * self.depth + "<ifStatement>")
        self.depth += 1
        # todo!!!!!
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
        self.to_output_file.append("\t" * self.depth + "<do>")
        self.depth += 1
        self.__eat("do")
        # todo subroutine call
        self.__eat(";")
        self.depth -= 1
        self.to_output_file.append("\t" * self.depth + "</do>")

        return

    def compile_return(self):
        # 'return' expression? ';'
        self.to_output_file.append("\t" * self.depth + "<return>")
        self.depth += 1
        self.__eat("return")
        if self.curr_token.split()[1] != ";":
            self.compile_expression()
        self.__eat(";")
        self.depth -= 1
        self.to_output_file.append("\t" * self.depth + "</return>")
        return

    def compile_expression(self):
        self.to_output_file.append("\t" * self.depth + "<expression>")
        self.depth += 1
        self.compile_term()
        if self.curr_token.split()[1] in Syntax.operators:
            self.to_output_file.append("\t" * self.depth + self.curr_token)
            self.curr_token = self.jack_tokens.advance()
            self.compile_term()
        self.depth -= 1
        self.to_output_file.append("\t" * self.depth + "</expression>")
        return

    def compile_term(self):
        self.to_output_file.append("\t" * self.depth + "<term>")
        self.depth += 1
        self.__handle_terminal_exp("<identifier>")
        self.depth -= 1
        self.to_output_file.append("\t" * self.depth + "</term>")
        return

    def compile_expression_list(self):
        return

    def __eat(self, param):
        token = self.curr_token.split()
        if token[1] != param:
            raise Exception
        else:
            self.to_output_file.append("\t" * self.depth + self.curr_token)
            self.curr_token = self.jack_tokens.advance()

    def __handle_terminal_exp(self, param):
        type = self.curr_token.split()[0]
        if type != param:
            raise Exception
        else:
            self.to_output_file.append("\t" * self.depth + self.curr_token)
            self.curr_token = self.jack_tokens.advance()

    def handel_type(self):
        # 'int' | 'char' | 'boolean' | className
        return
