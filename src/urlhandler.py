#!/usr/bin/env python2

import json
from database import DatabaseLayer
from urlparse import urlparse
import os

class UrlHandler(object):
    """Main handler for the parser. Checks the given URL and 
    decides if it should be written too the JSON file or passed."""
    def __init__(self, url):
        self.url = urlparse(url)
        self.raw_url = url
        self.db = DatabaseLayer()
        self.json = json.loads(open("settings.json", "rb").read())


    def valid_link(self, link):
        """Checks if the given URL is already read.
            Input:
                    link:str = URL
            Return:
                    bool True or False"""
        if link.encode('utf-8') in self.db.fetch():
            return False
        a = urlparse(link)
        if a.netloc in self.json[self.url.netloc]:
            if "http" in link:

                if a.path == "" or a.path == "/":
                    self.link = a.geturl()
                    print self.link
                else:
                    self.link = a.path.rsplit(".", 1)[0]
                    if self.link[-1] == "/": self.link = self.link[:-1]
                    if "article" in self.link: self.link = a.path.rsplit("/", 1)[0]
                    print self.link
                return True

    def url_write(self, link):
        """Checks the URL if valid or not.
            Then writes too file and 'database'
            depending on the result.
            Input:
                    link:str = URL
            Return:
                    bool True or False depending on result"""
        if self.valid_link(link):
            try:
                with open(os.getcwd()+"/output/outputjson", "rb") as f:
                    self.output = json.loads(f.read(),encoding="utf-8")
            except:
                self.output = {}
            try:
                self.output[self.url.netloc][self.link] += 1
            except Exception, e:
                if self.output == {} or self.url.netloc not in self.output.keys():
                    self.output[self.url.netloc] = {}
                self.output[self.url.netloc][self.link] = 0
                self.output[self.url.netloc][self.link] += 1
            self.db.insert(link)
            self._output_stuff()
            return True
        else:
            #print "skipped url: %s" % link
            return False

    def _output_stuff(self):
        """Writes dict too output json file."""
        with open(os.getcwd()+"/output/outputjson", "wb") as l:
            con = json.dumps(self.output, indent=4, sort_keys=True, encoding="ASCII")
            l.write(con)


