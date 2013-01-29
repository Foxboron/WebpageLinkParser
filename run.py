#!/usr/bin/env python2
from bs4 import BeautifulSoup
from urlparse import urlparse
from urlhandler import UrlHandler
import urllib
import json
import time
import os


def get_menu_items():
    """Fetches menu items"""
    with open("settings.json", "rb") as f:
        menu = json.loads(f.read())
        urls = menu.keys()
    keys = xrange(1,len(urls)+1)
    d = {str(k): v for k,v in zip(keys,urls)}
    return d

def get_url(content):
    """Takes a URL/File and yields URL's"""
    f = urllib.urlopen(url).read()
    soup = BeautifulSoup(content)
    for link in soup.find_all('a'):
        a = link.get('href')
        if not a or "http" not in a:
            continue
        else:
            yield a

def parse_url(url):
    """Sends a URL to the parser"""
    a = UrlHandler("http://www.vg.no")
    a.url_write(url)


def dir_walk(dir_s):
    """Walks through directories and returns HTM/HTML documents."""
    for i,m,k in os.walk(dir_s):
        if "files" not in i:
            if k:
                try:
                    a = [i+"/"+f for f in k if f.rsplit(".",1)[1] in ["html", "htm"]]
                except IndexError, e:
                    continue
                else:
                    for site in a:
                        timer = time.time()
                        opened_files = open("openedfiles", "rb+")
                        content_file = opened_files.read()
                        opened_files.close()
                        content_file = content_file.split("\n")
                        if site in content_file: 
                            print "skipped "+site
                            continue
                        else: 
                            opened_files = open("openedfiles", "ab+")
                            opened_files.write("\n"+site)
                            opened_files.close()
                            print site
                            with open(site, 'rb') as f:
                                content = f.read()
                                soup = BeautifulSoup(content)
                                for link in soup.find_all('a'):
                                    a = link.get('href')
                                    if not a or "http" not in a:
                                        continue
                                    else:
                                        yield a
                        print time.time() - timer
            else: continue
        else: continue
        
def main():
    items = get_menu_items()
    print "Menu Items:"
    for k,v in items.items():
        print "    %s) %s" % (k,v)
    while True:
        select = raw_input(">>> ")
        if select in items.keys():
            if items[select] in os.listdir("."):
                dir_sel = items[select]
                print "Do you wanna search the dir for html/htm files?"
                sel = ""
                while sel == "":
                    sel = "y" if raw_input("Y/n >>> ").lower() == "" else "n"
            if sel == "n":
                for i in get_url("http://"+items[select]):
                    parse_url(i)
            elif sel == "y":
                for i in dir_walk(items[select]):
                    parse_url(i)
        elif select.lower() == "exit":
            exit()


if __name__ == '__main__':
    a = time.time()
    try:
        main()
    except (EOFError,KeyboardInterrupt):
        exit(0)
    print time.time() - a