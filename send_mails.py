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

smtp_server = 'localhost'
port = 25

sender = 'otte@ub.uni-heidelberg.de'
receiver = 'otte@ub.uni-heidelberg.de'
#message = 'Hi There!'

message = MIMEText('This is a test mail')
message['Subject'] = 'Test mail'
message['From'] = 'admin@example.com'
message['To'] = 'otte@ub.uni-heidelberg.de'

try:
   with smtplib.SMTP(smtp_server, port) as server:
      server.sendmail(sender, receiver, message.as_string())
except Exception as e:
   print(e)

# context = ssl.create_default_context()
# try:
#    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#       server.noop()
#       #server.login(sender, password)
#       #server.sendmail(sender, receiver, message)
# except Exception as e:
#    print(e)
