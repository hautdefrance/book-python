import socketserver

class UDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        log.info('Received ping from %s:%s' % self.client_address)


if __name__ == '__main__':
    addr = ('localhost', 1234)

    logging.info('Listening for pings on %s...', addr)
    listener = socketserver.UDPServer(addr, UDPHandler)

    listener.serve_forever()