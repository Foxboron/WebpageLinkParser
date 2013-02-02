#!/usr/bin/env python2

from bs4 import BeautifulSoup
from urlparse import urlparse
from src.urlhandler import UrlHandler
import urllib
import json
import time
import os


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

def get_url(content):
    """Takes a URL/File and yields URL's
        Input: 
                content:str = URL
        Returns:
                yields url:str"""
    f = urllib.urlopen(content).read()
    soup = BeautifulSoup(f)
    for link in soup.find_all('a'):
        a = link.get('href')
        if not a or "http" not in a:
            continue
        else:
            yield a

def parse_url(url, selected_item):
    """Sends a URL to the parser.
        Input:
                url:str = url we need to parse"""
    if "http://" not in selected_item:
        selected_item = "http://"+selected_item
    a = UrlHandler(selected_item)
    a.url_write(url)


def dir_walk(dir_s):
    """Walks through directories and yields HTM/HTML documents.
        Input:
                dir_s:str = directory to start at.
        Return:
                yields url:str"""
    for i,m,k in os.walk(dir_s):
        if "files" not in i and k:
            try:
                a = [i+"/"+f for f in k if f.rsplit(".",1)[1] in ["html", "htm"]]
            except IndexError, e:
                continue
            else:
                for site in a:
                    timer = time.time()
                    opened_files = open(os.getcwd()+"/tmp/openedfiles", "rb+")
                    content_file = opened_files.read()
                    opened_files.close()
                    content_file = content_file.split("\n")
                    if site not in content_file: 
                        opened_files = open(os.getcwd()+"/tmp/openedfiles", "ab+")
                        opened_files.write("\n"+site)
                        opened_files.close()
                        with open(site, 'rb') as f:
                            content = f.read()
                            soup = BeautifulSoup(content)
                            for link in soup.find_all('a'):
                                a = link.get('href')
                                if a == None: continue
                                if a or "http" in a:
                                    yield a

def init():
    try: os.mkdir("tmp")
    except: pass
    open(os.getcwd()+"/tmp/link", 'ab+').close()
    open(os.getcwd()+"/tmp/openedfiles", 'ab+').close()
    try: os.mkdir("output")
    except: pass
    open(os.getcwd()+"/output/output.json", "ab").close()
    
def main():
    """Main Menu."""
    init()
    items = get_menu_items()
    print "Menu Items:"
    for k,v in items.items():
        print "    %s) %s" % (k,v)
    while True:
        select = raw_input(">>> ")
        if select in items.keys():
            sel = ""
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
        elif select.lower() == "exit":
            exit()


if __name__ == '__main__':
    a = time.time()
    try:
        main()
    except (EOFError,KeyboardInterrupt):
        exit(0)
    print time.time() - a
