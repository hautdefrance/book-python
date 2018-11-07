****
POP3
****


Connection
==========
* If port is not specified, the standard POP3 port (110)
* If port is not specified, 995, the standard POP3-over-SSL port is used


Methods
=======
.. csv-table:: ``poplib`` Methods
    :header-rows: 1

    "Method", "Arguments", "Description"
    "``poplib.POP3()``", "``host``, ``port=POP3_PORT``, ``timeout=None``", "This class implements the actual POP3 protocol"
    "``poplib.POP3_SSL()``", "``host``, ``port=POP3_SSL_PORT``, ``keyfile=None``, ``certfile=None``, ``timeout=None``, ``context=None``", "This is a subclass of POP3 that connects to the server over an SSL encrypted socket"
    "``POP3.user()``", "``username``", "Send user command, response should indicate that a password is required"
    "``POP3.pass_()``", "``password``", "Send password, response includes message count and mailbox size"
    "``POP3.apop()``", "``user``, ``secret``", "Use the more secure APOP authentication to log into the POP3 server"
    "``POP3.stat()``", "", "Get mailbox status. The result is a tuple of 2 integers: (message count, mailbox size)"
    "``POP3.list()``", "``which=None``", "Request message list, result is in the form ``(response, ['mesg_num octets', ...], octets)``"
    "``POP3.retr()``", "``which``", "Retrieve whole message number which, and set its seen flag. Result is in form ``(response, ['line', ...], octets)``"
    "``POP3.dele()``", "``which``", "Flag message number which for deletion"
    "``POP3.rset()``", "", "Remove any deletion marks for the mailbox"
    "``POP3.quit()``", "", "Signoff: commit changes, unlock mailbox, drop connection"
    "``POP3.top()``", "``which``, ``howmuch``", "Retrieves the message header plus howmuch lines of the message after the header of message number which"
    "``POP3.utf8()``", "", "Try to switch to UTF-8 mode. Returns the server response if successful, raises error_proto if not"
    "``POP3.stls()``", "``context=None``", "Start a TLS session on the active connection as specified in RFC 2595. This is only allowed before user authentication"


Example
=======
.. code-block:: python

    import getpass
    import poplib


    USERNAME = getpass.getuser()
    PASSWORD = getpass.getpass()
    HOSTNAME = 'localhost'
    PORT = poplib.POP3_SSL_PORT

    server = poplib.POP3_SSL(host=HOSTNAME, port=PORT, timeout=30)
    server.user(USERNAME)
    server.pass_(PASSWORD)


    numMessages = len(server.list()[1])

    for i in range(numMessages):
        for j in server.retr(i + 1)[1]:
            print(j)
