# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from flask import Flask, render_template, request, redirect

import test300


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/print', methods=['POST'])
def print():
    text = request.form['text']
    app.printer.write(text)
    return redirect('/')


if __name__ == '__main__':
    app.debug = True
    app.printer = test300.LX300()
    app.run()
