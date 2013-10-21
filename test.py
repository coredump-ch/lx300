# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from lx300 import LX300

if __name__ == '__main__':
    printer = LX300()
    try:
        while 1:
            text = raw_input('> ')
            printer.write(text + '\n')
    except (KeyboardInterrupt, EOFError):
        print('\nGoodbye')
