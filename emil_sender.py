import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'name'
email['to'] = 'to email id'
email['subject'] = 'you won 1M dollor'

email.set_content(html.substitute({'name': 'tom'}), 'html')

with smtplib.SMTP(host='', port=00) as smtp: #set your host and port
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your emil id', 'pw')
    smtp.send_message(email)
    print('done')