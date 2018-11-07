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
