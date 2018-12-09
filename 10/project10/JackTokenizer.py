import Syntax
import re


class JackTokenizer:
    # opens the input jack file and gets ready to tokenize it
    def __init__(self):
        self.file_string = 'if(x<0){sos="win"}'

    # are there any more tokens in the input?
    def has_more_tokens(self):
        return not self.file_string == ""

    # gets the next token from the input and makes it the return token.
    def advance(self):
        for token in Syntax.tokens:
            pattern = re.compile(token[0])
            match = pattern.match(self.file_string)
            if match:
                return match.group(), token[1]
        return None

    # returns the type of the current token as a constant
    def get_tokens(self):
        while self.has_more_tokens():
            next_token, token_type = self.advance()
            if next:
                print("<" + token_type + "> " + next_token + " </" + token_type + ">")
                self.file_string = self.file_string[len(next_token):]

