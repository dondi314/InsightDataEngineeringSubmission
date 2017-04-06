import re
hours_txt = 'data/hours.txt'
hours1_txt = 'data/hours1.txt'
max_list = [(-1, 'fred') for x in range(10)]
max = -1
toptennames = ['fred' for x in range(10)]
with open(hours_txt) as f:
    for line in f:
        line = line.strip()
        line = line.split(',')
        if len(line) == 2:
            hold = int(line[1])
            print type(hold)
            timestamp = line[0]
            print timestamp
            print timestamp
            if hold > max:
                max = hold
                max_list.pop(0)
                max_list.append((max, timestamp))
                max_list = sorted(max_list)
with open(hours1_txt) as f:
    for line in f:
        line = line.strip()
        line = line.split(',')
        hold = int(line[1])
        timestamp = line[0]
        if hold > max:
            max = hold
            max_list.pop(0)
            max_list.append((max, timestamp))
            max_list = sorted(max_list)

file = open(hours_txt, 'w')
for i in range(0,10):
    if max_list[10-i-1][0] > 0:
            file.write(max_list[10-i-1][1]+",%d\n" % max_list[10-i-1][0])
file.close()
