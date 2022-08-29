# send_emails.py

import email, smtplib, ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

from argparse import ArgumentParser

parser = ArgumentParser()
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
   metavar="Emails",
   type=str,
   default="",
   help="enter one or more website email adresses",
)
args = parser.parse_args()

smtp_server = 'localhost'
port = 25

html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

subject = "Subject"
sender = args.sender
recipient = args.recipient 

message = MIMEMultipart()
message['Subject'] = 'Test mail'
message['From'] = args.sender
message['To'] = args.recipient  # 'otte@ub.uni-heidelberg.de'

message.attach(MIMEText(html, 'html'))

filename = 'telefonliste.pdf'

with open(filename, 'rb') as attachment:
   part = MIMEBase('application', 'octet-stream')
   part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add_header(
   'Content-Disposition',
   f'attachment; filename={filename}'
)

message.attach(part)
text = message.as_string()

context = ssl._create_unverified_context()
try:
   with smtplib.SMTP(smtp_server, port) as server:
      server.ehlo()
      server.starttls(context=context)
      server.sendmail(sender, recipient, text)
except Exception as e:
   print(e)

