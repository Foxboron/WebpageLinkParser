#!/usr/bin/env python2
from bs4 import BeautifulSoup
from urlparse import urlparse
from urlhandler import UrlHandler
import urllib
import json

def get_url():
    f = urllib.urlopen("http://vg.no").read()
    soup = BeautifulSoup(f)
    for link in soup.find_all('a'):
        a = link.get('href')
        if not a or "http" not in a or "nyheter/innenriks" not in a:
            continue
        else:
            yield a

def parse_url(url):
    a = UrlHandler(url)
    print a.url_write("http://skattelister.no/")


def main():
    for i in get_url():
        parse_url(i)
        break


if __name__ == '__main__':
    main()