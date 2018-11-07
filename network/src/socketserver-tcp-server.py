from socketserver import BaseRequestHandler, TCPServer


HOST = '127.0.0.1'
PORT = 1337


class MyHandler(BaseRequestHandler):

    def handle(self):
        host, port = self.client_address
        data = self.request.recv(1024)
        print(f'From: {host}:{port}/TCP, received: "{data.decode()}"')

        response = 'Thanks'
        self.request.sendall(response.encode())


if __name__ == '__main__':

    with TCPServer((HOST, PORT), MyHandler) as server:

        print(f'Accepting connections on {HOST}:{PORT}/TCP...')
        print(f'To stop the server use ``Ctrl-C``\n')

        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print('Server closing... ', end='')
            server.server_close()
            print('Done.')
