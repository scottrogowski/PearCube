#!/usr/bin/env python

import sys

from flask import Flask, request, render_template
import sendgrid

SENDGRID_USERNAME = 'app47702827@heroku.com'
SENDGRID_PASSWORD = '7f2b7fc48527'

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/Example-Emails/Small-Cheap-Photo-Scanner')
def email():
    return render_template('email.html')

@app.route('/cs_request', methods=['POST'])
def cs_request():
    sg = sendgrid.SendGridClient(SENDGRID_USERNAME, SENDGRID_PASSWORD)

    message = sendgrid.Mail()
    message.add_to('scottmrogowski@gmail.com')
    message.set_subject('test2')
    message.set_text('Body')
    message.set_from('scott@pearcube.com')
    status, msg = sg.send(message)

    return ','.join(["POST", request.form.get('body',''), request.form.get('email_address',''), str(status), str(message)])

if __name__ == '__main__':
    kwargs = {}

    if '--debug' in sys.argv:
        kwargs['debug'] = True
    else:
        kwargs['host'] = '0.0.0.0'

    if '--port' in sys.argv:
        kwargs['port'] = sys.argv[sys.argv.index('--port') + 1]

    app.run(**kwargs)
