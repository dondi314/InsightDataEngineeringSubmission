# -*- coding: utf-8 -*-
from newuser import newuser as newuser
from itertools import groupby
from operator import itemgetter
import some_useful_functions as fn
from some_useful_functions import convertdatetimeobject
from some_useful_functions import mytimestamp
from newtime import newtime
import re
from datetime import datetime
from datetime import timedelta
from feature_3_command import get_dictionary
from feature_3_command import add_activity_count

def feature_3(log_txt, hours_txt):
    my_dictionary = get_dictionary(log_txt)
    my_dictionary = add_activity_count(my_dictionary, log_txt)

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
    file = open(hours_txt, 'w')

    for i in range(0,10):
        if listDOUBLE[10-i-1][0] > 0:
            file.write(listDOUBLE[10-i-1][1]+",%d\n" % listDOUBLE[10-i-1][0])
    file.close()
