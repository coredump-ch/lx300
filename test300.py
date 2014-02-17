# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals


class Escape(object):
    esc = chr(27)
    italic_start = esc + b'4'
    italic_end = esc + b'5'


class LX300(object):

    def write(self, text):
        print(text.encode('cp850', 'replace').decode('cp850').encode('utf8'))
