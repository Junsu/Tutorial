#!/usr/bin/python

# Learning Python 
# by Junsu Ko

import os
import sys


def tutorial_2_grammar() :
    
    print "IF"
    val_0=True

    if val_0 :
        print "True"
    else :
        print "Else"

    if val_0==True :
        print "True"
    if val_0!=False :
        print "True"


    print ""

    print "FOR 0...3"
    for i in range(4) :
        print i

    print ""

    print "Iteratable"
    val_l=["A",2,"K",5,3,6]
    print val_l
    for val in val_l :
        print val
    val_d={"a":1,"b":"2nd","c":3.5}    
    print val_d
    for val in val_d :
        print val, val_d[val]
    for val in val_d.keys() :
        print val
    for val in val_d.values() :
        print val
    for key,val in val_d.items() :
        print key,val

    print ""

    print "While"
    i=0
    while i<4 :
        i+=1
        print i



if __name__=='__main__' :
    tutorial_2_grammar()

