# -*- coding: utf-8 -*-
from datetime import datetime
import sys
sys.path.insert(0,'../src')
from some_useful_functions import convertdatetimeobject

unix_begin = datetime(1970, 1, 1, 0, 0, 0)
dt_type = type(unix_begin)
print "\n-------TESTING CASE 1------------------\n"
print "-------CHECKING def convertdatetimeobject()\n-------Does it accept and output correct type?"
if type(convertdatetimeobject(unix_begin)) == type('string'):
    print 'convertdatetimeobject() accepts correct type and outputs correct type'
    print "accepts <type 'datetime.datetime'>, outputs <type 'str'>"
    print 'test 1 passed'
else:
    print 'convertdatetimeobject() accepts correct type BUT outputs INCORRECT type (without throwing error)'
    print "accepts <type 'str'>, outputs ",type(convertdatetimeobject(unix_begin))
