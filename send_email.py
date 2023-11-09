from email.message import EmailMessage
import ssl
import smtplib


email_sender = 'senders_email'
email_password = 'email_password'

email_receiver = 'senders email goes here'

subject = 'The subject of the message goes here'
body = """Enter teh body of the message"""


em = EmailMessage()
em['from'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
