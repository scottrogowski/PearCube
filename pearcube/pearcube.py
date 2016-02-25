#!/usr/bin/env python

from flask import Flask, request, render_template

from lib.options import options
from lib.cs_emailer import cs_emailer


app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/Example-Emails/Small-Cheap-Photo-Scanner')
def email():
    return render_template('product_landing.html')

@app.route('/cs_request', methods=['POST'])
def cs_request():
    return cs_emailer(request.form)

if __name__ == '__main__':
    options.parse_command_line()

    app.run(debug = options.DEBUG,
            host = options.HOST,
            port = options.PORT)
