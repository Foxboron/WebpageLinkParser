#!/usr/bin/env python2
import sqlite3
from pymongo import MongoClient
import time
import os


class DatabaseLayer(object):
    """Trol"""
    def __init__(self):
        self.file = "link"

    def insert(self, what):
        f = open(self.file, "wb+")
        f.write("\n"+what)
        f.close()
        

    def fetch(self):
        try:
            f = open(self.file, "rb+")
            s = f.read()
            f.close()
            s = s.split("\n")
        except IOError:
            s = []
        return s

databaselayer = DatabaseLayer()
