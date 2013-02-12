#!/usr/bin/env python2
import sqlite3
import os
import hashlib
import shutil
from time import gmtime, strftime

def hashname(name):
    hash = hashlib.sha224(name).hexdigest()
    return hash


class Session(object):
    """Saves sessions"""
    def __init__(self):
        self.tmp_dir = os.getcwd()+"/tmp/"
        self.session_dir = os.getcwd()+"/session/"
        self.direc = os.getcwd()+"/session/"
        self.dbfile = self.direc+'Sessions.db'
        self.conn = sqlite3.connect(self.dbfile)
        self.conn.text_factory = str
        self.c = self.conn.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS thisisatable
                        (id integer PRIMARY KEY, 
                        output TEXT,
                        link TEXT,
                        openedfiles TEXT,
                        datetime TEXT)
                        """)
        self.conn.commit()
        try:
            self.c.execute ("""
                ALTER TABLE thisisatable
                ADD settings TEXT""")
        except Exception: pass
        else: self.conn.commit()
        self.result = []

    def fetch_session(self, num):
        """Searches the database for a variable"""
        try:
            self.c.execute("""SELECT output, link, openedfiles, settings FROM thisisatable WHERE id=?""", [num,])
        except:
        #Return False if query is not found
            return False
        
        else:
            #Returns True if query is fetched.
            self.result = [i for i in self.c.fetchall()[0]]
            return self.result

    def _empty_files(self):
        l = ["link", "openedfiles", "output.json"]
        for i in l:
            f = open("tmp/" + i)
            con = f.read()
            if con:
                return False
        return True

    def restore_session(self, num):
        if self._empty_files():
            output, link, openedfiles, settings = self.fetch_session(num)
            shutil.copy(self.session_dir+output, self.tmp_dir+"output.json")
            shutil.copy(self.session_dir+link, self.tmp_dir+"link")
            shutil.copy(self.session_dir+openedfiles, self.tmp_dir+"openedfiles")
            if settings:
                shutil.copy(self.session_dir+settings, os.getcwd()+"/settings.json")
            else: print "Session don't got a settings.json. The current settings.json file will be used upon save."
            print "Done"
        else:
            print "Consider clearing or saving your session before restoring another!"
        
    def save_session(self, output, link, openedfiles, id=None):
        name = strftime("%Y-%m-%d_%H.%M.%S", gmtime())
        output_new = hashname(name)+".output"
        link_new = hashname(name)+".link"
        openedfiles_new = hashname(name)+".openedfiles"
        settings_new = hashname(name)+".settings"
        try:
            if id:
                try:
                    self.c.execute("""INSERT OR REPLACE INTO thisisatable (id, output, link, openedfiles, settings, datetime) VALUES(?,?,?,?,?,?)""", 
                    [id, output_new, link_new, openedfiles_new, settings_new, name])
                except Exception, e:
                    print e
            else:
                try:
                    self.c.execute("""INSERT OR REPLACE INTO thisisatable (output, link, openedfiles, settings, datetime) VALUES(?,?,?,?,?)""", 
                    [output_new, link_new, openedfiles_new, settings_new, name])
                except Exception, e:
                    print e
        except Exception, e:
            if e == "datatype mismatch":
                print "Did you write a number?"
        else:
            try:
                os.rename(self.tmp_dir+output, self.session_dir+output_new)
                os.rename(self.tmp_dir+link, self.session_dir+link_new)
                os.rename(self.tmp_dir+openedfiles, self.session_dir+openedfiles_new)
                shutil.copy("settings.json", self.session_dir+settings_new)
            except Exception, e:
                self.conn.rollback()
                print "We got an error!"
            else:
                self.conn.commit()
                print "Saved session!"

    def list_session(self):
        try:
            self.c.execute("SELECT id, datetime FROM thisisatable")
            self.result=[element for element in self.c.fetchall()]
            return self.result
        except:
            return None
