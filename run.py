#!/usr/bin/env python2

from src.parse import *
from src.menu import *

def main():
    """Main Menu."""
    menu_items = {
    "exit": exit,
    "help": help,
    "save": save,
    "clear": clear} 
    init()
    items = get_menu_items()
    menu()
    while True:
        select = raw_input(">>> ").lower()
        if select == "":
            pass
        elif select in items.keys():
            a = time.time()
            main_parse(select)
            print "Tinme spent: %s" % str(time.time() - a)
        elif select in menu_items.keys():
            a = time.time()
            menu_items[select]()
            print "Time spent: %s" % str(time.time() - a)
        else:
            print "Not a menu item!"

if __name__ == '__main__':
    try:
        main()
    except (EOFError,KeyboardInterrupt):
        exit(0)