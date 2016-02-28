#!/usr/bin/env python

from flask import Flask, request, render_template
import premailer

from lib.options import options
from lib.cs_emailer import send_request_email, send_results_email

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/Portable-And-Cheap-Photo-Scanner')
def email():
    return render_template('product_landing.html')

@app.route('/cs_request', methods=['POST'])
def cs_request():
    return send_request_email(request.form)

@app.route('/debug_email', methods=['GET'])
def debug_email():
	if options.DEBUG:
		html = render_template('email.html')
		# html = premailer.transform(html)
		return html

@app.route('/send_debug_email', methods=['GET'])
def send_debug_email():
	if options.DEBUG:
		return send_results_email()

if __name__ == '__main__':
    options.parse_command_line()

    app.run(debug = options.DEBUG,
            host = options.HOST,
            port = options.PORT)
