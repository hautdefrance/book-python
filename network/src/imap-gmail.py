import getpass
import imaplib
import email
from pprint import pprint
from quopri import decodestring
from datetime import datetime

USERNAME = getpass.getuser()
PASSWORD = getpass.getpass()
HOST = 'imap.gmail.com'
PORT = 993

imap = imaplib.IMAP4_SSL(HOST, PORT)
imap.login(USERNAME, PASSWORD)
imap.select('INBOX')


def get_str(text):
    return decodestring(text).decode()


def get_date(text):
    try:
        return datetime.strptime(headers['Date'], '%a, %d %b %Y %H:%M:%S %z')
    except ValueError:
        return text


def get_body(msg):
    type = msg.get_content_maintype()

    if type == 'multipart':
        for part in msg.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload(decode=True).decode('utf-8')

    elif type == 'text':
        return msg.get_payload(decode=True).decode('utf-8')


status, data = imap.search(None, 'ALL')
# status: OK
# data: [b'1 2 3 4 ...']

for num in data[0].split():
    status, data = imap.fetch(num, '(RFC822)')
    mail = email.message_from_string(data[0][1].decode())
    headers = dict(mail._headers)
    mail = {
        'to': get_str(headers['To']),
        'sender': get_str(headers['From']),
        'subject': get_str(headers['Subject']),
        'date': get_date(headers['Date']),
        'body': get_body(mail)
    }
    pprint(mail)

imap.close()
imap.logout()
