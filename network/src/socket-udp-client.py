import socket


HOST = '127.0.0.1'
PORT = 1337
DATA = 'Hello World'


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    print(f'Connecting to {HOST}:{PORT}/UDP')
    sock.connect((HOST, PORT))

    print(f'Sending: "{DATA}"')
    sock.sendall(bytes(DATA, encoding='utf-8'))

    received = str(sock.recv(1024), encoding='utf-8')
    print(f'Received: {received}')
