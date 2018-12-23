import Syntax
import re


class JackTokenizer:
	"""
	 opens the input jack file and gets ready to tokenize it
	"""

	def __init__(self, all_tokens):
		self.list_of_tokens = self.get_tokens(all_tokens)
		self.curr_token = 0

	def has_more_tokens(self):
		"""
		answers the question: are there any more tokens in the input?
		:return: True if there are more tokens , False otherwise
		"""
		return self.curr_token < len(self.list_of_tokens)

	def advance(self):
		if self.has_more_tokens():
			to_return = self.list_of_tokens[self.curr_token]
			self.curr_token += 1
			return to_return
		return None

	def get_next_token(self, tokens):
		"""
		gets the next token from the input and makes it the return token.
		:param tokens: the tokens
		:return:
		"""
		for token in Syntax.tokens:
			pattern = re.compile(token[0])
			match = pattern.match(tokens)
			if match:
				return match.group(), token[1]
		return None

	def get_tokens(self, tokens):
		"""
		 returns the type of the current token as a constant
		:param tokens:
		:return:
		"""
		list_of_tokens = []
		while not tokens == "":
			next_token, token_type = self.get_next_token(tokens)
			tokens = tokens[len(next_token):]
			tokens = tokens.strip()
			if next_token in Syntax.symbol_to_change.keys():
				next_token = Syntax.symbol_to_change[next_token]
			if next_token.startswith("\""):
				next_token = next_token[1:-1]
			list_of_tokens.append("<" + token_type + "> " + next_token + " </" + token_type + ">")
		return list_of_tokens

	def peek(self):
		"""
		returns the next token
		:return:
		"""
		return self.list_of_tokens[self.curr_token]
