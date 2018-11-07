import getpass
import imaplib

HOST = 'imap.gmail.com'
PORT = 993
USERNAME = getpass.getuser()

# Gmail requires to generate One-Time App Password
# https://security.google.com/settings/security/apppasswords
PASSWORD = getpass.getpass()

imap = imaplib.IMAP4_SSL(HOST, PORT)
imap.login(USERNAME, PASSWORD)
imap.select('INBOX')

typ, data = imap.search(None, 'ALL')

for num in data[0].split():
    typ, data = imap.fetch(num, '(RFC822)')
    data = data[0][1]

    print(f'Message: {num}')
    print(f'Data: {data}')
    print('-' * 30)

imap.close()
imap.logout()
