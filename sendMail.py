import sendgrid
import os
from sendgrid.helpers.mail import *


TEMPLATE_ID = "d-05e7f447a81e4943a543832c73473e75"
sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("eavina@mit.edu")

def sendMailTo(emailAddr):
    to_email = To(emailAddr)
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, to_email)
    
    mail.dynamic_template_data = {}
    mail.template_id = TEMPLATE_ID

    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


try:
    sendMailTo("rickyavina@icloud.com")
except Exception as e:
    print(e)
