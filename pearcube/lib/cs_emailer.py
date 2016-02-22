import sendgrid
from validate_email import validate_email

from lib.options import options
from lib.secrets import SENDGRID_USERNAME, SENDGRID_PASSWORD

sg_singleton = sendgrid.SendGridClient(SENDGRID_USERNAME, SENDGRID_PASSWORD)

def cs_emailer(form):
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
