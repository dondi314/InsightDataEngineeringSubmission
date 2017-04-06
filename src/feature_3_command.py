# -*- coding: utf-8 -*-
from newuser import newuser as newuser
from itertools import groupby
from operator import itemgetter
from newtime import newtime
import some_useful_functions as fn
from some_useful_functions import convertdatetimeobject
from some_useful_functions import mytimestamp
import re
from datetime import datetime
from datetime import timedelta


def get_dictionary(log_txt):
    my_dictionary = {}
    with open(log_txt) as f:
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
    return my_dictionary

def add_activity_count(my_dictionary, log_txt):

    with open(log_txt) as f:
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
    return my_dictionary
