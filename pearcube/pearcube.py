#!/usr/bin/env python

import sys

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/Example-Emails/Small-Cheap-Photo-Scanner')
def email():
    return render_template('email.html')

# @app.route('/cs_request', method='POST')
# def cs_request():
#     request.form['text']
#     request.form['email']

if __name__ == '__main__':
    if '--debug' in sys.argv:
        kwargs = {'debug': True}
    else:
        kwargs = {'host':'0.0.0.0'}
    app.run(**kwargs)
