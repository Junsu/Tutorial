#!/usr/bin/python

# Learning Python 
# by Junsu Ko

import os
import sys


def tutorial_3_io() :

    _out=file("test",'wt')
    _out.write("Hello, Python.\n")
    _out.write("Oh, My God.")
    _out.close()

    _in=file("test")
    print _in.readline()
    for line in _in :
        print line
    _in.close()

    print ""

    print "With"
    with file("test") as _in :
        for line in _in :
            print line
        

if __name__=='__main__' :
    tutorial_3_io()


