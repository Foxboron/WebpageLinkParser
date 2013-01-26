#!/usr/bin/env python2
import sqlite3


class DatabaseLayer(object):
    """Trol"""
    def __init__(self):
        self.sql_statment = ""
        self.dbfile = "database.db"
        self.conn = sqlite3.connect(self.dbfile, check_same_thread=False)
        self.c = self.conn.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS viewcount
                        (site TEXT )
                        """)
        self.conn.commit()

    def insert(self, what):
        self.c.execute("""INSERT or replace into viewcount (site) VALUES(?)""", [what,])
        self.conn.commit()

    def fetch(self):
        self.c.execute("SELECT * FROM viewcount")
        result = [element[0] for element in self.c.fetchall()]
        return result

databaselayer = DatabaseLayer()
