#!/usr/bin/env python
"""
Print file with single line output.

Usage: 
  printupdate.py [--wrap] <name> <len>

Examples:
  printupdate.py text 30

Options:
  -h, --help
"""
from docopt import docopt
import sys 
from time import sleep
import os

def process_line(string, length=30, wrap=True):
    string = string[:-1]
    if len(string) <= length:
        yield string
        return
    else:
        if not wrap:
            yield string[:length]
            return
        else:
            start_index = 0
            index = length
            string_len = len(string)
            while index < string_len:
                yield string[start_index:index]
                start_index = index
                index += length
            if index != string_len:
                yield string[start_index:string_len]
            return

if __name__ == '__main__':    
    arguments = docopt(__doc__)
    LENGTH = arguments['<len>']
    INT_LENGTH = int(LENGTH)
    fixed = '{:<' + LENGTH + '}\r'
    pad = INT_LENGTH*" " + "\r"
    WRAP = arguments['--wrap']
    with open(arguments['<name>'], "r") as f:
        for line in f:
            for piece in process_line(line, INT_LENGTH, WRAP):
                if piece == "":
                    continue
                piece = fixed.format(piece)
                sys.stdout.write(pad+piece+'\r')
