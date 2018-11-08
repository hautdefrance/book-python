import socket
import json
import logging
from pprint import pprint


HOST = "localhost"
PORT = 1337
XML_CMD_FILE = 'botnet-commands.xml'


logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime).19s] %(levelname)s (%(name)s) %(message)s')
log = logging.getLogger('botnet.atacker.client')


with open(XML_CMD_FILE) as file:
    commands = file.read()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

    log.debug(f'Connecting to {HOST}:{PORT}')
    sock.connect((HOST, PORT))
    sock.settimeout(7.0)
    sock.sendall(commands.encode())

    log.debug('Receive data from the server and shut down')
    received = str(sock.recv(1024), 'utf-8')
    output = json.loads(received)


print(f'Sent:     {commands}')
print(f'Received: {output}')
print('\n\n')

for executed in output:
    pprint(executed)
