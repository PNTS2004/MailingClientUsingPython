import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from dotenv import load_dotenv
import os

load_dotenv("credentials.env")

email_address = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")
toaddr = os.getenv("TOADDR")

msg=MIMEMultipart()
msg['FROM']='Pooja Nokhwal'
msg['TO']='Pooja Nokhwal'
msg['SUBJECT']='Testing the mail client'

with open('message.txt','r') as f:
    message=f.read()

msg.attach(MIMEText(message, 'plain'))

#you can write:- text=msg.as_string() and then in s.sendmail, replace msg.as_string() with just: text
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as s:
    s.login(email_address, password)
    s.sendmail(email_address, toaddr, msg.as_string())