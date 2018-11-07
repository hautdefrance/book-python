from socketserver import BaseRequestHandler, UDPServer


HOST = '127.0.0.1'
PORT = 1337


class MyHandler(BaseRequestHandler):

    def handle(self):
        host, port = self.client_address
        data, socket = self.request

        print(f'From: {host}:{port}/TCP, received: "{data.decode()}"')

        response = 'Thanks'
        socket.sendto(response.encode(), self.client_address)


if __name__ == '__main__':

    with UDPServer((HOST, PORT), MyHandler) as server:

        print(f'Accepting connections on {HOST}:{PORT}/UDP...')
        print(f'To stop the server use ``Ctrl-C``\n')

        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print('Server closing... ', end='')
            server.server_close()
            print('Done.')

