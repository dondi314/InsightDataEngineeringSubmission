# -*- coding: utf-8 -*-
import some_useful_functions as fn
from datetime import datetime
from datetime import timedelta
from some_useful_functions import mytimestamp

def busiest_15_minute_window_per_week(log_txt, busiest_quarter_hours_txt):
    time_window = {}
    for i in range(0,24):
        for j in range(0,4):
            for k in range(0,7):
                time_window[(i,j,k)] = 0
    with open(log_txt) as infile:
        for line in infile:
            try:
                line = line.strip()
                datetimestamp = mytimestamp(fn.timestamp(line))
                the_hour = datetimestamp.hour
                the_minute = datetimestamp.minute
                the_day_of_week = datetimestamp.weekday()
                if the_minute < 15:
                    the_quarter = 0
                elif the_minute < 30:
                    the_quarter = 1
                elif the_minute < 45:
                    the_quarter = 2
                else:
                    the_quarter = 3
                time_window[(the_hour, the_quarter, the_day_of_week)]+=1
            except IndexError:
                print "We are skipping this line (it might be blank)"
                print line
    my_count_list = []
    for key in time_window:
        my_count_list.append([time_window[key],key])
    my_count_list.sort()
    file = open(busiest_quarter_hours_txt, 'w')
    x = 4*7*24
    for i in range(0,x-1):
        number = my_count_list[x-i-1][0]
        item = my_count_list[x-i-1][1]
        item2 = fn.how_to_convert(item)
        if number != 0:
            file.write(item2+',%d\n' % number)
    file.close()
