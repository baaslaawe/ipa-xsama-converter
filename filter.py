#!/usr/bin/python
from __future__ import print_function
import codecs
import sys

def main():
    if len(sys.argv) != 2:
        print_usage()
    symbol_file = sys.argv[1]
    
    symbols = {}
    with codecs.open(symbol_file, 'r', encoding='utf8') as f:
        for line in f:
            for char in line:
                symbols[char] = 1

    line = sys.stdin.readline()
    # Do the conversion now
    while line:
        line = unicode(line, 'utf-8')
        output = ""
        for char in line:
            if symbols.get(char) or char.isspace():
                output += char
	output += "\n"
        try:
            sys.stdout.write(output.encode("utf-8"))
        except IOError:
            try:
                sys.stdout.close()
            except IOError:
                exit(1)
            try:
                sys.stderr.close()
            except IOError:
                exit(1)
            exit(0)
        line = sys.stdin.readline()

def print_usage():
    print("Usage: python filter.py symbol_file")
    print("It will filter on all symbols in the symbol_file")
    print("Program will read from STDIN and write matching symbols to STDOUT")
    exit(1)

if __name__ == "__main__":
    main()
