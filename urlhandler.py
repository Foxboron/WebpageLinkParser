#!/usr/bin/env python2

import json
from database import DatabaseLayer
from urlparse import urlparse


class UrlHandler(object):
    def __init__(self, url):
        self.url = urlparse(url)
        self.raw_url = url
        self.db = DatabaseLayer()
        self.json = json.loads(open("settings.json", "rb").read())


    def valid_link(self, link):
        if link in self.db.fetch():
            return False
        a = urlparse(link)
        print a.netloc
        if a.netloc in self.json[self.url.netloc]:
            if "http" in link:
                if a.path == "" or a.path == "/":
                    self.link = a.geturl()
                else:
                    self.link = a.path.rsplit("/", 1)[0]
                return True

    def url_write(self, link):
        if self.valid_link(link):
            try:
                with open("output.json", "rb") as f:
                    self.output = json.loads(f.read())
            except:
                self.output = {}
            try:
                self.output[self.url.netloc][self.link] += 1
            except Exception, e:
                if self.output == {}:
                    self.output[self.url.netloc] = {}
                self.output[self.url.netloc][self.link] = 0
                self.output[self.url.netloc][self.link] += 1
            self.db.insert(link)
            self.output_stuff()
        else:
            return False

    def output_stuff(self):
        l = open("output.json", "wb")
        l.write(json.dumps(self.output, indent=4))

