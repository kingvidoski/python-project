from email.message import EmailMessage
import ssl
import smtplib
from os import environ as env

from dotenv import load_dotenv
load_dotenv()


print('Initializing')

email_sender = 'kingvidoski@gmail.com'
email_password = env['EMAIL_PASSWORD']

email_receiver = 'kingvidoski@gmail.com'

subject = "Coding with kingsley"
body = """
I am a software developer and
I am open to new roles
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

print('Sent mail')
