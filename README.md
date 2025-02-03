# Sending Emails with Python from Terminal

This is a simple python script for sending email messages from the terminal. You can configure the subject, the sender's and recipient's email addresses as command line arguments. The email body and potential attachments are added by specifying their relative paths.

## Installation

```bash
$ git clone git@github.com:pentaquarx/send-emails-from-terminal.git
$ cd send-emails-from-terminal
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Usage

```bash
$ python send_mails.py -t 'My subject' -s '<sender’s email>' -r '<recipient’s email>' -b 'body.html' -a '<optional: path/to/attachment>'
```
