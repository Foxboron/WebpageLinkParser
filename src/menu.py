import os
import json
from src.parse import *
from src.session import *


def get_menu_items():
    """Fetches menu items from settings.json
        Returns: 
                Dict with {num, item}"""
    urls = _get_settings()
    keys = xrange(1,len(urls)+1)
    d = {str(k): v for k,v in zip(keys,urls)}
    return d


def _get_settings():
    """Fetches the settings file,
        Returns:
                Keys of the JSON file."""
    with open("settings.json", "rb") as f:
        menu = json.loads(f.read())
        urls = menu.keys()
    return urls


def main_parse(select):
    sel = None
    items = get_menu_items()
    dir_sel = items[select]
    if items[select] in os.listdir("."):
        print "Do you wanna search the dir for html/htm files?"
        sel = raw_input("Y/n >>> ").lower()
    if sel == "y" or sel == "":
        for i in dir_walk(items[select]):
            parse_url(i, dir_sel)
    elif sel == "n" or sel == None:
        for i in get_url("http://"+items[select]):
            parse_url(i, dir_sel)

def help(arg):
    print """
Menu Items:
To parse a selected webpage, type the number before the webpage listed.
    menu
        Shows the menu of webpages you can parse according to settings.json
    save [name]
        Saves output.json too the directory 'saved' 
            and parses the info into a readable format.
        If no names is specefied, the time is used instead.
    help
        Shows this message
    exit
        Exits the program.
    session
        Use session help too see a new list of commands!
    edit
        Use session help too see a new list of commands!
    clear [name]
        Clears the tmp directory and saves the file with 
        or without a specefied name and in a readable format.   
"""


def menu(arg):
    """Print the menu!"""
    items = get_menu_items()
    print "Menu Items:"
    for k,v in items.items():
        print "    %s) %s" % (k,v)


def clear(arg):
    """
    Clears the tmp files and saved the output file.
        Input:
            arg:str = Name of the file
    """
    save(arg)
    try: os.mkdir("tmp")
    except: pass
    open(os.getcwd()+"/tmp/link", 'wb+').close()
    open(os.getcwd()+"/tmp/openedfiles", 'wb+').close()
    open(os.getcwd()+"/tmp/output.json", "wb").close()


from time import gmtime, strftime
def save(arg):
    """
    Saves the output file
        Input:
            arg:str = Name of the file
    """
    if len(arg) == 2:
        name = arg[1]+".txt"
    else:
        name = strftime("%Y-%m-%d_%H.%M.%S", gmtime())+".txt"
    try: os.mkdir("saved")
    except: pass
    old = open("tmp/output.json", 'rb')
    try:
        con = parse(json.loads(old.read()))
        with open("saved/"+name, 'wb') as f:
            f.write(con.encode("utf-8"))
        print "Saved output.json too %s" % name
    except ValueError, e:
        print e
        print "Nothing to be saved!"
    old.close()

def parse(con):
    """
    Parses a list for the 'session list' command.
    Input:
        con:tuple = (int, str)
    """
    new = ""
    for k,v in con.iteritems():
        new += "\n%s\n%s\n%s\n\n" % ("#"*len(k),k,"#"*len(k))
        for j,m in v.iteritems():
            new += "%s: %s\n" % (j,m)
    return new

def session(arg):
    """
    Main function for handling the session menu.
    Input:
        arg:list = the command issued.
    Return:
        yeilds the right menu option.
    """
    s = Session()
    if "list" in arg:
        n = s.list_session()
        if n:
            for i in s.list_session():
                date = i[1].split("_")
                print "Session %s Stored: %s %s" % (i[0], date[0], date[1])
        else:
            print "Nothing saved yet"
    elif "save" in arg[1]:
        if len(arg) == 3:
            s.save_session("output.json", "link", "openedfiles", id=arg[2])
        else:    
            s.save_session("output.json", "link", "openedfiles")
        init("")
    if "restore" in arg[1] and len(arg) == 3:
        print "Trying to restore session %s..." % arg[2]
        s.restore_session(arg[2])
    elif "restore" in arg[1] and len(arg) == 2:
        print "Need a number!"
    if "help" in arg:
        session_help()


def session_help():
    """a help menu...doh"""
    print """Sessions Menu Items:
Caches sessions on searches and makes you able to switch between them!
Example:
    session restore 1

save [num]
    Saves the current session

list
    Lists the current sessions saved.

restore [num]
    Restores the session of the given number!  

help
    Displays this message.  
    """

def edit(arg):
    print "Not implemented yet"

def init(arg):
    """Issues the basic dir's and empty files."""
    try: os.mkdir("tmp")
    except: pass
    open(os.getcwd()+"/tmp/link", 'ab+').close()
    open(os.getcwd()+"/tmp/openedfiles", 'ab+').close()
    open(os.getcwd()+"/tmp/output.json", "ab").close()
    try: os.mkdir("session")
    except: pass