#!/usr/bin/env python2
from bs4 import BeautifulSoup
from urlparse import urlparse
from urlhandler import UrlHandler
import urllib
import json
import time

def get_url():
    f = urllib.urlopen("http://www.vg.no").read()
    soup = BeautifulSoup(f)
    for link in soup.find_all('a'):
        a = link.get('href')
        if not a or "http" not in a:
            continue
        else:
            yield a

def parse_url(url):
    a = UrlHandler("http://www.vg.no")
    a.url_write(url)


def main():
    for i in get_url():
        parse_url(i)


if __name__ == '__main__':
    a = time.time()
    main()
    print time.time() - a