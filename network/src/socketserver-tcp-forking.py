import socket
import threading
from socketserver import ForkingTCPServer, BaseRequestHandler


HOST = '127.0.0.1'
PORT = 1337


class MyHandler(BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).decode()
        thread = threading.current_thread()
        response = f'{thread.name}: {data}'
        self.request.sendall(response.encode())


def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(message.encode())
        response = sock.recv(1024).decode()
        print(f'Received: {response}')


if __name__ == '__main__':
    
    with ForkingTCPServer((HOST, PORT), MyHandler) as server:
        ip, port = server.server_address

        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        server_thread = threading.Thread(target=server.serve_forever)

        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()
        print(f'Server loop running in thread: {server_thread.name}')

        client(ip, port, 'Hello World 1')
        client(ip, port, 'Hello World 2')
        client(ip, port, 'Hello World 3')

        server.shutdown()

