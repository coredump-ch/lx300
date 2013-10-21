Epson LX300 Twitterstream
=========================

This project prints a twitterstream on an LX300+ dot matrix
printer.

Files
-----

- `lx300.py`: Contains wrapper for sending stuff to printer.
- `test.py`: Starts a very simple terminal to write stuff directly to printer.
- `twitterstream.py`: Writes mentions and tweets from twitter to printer.

Usage
-----

To start a terminal to write directly to the printer, use:

    python test.py

To print all tweets by the twitter user `coredump_ch`, use:

    export CONSUMER_KEY='your_consumer_key'
    export ACCESS_KEY='your_access_key'

    python twitter.py coredump_ch

If you want to store the access credentials that are printed on the terminal
after the first login, set the `ACCESS_KEY` and `ACCESS_SECRET` env variables.

License
-------

GPLv3
