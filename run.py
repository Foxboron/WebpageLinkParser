#!/usr/bin/env python2

from src.parse import *
from src.menu import *

def main():
    """Main Menu."""
    menu_items = {
    "exit": exit,
    "help": help} 
    init()
    items = get_menu_items()
    menu()
    while True:
        select = raw_input(">>> ").lower()
        if select == "":
            pass
        elif select in items.keys():
            main_parse(select)
        elif select in menu_items.keys():
            menu_items[select]()
        else:
            print "Not a menu item!" 

if __name__ == '__main__':
    a = time.time()
    try:
        main()
    except (EOFError,KeyboardInterrupt):
        exit(0)
    print time.time() - a
