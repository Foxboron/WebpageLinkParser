#!/usr/bin/env python2

import json
from urlparse import urlparse


class UrlHandler(object):
    def __init__(self, url):
        self.url = urlparse(url)
        self.raw_url = url
        self.json = json.loads(open("settings.json", "rb").read())

    def valid_url(self):
        if self.url.netloc in self.json.keys():
            return True
        return False

    def valid_link(self, link):
        if link in self.json[self.url.netloc]:
            self.link = link
            return True
        self.link = urlparse(link)
        if self.link.path in self.json[self.url.netloc]:
            self.link = self.link.path
            return True
        return False

    def url_write(self, link):
        if self.valid_link(link):
            try:
                with open("output.json", "rb") as f:
                    output = json.loads(f.read())
            except ValueError:
                output = {}
            try:
                output[self.url.netloc][self.link] += 1
            except Exception, e:
                if output == {}:
                    output[self.url.netloc] = {}
                output[self.url.netloc][self.link] = 0
                output[self.url.netloc][self.link] += 1
            l = open("output.json", "wb")
            l.write(json.dumps(output))
        else:
            print self.link
            return False

