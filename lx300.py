# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from serial import Serial


class Escape(object):
    esc = chr(27)
    italic_start = esc + b'4'
    italic_end = esc + b'5'


class LX300(object):

    def __init__(self, port='/dev/ttyS0', baudrate=19200):
        self.ser = Serial(port, baudrate)
        init = Escape.esc + b'@'
        select = chr(17)
        self.ser.write(init + select)

    def write(self, text):
        self.ser.write(text.encode('cp850', 'replace'))
