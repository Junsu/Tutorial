#!/usr/bin/python

import os
import sys

import re
from subprocess import Popen,PIPE
import glob


def tutorial_system_call() :
    cmd=["ls","-L"]
    try :
        p=Popen(cmd,stdout=PIPE,stderr=PIPE)
    except OSError,e :
        self._eco.logger.error("FAILED CMD\t%s"%(" ".join(cmd)))
        return False
    #
    out,err=p.communicate()
    print out


def tutorial_system_call2() :
    cmd=["ls","-L"]
    os.system(" ".join(cmd))


def tutorial_path_explorer() :
    target_path="./"
    fn_s=sorted(os.listdir(target_path))
    print fn_s


def tutorial_path_explorer2() :
    target_path="./*.gz"
    fn_s=glob.glob(target_path)
    print fn_s


def tutorial_re():
    pattern="^(.*?)_?([ATGC]{8}|[ATGC]{6})?(_L(\\d{3}))?_?R?([12])?(_(\\d{3}))?(\\.clean)?\\.(fastq|fq)\\.?(gz|bz|bz2|bgz|zip)?$"
    fname="T1212D1346_CCGTCC_L007_R1_015.clean.fastq.gz"

    m = re.search(pattern,fname)
    print m.group()
    print m.groups()
    print m.group(0)
    print m.group(1)
    print m.group(2)
    print m.group(3)


def main() :
    print "================================="
    print " System Call 1"
    print "---------------------------------"
    tutorial_system_call()
    print ""
    #
    print "================================="
    print " System Call 2"
    print "---------------------------------"
    tutorial_system_call2()
    print ""
    #
    print "================================="
    print " Path Explorer 1"
    print "---------------------------------"
    tutorial_path_explorer()
    print ""
    #
    print "================================="
    print " Path Explorer 2"
    print "---------------------------------"
    tutorial_path_explorer2()
    print ""
    #
    print "================================="
    print " Regular Expression"
    print "---------------------------------"
    tutorial_re()
    print ""
    #


if __name__=='__main__' :
    main()


