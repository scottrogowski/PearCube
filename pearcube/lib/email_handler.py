import json

import sendgrid
from validate_email import validate_email
from flask import render_template
import premailer

from lib.options import options
from lib.secrets import SENDGRID_USERNAME, SENDGRID_PASSWORD

PRODUCT_FINDER_EMAIL = 'finder@pearcube.com'
MY_EMAIL = 'scott@pearcube.com'

sg_singleton = sendgrid.SendGridClient(SENDGRID_USERNAME, SENDGRID_PASSWORD)

def send_request_email(form):
    their_email = form.get('email_address','')
    what_they_wrote = form.get('body', '')

    if not validate_email(their_email):
        return "INVALID_EMAIL", 400

    if not what_they_wrote:
        return "INVALID_BODY", 400

    confirmation_body = render_template("confirmation_email_plain.html",
                                        their_email=their_email,
                                        what_they_wrote=what_they_wrote)
    confirmation_body = premailer.transform(confirmation_body) # makes styles inline

    kargs = {'from_email': PRODUCT_FINDER_EMAIL,
             'subject': 'PearCube product finder',
             'html': confirmation_body}
    msg_for_me = sendgrid.Mail(
        to = MY_EMAIL,
        reply_to = their_email,
        **kargs)

    if options.LIVE_EMAILING:
        status, res = sg_singleton.send(msg_for_me)
        res = json.loads(res)
        # successful sendgrid responses look like
        # {"message": "success"}
        # they don't validate emails before returning
        # also, they return res as a string... which is weird
        return json.dumps(res), status
    else:
        return json.dumps({'confirmation_body': confirmation_body}), 200

def send_results_email():
    html = render_template("email.html")
    html = premailer.transform(html)
    title = "Best Cheap Flat Screen Television"
    # to_email = 'irisha.malkova@gmail.com'
    to_email = 'scottmrogowski@gmail.com'


    msg = sendgrid.Mail(
        from_email = PRODUCT_FINDER_EMAIL,
        reply_to = "scottmrogowski@gmail.com",
        to = to_email,
        subject = 'PearCube - %s' % title,
        html = html)

    if options.LIVE_EMAILING:
        status, msg = sg_singleton.send(msg)
        msg += to_email
        return msg, status
    else:
        return "Live emailing is off"
