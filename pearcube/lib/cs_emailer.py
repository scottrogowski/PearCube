import json

import sendgrid
from validate_email import validate_email
from flask import render_template
import premailer

from lib.options import options
from lib.secrets import SENDGRID_USERNAME, SENDGRID_PASSWORD

sg_singleton = sendgrid.SendGridClient(SENDGRID_USERNAME, SENDGRID_PASSWORD)

def send_request_email(form):
    email = form.get('email_address','')
    body = form.get('body', '')
    if not validate_email(email):
        return "INVALID_EMAIL", 400

    if not body:
        return "INVALID_BODY", 400

    msg = sendgrid.Mail(
        from_email = email,
        to = 'scottmrogowski@gmail.com',
        subject = 'PearCube product finder',
        text = body)

    if options.LIVE_EMAILING:
        status, msg = sg_singleton.send(msg)
        return json.dumps(msg), status

    return ','.join([email, body]), 200

def send_results_email():
    html = render_template("email.html")
    html = premailer.transform(html)

    msg = sendgrid.Mail(
        from_email = "scottmrogowski@gmail.com",
        to = 'michaelagcordes@yahoo.com',
        subject = 'PearCube - Small & Portable Photo Scanner',
        html = html)

    if options.LIVE_EMAILING:
        status, msg = sg_singleton.send(msg)
        return msg, status

    return html, 200