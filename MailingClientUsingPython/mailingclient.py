import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os

load_dotenv("credentials.env")

email_address = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")
toaddr = os.getenv("TOADDR")

if not all([email_address, password, toaddr]):
    print("Error: Email credentials are missing.")
    exit()

msg=MIMEMultipart()
msg['FROM']='SENDER'
msg['TO']='RECIEVER'
msg['SUBJECT']='SUBJECT OF THE MAIL'

with open('message.txt','r') as f:
    message=f.read()

image='mention the path'
with open(image, 'rb') as attach_image:
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attach_image.read())

    encoders.encode_base64(p)
    p.add_header('Content-Disposition', f'attachment; filename={image}')

msg.attach(MIMEText(message, 'plain'))
msg.attach(p)

#you can write:- text=msg.as_string() and then in s.sendmail, replace msg.as_string() with just: text
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as s:
    s.login(email_address, password)
    s.sendmail(email_address, toaddr, msg.as_string())
