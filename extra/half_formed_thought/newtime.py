# -*- coding: utf-8 -*-
import some_useful_functions as fn
from some_useful_functions import convertdatetimeobject
from some_useful_functions import mytimestamp
import re
from datetime import datetime
from datetime import timedelta

class newtime(object):
    def __init__(self, timeobject):
        self.timeobject = timeobject
        self.activity = 1

    def should_i_add_to_activity(self, anothertimeobject):
        difference = int((self.timeobject - anothertimeobject.timeobject).total_seconds())
        if (difference >= 0 and difference <= 3600):
            self.activity += 1
