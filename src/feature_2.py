# -*- coding: utf-8 -*-
from newresource import newresource
from itertools import groupby
from operator import itemgetter
import some_useful_functions as fn

def feature_2(log_txt, resources_txt):
    resources_dic = {}
    topten_resources_dic = {'a':-1,'b':-2,'c':-3,'d':-4,'e':-5,'f':-6,'g':-7,'h':-8,'i':-9,'j':-10}
    with open(log_txt) as infile:
        for line in infile:

            try:

                resource = fn.resource(line)
                timestamp = fn.timestamp(line).strip()
                timestamp2 = timestamp + " -400"
                integer_current_time = fn.date_seconds(timestamp)
                if resources_dic.has_key(resource):
                    resources_dic[resource].add_to_bandwidth()
                else:
                    resources_dic[resource] = newresource(line)
                    resource_new = resources_dic[resource]
                if topten_resources_dic.has_key(resource):
                    topten_resources_dic[resource] = resource_new.bandwidth
                else:
                    ordered = sorted(topten_resources_dic.iteritems(), key=itemgetter(1))
                    bykey = groupby(ordered, key=itemgetter(1))
                    the_list = map(itemgetter(0), next(bykey)[1])
                    the_min_item = the_list[0]
                    if topten_resources_dic[the_min_item] < resource_new.bandwidth:
                        del topten_resources_dic[the_min_item]
                        topten_resources_dic[resource] = resource_new.bandwidth
            except IndexError:
                if not line.strip():
                    print "We are skipping this line (it might be blank)"
                    print line
    file = open(resources_txt, 'w')
    newlist = sorted(topten_resources_dic, key=topten_resources_dic.__getitem__, reverse=True)
    for i in range(0,10):
        item = newlist[i]
        if topten_resources_dic[item] > -1:
            file.write(item+'\n')
    file.close()
