# -*- coding: utf-8 -*-
from feature_1_and_4_and_5 import feature_1_and_4_and_5
from feature_2 import feature_2
from feature_3 import feature_3
import some_useful_functions as fn
from some_useful_functions import mytimestamp
from feature_3_command import get_dictionary
from feature_3_command import add_activity_count
from feature_6 import busiest_15_minute_window_per_week
import feature_7

log_txt = 'log_input/log.txt'
# Run feature 1 program and feature_4 program and feature 5 program
hosts_txt = 'log_output/hosts.txt'
blocked_txt = 'log_output/blocked.txt'
top_ten_users_bandwidth_txt = 'log_output/top_ten_users_bandwidth.txt'
feature_1_and_4_and_5(log_txt, hosts_txt, blocked_txt, top_ten_users_bandwidth_txt)

# Run feature 2 program
resources_txt = 'log_output/resources.txt'
feature_2(log_txt, resources_txt)

# Run feature 6 program
busiest_quarter_hours_txt = 'log_output/busiest_quarter_hours.txt'
busiest_15_minute_window_per_week(log_txt, busiest_quarter_hours_txt)

# Run feature)_7 program
busiest_15_minute_bandwidth_txt = 'log_output/busiest_15_minute_bandwidth.txt'
feature_7.busiest_15_minute_bandwidth(log_txt, busiest_15_minute_bandwidth_txt)

# Run feature 3 program
hours_txt = 'log_output/hours.txt'
file = open(hours_txt, 'w')
file.close()
try:
    feature_3(log_txt, hours_txt)
except UnboundLocalError:
    print "Nothing printed to hours.txt.  Are you sure the log file is not blank?\n"
