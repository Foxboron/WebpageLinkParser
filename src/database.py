#!/usr/bin/env python2
import sqlite3
from pymongo import MongoClient
import time
import os


class DatabaseLayer(object):
    """'Database' handling.
        TL;DR: writes and opens a file.
        Problem: Depending on the end size of the 'link' file
        it might get a bit too big. SOlution is thus to only read 
        from the file when we KNOW something is written too it."""
    def __init__(self):
        self.file = "link"
        self.content = []

    def insert(self, what):
        f = open(self.file, "ab+")
        f.write("\n"+what)
        self_fetch()
        f.close()

    def _fetch(self):
        try:
            f = open(self.file, "rb+")
            s = f.read()
            f.close()
            self.content = s.split("\n")
        except IOError:
            self.content = []

    def fetch(self):
        return self.content

databaselayer = DatabaseLayer()
