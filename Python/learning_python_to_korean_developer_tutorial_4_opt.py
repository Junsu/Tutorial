#!/usr/bin/python

# Learning Python 
# by Junsu Ko

#
# Command 
#   python learning_python_to_korean_developer_tutorial_4_opt.py EXAMPLE 
#

import os
import sys


def tutorial_4_opt() :
    print sys.argv[0]
    if len(sys.argv)>1 :
        print sys.argv[1]
    
    for arg in sys.argv :
        print arg
        

if __name__=='__main__' :
    tutorial_4_opt()


