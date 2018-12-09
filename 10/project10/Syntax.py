keyword = "class|constructor|function|method|field|static|var|int|char|boolean|void|true|false|null|this|let|do|if|\
           else|while|return"
symbol = "\\{|\\}|\\(|\\)|\\[|\\]|\\.|\\||\\;|\\+|\\-|\\*|\\/|\\&|\\||\\<|\\>|\\=|\\~"

integer_constant_reg = "\d+"

string_constant_reg = "\"[^\n\"]*\""

identifier_regex = "[a-zA-Z]\w*"

tokens = [(keyword, "keyword"), (symbol, "symbol"), (integer_constant_reg, "intConst"),
          (string_constant_reg, "stringConst"), (identifier_regex, "identifier")]
