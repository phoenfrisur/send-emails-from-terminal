import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['From'] = 'localhost' 
msg['To'] = 'otte@ub.uni-heidelberg.de'
msg['Subject'] = 'Telefonliste'

body = 'Anbei die aktuelle Telefonliste'
msg.set_content(body)

with open('telefonliste.pdf', 'rb') as content_file:
   content = content_file.read()
   msg.add_attachment(content, maintype='application', subtype='txt', filename='telefonliste.pdf')

with smtplib.SMTP('localhost') as s:
   s.send_message(msg)
