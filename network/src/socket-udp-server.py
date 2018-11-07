import socket


HOST = '127.0.0.1'
PORT = 1337


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:

    print(f'Listening on {HOST}:{PORT}/UDP...')
    sock.bind((HOST, PORT))

    while True:
        received, addr = sock.recvfrom(1024)
        received = str(received, encoding='utf-8')

        print(f'From: {addr}, received: "{received}"')
