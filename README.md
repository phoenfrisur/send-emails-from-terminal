# Sending Emails with Python from Terminal

This is a simple python script for sending email messages from the terminal. You can configure the subject, the sender's and recipient's email addresses as command line arguments. The email body and potential attachments are added by specifying their relative paths.

## Installation

```bash
$ git clone git@github.com:pentaquarks/send-emails.git
$ cd send-emails
$ pip install -r requirements.txt
```

## Usage

```bash
$ python send_mails.py -t '<subject>' -s '<sender email>' -r '<recipients email>' -b '<path/to/body>' -a '<path/to/attachment>'
```
