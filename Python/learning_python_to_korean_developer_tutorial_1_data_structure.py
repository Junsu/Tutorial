#!/usr/bin/python

# Learning Python 
# by Junsu Ko

import os
import sys


def sort_by_custom(one,other) :
    if isinstance(one,str) and not isinstance(other,str) :
        return -1
    if not isinstance(one,str) and isinstance(other,str) :
        return 1
    if one>other :
        return 1
    if one<other :
        return -1
    return 0


def tutorial_1_data_type() :
    
    # Boolean
    val_0=True

    # Integer
    val_a=1

    # Float
    val_b=2.56

    # String
    val_c='Single quat. is string.'
    val_d="Double quat. is string, too"
    val_e='''Triple quat. is multi-line string.
    For triple, single, and double is sample feature.'''

    # List
    print "List"
    val_l=['1st',4,3,2,3.5]
    print val_l
    val_l.append("test")
    print val_l
    val_l.sort()                # Sorting
    print val_l
    val_l.sort(sort_by_custom)  # Custom Sorting
    print val_l
    val_l.reverse()             # Reverse
    print val_l
    val_l_2=val_l[1:4]          # Slicing
    print val_l_2

    print ""

    # Diction
    print "Diction (Hashing)"
    val_l={"1st":1, "2nd":"string data"}
    print val_l
    val_l["3rd"]="hi, yo"
    print val_l
    print val_l["2nd"]

    print ""

    # Set
    print "Set (Unique Set)"
    val_s=set(["hi","wow"])
    print val_s
    val_s.add("wow")
    print val_s
    val_s.add("wow2")
    print val_s


if __name__=='__main__' :
    tutorial_1_data_type()

