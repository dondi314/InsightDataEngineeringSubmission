# -*- coding: utf-8 -*-
import some_useful_functions as fn
class newresource(object):
    def __init__(self, input):
        self.name = fn.resource(input)
        code, bits = fn.code_bits(input)
        self.bandwidth = bits
        self.bits = bits

    def add_to_bandwidth(self):
        self.bandwidth += self.bits
