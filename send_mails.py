# send_emails.py

import email, smtplib, ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    "-t",
    "--title",
    type=str,
    default="",
    help="enter the subject of the email"
)
parser.add_argument(
    "-s",
    "--sender",
    type=str,
    default="",
    help="enter one email sender adress"
)
parser.add_argument(
    "-r",
    "--recipient",
    # metavar="Emails",
    type=str,
    default="",
    help="enter one or more website email adresses",
)
parser.add_argument(
    "-b",
    "--body",
    type=str,
    default="",
    help="enter the relative path to the html file for the email body"
)
parser.add_argument(
    "-a",
    "--attachment",
    type=str,
    default="",
    help="enter the relative path to the file to be attached"
)
args = parser.parse_args()

try:
    subject = args.title
    sender = args.sender
    recipient = args.recipient 
    body = args.body
    attachment = args.attachment
    if not recipient:
        raise ValueError("Please enter the recipient's address!")
except ValueError as e:
    print(e)

message = MIMEMultipart()
message['Subject'] = subject
message['From'] = sender
message['To'] = recipient

try:
    with open(body, 'r', encoding='utf-8') as file:
        message.attach(MIMEText(file.read(), 'html'))
except FileNotFoundError:
    print("File for email's body not found!")

# Alternatively to 'with open()', you can use codecs:
# import codecs
# file = codecs.open(body, "r", "utf-8")
# message.attach(MIMEText(file.read(), 'html'))

try:
    with open(attachment, 'rb') as file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename={attachment}'
        )
        message.attach(part)
except FileNotFoundError:
    print("Attachment file not found!")

smtp_server = 'localhost'
port = 25
text = message.as_string()
context = ssl._create_unverified_context()

try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.sendmail(sender, recipient, text)
except Exception as e:
    print(e)

