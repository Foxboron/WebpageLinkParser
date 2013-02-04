import os
import json
from src.parse import *


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
    sel = ""
    items = get_menu_items()
    dir_sel = items[select]
    if items[select] in os.listdir("."):
        print "Do you wanna search the dir for html/htm files?"
        while sel == "":
            sel = "y" if raw_input("Y/n >>> ").lower() == "" else "n"
    if sel == "n" or sel == "":
        for i in get_url("http://"+items[select]):
            parse_url(i, dir_sel)
    elif sel == "y":
        for i in dir_walk(items[select]):
            parse_url(i, dir_sel)

def help(arg):
    print """
Menu Items:
    save
    help
    exit
    clear   
"""


def menu(arg):
    items = get_menu_items()
    print "Menu Items:"
    for k,v in items.items():
        print "    %s) %s" % (k,v)


def clear(arg):
    name = strftime("%Y-%m-%d_%H.%M.%S", gmtime())+".json"
    try: os.mkdir("saved")
    except: pass
    if "output.json" in os.listdir("output"):
        print "Saved output.json too %s" % name
        os.rename("output/output.json", "saved/"+name)
    try: os.mkdir("tmp")
    except: pass
    open(os.getcwd()+"/tmp/link", 'wb+').close()
    open(os.getcwd()+"/tmp/openedfiles", 'wb+').close()
    try: os.mkdir("output")
    except: pass
    open(os.getcwd()+"/output/output.json", "wb").close()


from time import gmtime, strftime
def save(arg):
    name = strftime("%Y-%m-%d_%H.%M.%S", gmtime())+".json"
    try: os.mkdir("saved")
    except: pass
    if "output.json" in os.listdir("output"): 
        print "Saved output.json too %s" % name
        os.rename("output/output.json", "saved/"+name)
    init()


def init(arg):
    try: os.mkdir("tmp")
    except: pass
    open(os.getcwd()+"/tmp/link", 'ab+').close()
    open(os.getcwd()+"/tmp/openedfiles", 'ab+').close()
    try: os.mkdir("output")
    except: pass
    open(os.getcwd()+"/output/output.json", "ab").close()
