# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import textwrap
import itertools


WIDTH = 80
CAT = "                                 |\         /|\n" + \
"                                 | \       / |\n" + \
"                                 \  ~-~-~-~  )\n" + \
"              LONGCAT            (           )\n\n" + \
"                    IS           (  O    O   )\n\n" + \
"                     LOOOOOOONG! (           )\n" + \
"                                  \ == o == /\n" + \
"                             -----------_____-\n" + \
"                            (                 )\n" + \
"               -----___      ---------____    )\n" + \
"              (        \-----------           )\n" + \
"               ------                          )\n" + \
"                     \------------              \\\n" + \
"                              /                  \\\n" + \
"                             /                    \\\n" + \
"                            /                      \\\n" + \
"                           /                        \\\n" + \
"                          /                          \\\n" + \
"                         /                            \\\n" + \
"                        /                              \\\n" + \
"                       /                                \\\n" + \
"                      /                                  \\\n" + \
"                     /                                    \\\n" + \
"                    /                                      \\\n" + \
"                   /        A PROJECT                       \\\n" + \
"                  /                                          \\\n" + \
"                 /                   BY                       \\\n" + \
"                /                                              \\\n" + \
"               /                                                \\\n" + \
"              /                ~~ C0REDUMP RAPPERSWIL ~~         \\\n" + \
"             /                                                    \\\n" + \
"            /                                                      \\\n" + \
"           /                                                        \\\n" + \
"          /                                                          \\\n" + \
"         /                                                            \\\n" + \
"        /                                                              \\\n" + \
"       /                                                                \\\n" + \
"      /                                                                  \\\n" + \
"     /                                                                    \\\n" + \
"    /        Visit http://152.96.159.x/ on your smartphone to send text.   \\\n" + \
"   /                                                                        \\\n" + \
"  /                                                                          \\\n" + \
" /                                                                            \\\n" + \
"#                                                                              #\n" + \
"|                                                                              |\n" + \
"#                                                                              #"

class Escape(object):
    esc = chr(27)
    italic_start = esc + b'4'
    italic_end = esc + b'5'


class LX300(object):

    def __init__(self, port='/dev/ttyS0', baudrate=19200):
        """Initialize printer."""
        self.side = itertools.cycle(['|', '#'])
        self._print_header()

    def _print_header(self):
        """Print the header cat."""
        print(CAT)

    def _write_line(self, line):
        """Write a single line to the printer."""
        kwargs = {
            'side': self.side.next(),
            'text': line.ljust(WIDTH - 4),
        }
        print(self._encode('{side} {text} {side}'.format(**kwargs)))

    def _encode(self, text):
        """Encode the unicode string with CP850 encoding. Replace unconvertable chars."""
        return text.encode('cp850', 'replace').decode('cp850').encode('utf8')

    def write(self, text):
        """Write the specified text into the cat."""
        lines = filter(None, text.split('\r\n'))
        for line in lines:
            for l in textwrap.wrap(line, WIDTH - 4):
                self._write_line(l)
        self._write_line('')
