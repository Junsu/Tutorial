#!/usr/bin/python

import os
import sys

import MySQLdb


def tutorial_mysql_connect() :
    db = MySQLdb.connect(db="GI_WEB",user="USER",passwd="PASSWD",host="dog",charset='utf8')
    cursor = self.db.cursor()

    rst=cursor.execute("SELECT * FROM user")
    if rst!=None or rst==0 :
        for rec in cursor.fetchall() :
            print rec

    cursor.close()
    db.close()


if __name__=='__main__' :
    tutorial_mysql_connect()
