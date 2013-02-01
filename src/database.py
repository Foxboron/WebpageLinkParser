#!/usr/bin/env python2
import sqlite3
import time
import os


class DatabaseLayer(object):
    """'Database' handling.
        TL;DR: writes and opens a file.
        Problem: Depending on the end size of the 'link' file
        it might get a bit too big. SOlution is thus to only read 
        from the file when we KNOW something is written too it."""
    def __init__(self):
        self.file = os.getcwd()+"/tmp/link"
        self.content = []

    def insert(self, what):
        f = open(self.file, "ab+")
        f.write("\n"+what.encode('utf-8'))
        f.close()

    def fetch(self):
        try:
            f = open(self.file, "rb")
            s = f.read()
            self.content = s.split("\n")
            f.close()
        except IOError:
            self.content = []
        return self.content

databaselayer = DatabaseLayer()
