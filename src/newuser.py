import some_useful_functions as fn
from datetime import datetime
from datetime import timedelta

'''This class creates a new user.  The first input variable should be an unformatted line of
text from the log file, and the second variable should be the location of the blocked textfile,
i.e. it should be (/log_output/blocked.txt).  This file is responsible for determining if the
user should be blocked or not.'''

class newuser(object):

    def __init__(self, input, blocked_txt):
        self.input = input.strip()
        self.blocked_txt = blocked_txt
        code, bits = fn.code_bits(input)
        was_there_a_breach = fn.security_breach(code)
        total_security_breaches_ever = 0
        total_security_breaches_last_20 = 0
        integer_breach_end_time = 0
        integer_current_time = fn.date_seconds(fn.timestamp(input))
        if was_there_a_breach == True:
            total_security_breaches_ever += 1
            total_security_breaches_last_20 += 1
            integer_breach_end_time = integer_current_time + 20
        self.total_security_breaches_ever = total_security_breaches_ever
        self.total_security_breaches_last_20 = total_security_breaches_last_20
        self.integer_current_time = integer_current_time
        self.integer_breach_end_time = integer_breach_end_time
        self.ipaddress = fn.ipaddress(input)
        self.how_big_of_a_fan = 1
        self.bits = bits
        self.integer_imprison_end_time = 0
        self.totalbandwidth = self.bits

    def new_activity(self, input):
        self.input = input
        self.how_big_of_a_fan += 1
        self.integer_current_time = fn.date_seconds(fn.timestamp(input))
        code, bits = fn.code_bits(input)
        self.bits = bits

        self.totalbandwidth += self.bits
        breach = fn.security_breach(code)
        if breach == True:
            self.total_security_breaches_ever += 1
            self.check_for_breach_lockdown()
        else:
            if self.integer_current_time <= self.integer_imprison_end_time and code == '200':
                self.total_security_breaches_ever += 1
                file = open(self.blocked_txt, 'a')
                file.write(self.input.strip()+"\n")
                file.close()
            if self.integer_current_time > self.integer_imprison_end_time and code == '200':
                self.integer_imprison_end_time = 0
                self.breach_end_time = 0



    def check_for_breach_lockdown(self):
        A = self.integer_current_time
        B = self.integer_breach_end_time
        C = self.integer_imprison_end_time

        if A > C:
            if A > B:
                self.total_security_breaches_last_20 = 1
                self.integer_breach_end_time = self.integer_current_time + 20
            if A <= B and self.total_security_breaches_last_20 <= 2:
                self.total_security_breaches_last_20 += 1
            if A <= B and self.total_security_breaches_last_20 == 3:
                self.integer_imprison_end_time = A + (5*60)
                self.total_security_breaches_last_20 = 0

        else:

            file = open(self.blocked_txt, 'a')
            file.write(self.input.strip()+"\n")
            file.close()
