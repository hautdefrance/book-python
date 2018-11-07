import socket


HOST = '127.0.0.1'
PORT = 1337
RESPONSE = 'Thanks'



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

    print(f'Listening on {HOST}:{PORT}/TCP...')
    sock.bind((HOST, PORT))
    sock.listen(1)

    while True:
        conn, addr = sock.accept()

        received = conn.recv(1024).decode()
        print(f'From: {addr}, received: "{received}"')

        # Reply to client
        conn.sendall(RESPONSE.encode())

        if not received:
            print(f'Client {addr} disconnected.')
            conn.close()
