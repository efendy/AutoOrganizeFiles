#!/usr/bin/python

import os, sys

SCRIPT_NAME = os.path.basename(__file__)
ACTIONS = ["start", "end", "list", "help"]

def start(directorypath):
    print("")

def end(directorypath):
    print("")
    
def show():
    print("")

def help():
    print("")
    print("Usage: {} <action> [<directory_path>]".format(SCRIPT_NAME))
    print(" action:")
    print("     start <directory_path>")
    print("     end <directory_path>")
    print("     show")
    print("     help")
    print(" i.e: python3 {} start ~/Downloads/".format(SCRIPT_NAME))
    print("- end -")

def main(argv):
    if len(argv) > 0:
        action = argv[0]
        if action == "show":
            show()
            sys.exit()
        if len(argv) > 1:
            directorypath = argv[1]
            if action == "start":
                if not os.path.exists(directorypath):
                    print("Error: {} does not exist.".format(directorypath))
                    help()
                    sys.exit(2)
                start(directorypath)
                sys.exit()
            if action == "end":
                end(directorypath)
                sys.exit()
        
    help()

if __name__ == "__main__":
   main(sys.argv[1:])