"""
the syntax of the language using regex
"""

keyword = "class|constructor|function|method|field|static|var|int|char|boolean|void|true|false" \
		  "|null|this|let|do|if|else|while|return"

symbol = "\\{|\\}|\\(|\\)|\\[|\\]|\\.|\\||\\;|\\+|\\-|\\*|\\/|\\&|\\||\\<|\\>|\\=|\\~|\\,"

symbol_to_change = {"<": "&lt;", ">": "&gt;", "\"": "&quot;", "&": "&amp;"}

integer_constant_reg = "\d+"

string_constant_reg = "\"[^\n\"]*\""

identifier_regex = "[a-zA-Z]\w*"

# ADD, SUB, NEG, EQ, GT, LT, AND, OR, NOT
op_name = {"&lt;": "lt", "&gt;": "gt", "+": "add", "-": "sub", "=": "eq", "neg": "neg", "~": "not"}

tokens = [(keyword, "keyword"), (symbol, "symbol"), (integer_constant_reg, "integerConstant"),
		  (string_constant_reg, "stringConstant"), (identifier_regex, "identifier")]

operators = ["+", "-", "*", "|", "/", "&lt;", "&gt;", "=", "&amp;"]
