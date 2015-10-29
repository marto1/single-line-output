"""
Print file with single line output.

Usage: 
printupdate.py <name> <len>

Examples:
  printupdate.py text 30

Options:
  -h, --help
"""
from docopt import docopt
import sys 
from time import sleep
import os



if __name__ == '__main__':    
    arguments = docopt(__doc__)
    LENGTH = arguments['<len>']
    fixed = '{:<' + LENGTH + '}\r'
    pad = int(LENGTH)*" " + "\r"
    with open(arguments['<name>'], "r") as f:
        for line in f:
            line = line[:-1]
            line = line[:int(LENGTH)]
            if line == "":
                continue
            l = fixed.format(line)
            sys.stdout.write(pad)
            sys.stdout.write(l)
