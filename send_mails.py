# import smtplib
# from email.message import EmailMessage
# 
# msg = EmailMessage()
# msg['From'] = 'localhost' 
# msg['To'] = 'otte@ub.uni-heidelberg.de'
# msg['Subject'] = 'Telefonliste'
# 
# body = 'Anbei die aktuelle Telefonliste'
# msg.set_content(body)
# 
# with open('telefonliste.pdf', 'rb') as content_file:
#    content = content_file.read()
#    msg.add_attachment(content, maintype='application', subtype='txt', filename='telefonliste.pdf')
# 
# with smtplib.SMTP('localhost') as s:
#    s.send_message(msg)

import email, smtplib, ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

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
#body = "This is an email with attachment sent from Python"
sender = 'otte@ub.uni-heidelberg.de'
receiver = 'otte@ub.uni-heidelberg.de'

message = MIMEMultipart()
message['Subject'] = 'Test mail'
message['From'] = 'localhost@pers31.ub.uni-heidelberg.de'
message['To'] = 'otte@ub.uni-heidelberg.de'

message.attach(MIMEText(html, 'html'))
#message.attach(MIMEText(body, 'plain'))

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
      server.sendmail(sender, receiver, text)
except Exception as e:
   print(e)
# text = """\
# Hi,
# How are you?
# Real Python has many great tutorials:
# www.realpython.com"""
# html = """\
# <html>
#   <body>
#     <p>Hi,<br>
#        How are you?<br>
#        <a href="http://www.realpython.com">Real Python</a> 
#        has many great tutorials.
#     </p>
#   </body>
# </html>
# """
# 
# # Turn these into plain/html MIMEText objects
# part1 = MIMEText(text, "plain")
# part2 = MIMEText(html, "html")
# 
# # Add HTML/plain-text parts to MIMEMultipart message
# # The email client will try to render the last part first
# message.attach(part1)
# message.attach(part2)
# 
# #context = ssl.create_default_context()
# context = ssl._create_unverified_context()
# try:
#    with smtplib.SMTP(smtp_server, port) as server:
#       server.ehlo()
#       server.starttls(context=context)
#       server.sendmail(sender, receiver, message.as_string())
# except Exception as e:
#    print(e)

# try:
#    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#       server.noop()
#       #server.login(sender, password)
#       #server.sendmail(sender, receiver, message)
# except Exception as e:
#    print(e)
