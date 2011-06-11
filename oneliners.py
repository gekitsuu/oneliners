#!/usr/bin/python
"""
oneliners.py is meant to collect one liners for a specific
command so that hey can be stored and later retreived from 
the command line
"""

import shelve
import sys
from optparse import OptionParser

def add_liner(myshelf, command, liner):
    """Add a 1-liner to the database"""
    if not myshelf.has_key(command):
        myshelf[command] = []
    linerlist = myshelf[command]
    linerlist.append(liner)
    myshelf[command] = linerlist
    print "%s added to command %s" % (liner, command)

def read_liners(myshelf, command):
    """Read 1-liners from the database for the given command"""
    
    if myshelf.has_key(command):
        result = myshelf[command]
    return result

def main():
    """Main program Execution"""    
    parser = OptionParser()
    
    parser.add_option('-a', '--add', dest="newliner", help='add a new liner to the command specified')
    parser.add_option('-c', '--command', dest="command", help='command that is being accessed')
    (options, args) = parser.parse_args()
    
    datafile = '/home/aglenn/.1liner.dat'
    myshelf = shelve.open(datafile, protocol=0)
    
    if options.command and not options.newliner:
        for liner in read_liners(myshelf, options.command):
            print liner
    if options.newliner:
        if not options.command:
            print("Command must be specified with -c")
            sys.exit(1)
        add_liner(myshelf, options.command, options.newliner)
    
    myshelf.close()

if __name__ == "__main__":
    main()
