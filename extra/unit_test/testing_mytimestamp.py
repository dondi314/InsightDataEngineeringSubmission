# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.insert(0,'../../src')
from some_useful_functions import mytimestamp

unix_begin = datetime(1970, 1, 1, 0, 0, 0)
dt_type = type(unix_begin)
unix_timestamp = "01/Jan/1970:00:00:00"
print "\n-------TESTING CASE 2------------------\n"
print "-------CHECKING def mytimestamp()\n-------Does it accept and output correct type?"
if type(mytimestamp(unix_timestamp)) == dt_type:
    print 'convertdatetimeobject() accepts correct type and outputs correct type'
    print "accepts <type 'str'>, outputs",dt_type
    print 'test 2 passed'
else:
    print 'convertdatetimeobject() accepts correct type BUT outputs INCORRECT type'
    print "accepts <type 'str'>, outputs ",dt_type
    print 'test 2 failed'
