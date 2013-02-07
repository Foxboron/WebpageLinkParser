#!/usr/bin/env python2

from src.parse import *
from src.menu import *

def main():
    """Main Menu."""
    menu_items = {
    "exit": exit,
    "help": help,
    "save": save,
    "clear": clear,
    "menu": menu,
    "edit": edit,
    "session": session} 
    init("")
    items = get_menu_items()
    menu("")
    while True:
        select = raw_input(">>> ").lower().split()
        if len(select) == 0:
            pass
        elif select[0] in items.keys():
            a = time.time()
            main_parse(select[0])
            print "Time spent: %s" % str(time.time() - a)
        elif select[0] in menu_items.keys():
            menu_items[select[0]](select)
        else:
            print "Not a menu item!"

if __name__ == '__main__':
    try:
        main()
    except (EOFError,KeyboardInterrupt):
        exit(0)