# -*- coding: utf-8 -*-
from newuser import newuser
from itertools import groupby
from operator import itemgetter
import some_useful_functions as fn

""" This file is used for obtaining features 1,4, and 5.    """

def feature_1_and_4_and_5(log_txt, hosts_txt, blocked_txt, top_ten_users_bandwidth_txt):
    file = open(blocked_txt, 'w')
    file.close()
    ipaddress_dic = {}
    topten_users_dic = {'a':-1,'b':-2,'c':-3,'d':-4,'e':-5,'f':-6,'g':-7,'h':-8,'i':-9,'j':-10}
    topten_users_bandwidth_dic = {'a':-1,'b':-2,'c':-3,'d':-4,'e':-5,'f':-6,'g':-7,'h':-8,'i':-9,'j':-10}
    with open(log_txt) as infile:
        for line in infile:
            try:
                line = line.strip()
                name_of_user = fn.ipaddress(line)
                try:
                    ipaddress_dic[fn.ipaddress(line)].new_activity(line)
                except KeyError:
                    ipaddress_dic[name_of_user] = newuser(line, blocked_txt)

                try:
                    topten_users_dic[name_of_user] = ipaddress_dic[name_of_user].how_big_of_a_fan
                except KeyError:
                    ordered = sorted(topten_users_dic.iteritems(), key=itemgetter(1))
                    bykey = groupby(ordered, key=itemgetter(1))
                    the_list = map(itemgetter(0), next(bykey)[1])
                    the_min_item = the_list[0]
                    if topten_users_dic[the_min_item] < ipaddress_dic[name_of_user].how_big_of_a_fan:
                        del topten_users_dic[the_min_item]
                        topten_users_dic[name_of_user] = ipaddress_dic[name_of_user].how_big_of_a_fan

                try:
                    topten_users_bandwidth_dic[name_of_user] = ipaddress_dic[name_of_user].totalbandwidth
                except KeyError:
                    ordered = sorted(topten_users_bandwidth_dic.iteritems(), key=itemgetter(1))
                    bykey = groupby(ordered, key=itemgetter(1))
                    the_list = map(itemgetter(0), next(bykey)[1])
                    the_min_item = the_list[0]
                    if topten_users_bandwidth_dic[the_min_item] < ipaddress_dic[name_of_user].totalbandwidth:
                        del topten_users_bandwidth_dic[the_min_item]
                        topten_users_bandwidth_dic[name_of_user] = ipaddress_dic[name_of_user].totalbandwidth
            except IndexError:
                print "We are skipping the line (it might be blank)"
                print line
    file = open(hosts_txt, 'w')
    newlist = sorted(topten_users_dic, key=topten_users_dic.__getitem__, reverse=True)
    for i in range(0,10):
        item = newlist[i]
        if topten_users_dic[item] > -1:
            mystring = item+",%d" % topten_users_dic[item]
            mystring = ''.join(mystring.split())
            file.write(mystring+'\n')
    file.close()

    file = open(top_ten_users_bandwidth_txt, 'w')
    newlist = sorted(topten_users_bandwidth_dic, key=topten_users_bandwidth_dic.__getitem__, reverse=True)
    for i in range(0,10):
        item = newlist[i]
        if topten_users_bandwidth_dic[item] > -1:
            mystring = item+",%d" % topten_users_bandwidth_dic[item]
            mystring = ''.join(mystring.split())
            file.write(mystring+'\n')
    file.close()
