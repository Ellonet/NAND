import sys
import JackTokenizer
import Syntax
import re

if __name__ == '__main__':
    check = "method(x<0){class=3}"

    temp = re.compile(Syntax.keyword)
    i = re.match(temp, check)
    match = i.group()
    print(match)
    check = check[len(match):]
    temp = re.compile(Syntax.symbol)
    i = re.match(temp, check)
    match = i.group()
    print(match)