from JackTokenizer import JackTokenizer
from JackFileReader import JackFileReader
import sys

if __name__ == '__main__':
    jack_file = JackFileReader(sys.argv[1])
    print(jack_file.geOneLiner())
    # jack = JackTokenizer(jack_file.geOneLiner())
