#!/usr/bin/python
"""
oneliners.py is meant to collect one liners for a specific
command so that hey can be stored and later retreived from 
the command line
"""

import shelve
import sys
import os
from optparse import OptionParser

HOMEDIR = os.getenv('HOME')

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
    else:
        result = None
    return result

def main():
    """Main program Execution"""    
    parser = OptionParser()
    
    parser.add_option('-a', '--add', dest="newliner", help='add a new liner to the command specified')
    parser.add_option('-c', '--command', dest="command", help='command that is being accessed')
    (options, args) = parser.parse_args()
    
    datafile = HOMEDIR + '/.oneliners.dat'
    if os.path.exists(datafile):
        myshelf = shelve.open(datafile, 'w',protocol=0)
    else:
        myshelf = shelve.open(datafile, 'c',protocol=0)
    
    if options.command and not options.newliner:
        try:
            for liner in read_liners(myshelf, options.command):
                print liner
        except TypeError:
            print("No Stored Oneliners found for '%s'" % options.command)
        finally:
            pass
    if options.newliner:
        if not options.command:
            print("Command must be specified with -c")
            sys.exit(1)
        add_liner(myshelf, options.command, options.newliner)
    
    myshelf.close()

if __name__ == "__main__":
    main()