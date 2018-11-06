*************
IMAP Protocol
*************


Connection
==========
* ``imaplib.IMAP4(host, port)``, If port is omitted, the standard IMAP4 port (143) is used.
* ``imaplib.IMAP4_SSL(host, port)``, if port is omitted, the standard IMAP4-over-SSL port (993)


Methods
=======
.. csv-table:: python
    :header-rows: 1

    "Method", "Description"
    "``IMAP4.append(mailbox, flags, date_time, message)``", "Append message to named mailbox"
    "``IMAP4.check()``", "Checkpoint mailbox on server"
    "``IMAP4.close()``", "Close currently selected mailbox"
    "``IMAP4.copy(message_set, new_mailbox)``", "Copy message_set messages onto end of new_mailbox"
    "``IMAP4.create(name)``", "Create new mailbox"
    "``IMAP4.delete(name)``", "Delete mailbox "
    "``IMAP4.expunge()``", "Permanently remove deleted items from selected mailbox"
    "``IMAP4.fetch(message_set, message_parts)``", "Fetch (parts of) messages. ``message_parts`` should be a string of message part names enclosed within parentheses, eg: ``(UID BODY[TEXT])``"
    "``IMAP4.list([directory[, pattern]])``", "List mailbox names in directory matching pattern"
    "``IMAP4.login(user, password)``", "Identify the client using a plaintext password"
    "``IMAP4.logout()``", "Shutdown connection to server"
    "``IMAP4.recent()``", "Prompt server for an update"
    "``IMAP4.rename(oldmailbox, newmailbox)``", "Rename mailbox named oldmailbox to newmailbox"
    "``IMAP4.search(charset, criterion[, ...])``", "Search mailbox for matching messages. ``charset`` may be None, in which case no CHARSET will be specified in the request to the server."
    "``IMAP4.select([mailbox[, readonly]])``", "Select a mailbox. The default mailbox is ``INBOX``. If the readonly flag is set, modifications to the mailbox are not allowed"


Usage
=====
.. code-block:: python

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

Case Study
==========
.. code-block:: python

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
