#!/usr/bin/env python2
from bs4 import BeautifulSoup
from urlparse import urlparse
from src.urlhandler import UrlHandler
import urllib
import json
import time
import os


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