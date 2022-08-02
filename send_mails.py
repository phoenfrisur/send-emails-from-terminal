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

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = 'localhost'
port = 25

sender = 'otte@ub.uni-heidelberg.de'
receiver = 'otte@ub.uni-heidelberg.de'
#message = 'Hi There!'

message = MIMEMultipart('alternative')
message['Subject'] = 'Test mail'
message['From'] = 'localhost@pers31.ub.uni-heidelberg.de'
message['To'] = 'otte@ub.uni-heidelberg.de'

text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
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

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

#context = ssl.create_default_context()
context = ssl._create_unverified_context()
try:
   with smtplib.SMTP(smtp_server, port) as server:
      server.ehlo()
      server.starttls(context=context)
      server.sendmail(sender, receiver, message.as_string())
except Exception as e:
   print(e)

# try:
#    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#       server.noop()
#       #server.login(sender, password)
#       #server.sendmail(sender, receiver, message)
# except Exception as e:
#    print(e)
