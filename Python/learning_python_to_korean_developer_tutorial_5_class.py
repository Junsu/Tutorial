#!/usr/bin/python

import os
import sys


class Human :
    def __init__(self,name) :
        self._name=name
    def name(self):
        return self._name
    def __eq__(self,other):
        if other==None :
            return False
        if self.name()==other.name() :
            return True
        return False
    def __cmp__(self,other) :
        if other==None :
            return 1
        if self.name()<other.name() :
            return -1
        if self.name()>other.name() :
            return 1
        return 0


class Male :
    def sex(self):
        return "Male"


class Ryu(Human,Male) :
    def __init__(self):
        Human.__init__(self,"Dr. Ryu")


class Ko(Human,Male) :
    def __init__(self,name):
        Human.__init__(self,name)
    def __str__(self):
        buf=[]
        buf.append(self.name())
        buf.append(self.sex())
        return " | ".join(buf)


def main() :
    out=sys.stdout

    ryu=Ryu()
    print ryu.name()
    print "%s"%(ryu.sex())
    out.write("%s | %s\n"%(ryu.name(),ryu.sex()))

    ko=Ko("Dr. Ko")
    print ko.name()
    print ko.sex()
    print str(ko)

    ko2=Ko("Dr. Ko")
    ko3=Ko("Dr. Ko3")

    print ""

    print "Class Comparison"
    print ryu==ko
    print ko2==ko
    print ko3==ko

    print ""

    print "Class Sorting"
    human_s=[ryu,ko,ko2,ko3]
    human_s.sort()

    print human_s


if __name__=='__main__' :
    main()


