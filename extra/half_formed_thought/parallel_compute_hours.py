# -*- coding: utf-8 -*-
import os, re
import glob
from newtime import newtime
import some_useful_functions as fn
from datetime import datetime
from datetime import timedelta
from some_useful_functions import convertdatetimeobject
from some_useful_functions import mytimestamp
hours_txt = 'data/hours.txt'
file = open(hours_txt, 'w')
file.close()
for file in glob.glob('*cow.txt*'):
    my_dictionary = {}
    with open(file) as f:
        for line in f:
            try:
                line = line.strip()
                datetimestamp = mytimestamp(fn.timestamp(line))
                timestamp = convertdatetimeobject(datetimestamp)
                try:
                    my_dictionary[timestamp].activity +=1
                except KeyError:
                    my_dictionary[timestamp] = newtime(datetimestamp)
            except IndexError:
                print "We are skipping this line (it might be blank)"
                print line
    with open(file) as f:
        for line in f:
            try:
                line = line.strip()
                datetimestamp = mytimestamp(fn.timestamp(line))
                timestamp = convertdatetimeobject(datetimestamp)
                if my_dictionary.has_key(timestamp) == True:
                    for i in range(1,3600):
                        newdatetimestamp = datetimestamp - timedelta(seconds=i)
                        newtimestamp = convertdatetimeobject(newdatetimestamp)
                        if my_dictionary.has_key(newtimestamp):
                            my_dictionary[newtimestamp].activity += 1
            except IndexError:
                print "We are skipping this line (it might be blank)"
                print line


    mylistmax = []
    mylisttimestamp = []

    for i in range(0,10):
        max = 0
        for key in my_dictionary:
            if my_dictionary[key].activity > max:
                max_holder = my_dictionary[key].activity
                if key not in mylisttimestamp:
                    max = max_holder
                    timestamp = key
                    mylistmax.append(max)
                    mylisttimestamp.append(timestamp)
    listDOUBLE = []
    for i in range(0,10):
        listDOUBLE.append([mylistmax[i],mylisttimestamp[i]])
        listDOUBLE.sort()
    file = open(hours_txt, 'a')
    for i in range(0,10):
        if listDOUBLE[10-i-1][0] > 0:
            file.write(listDOUBLE[10-i-1][1]+",%d\n" % listDOUBLE[10-i-1][0])
    file.close()
