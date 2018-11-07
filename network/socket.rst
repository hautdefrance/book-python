******
Socket
******


``socket``
==========

Protokoły
---------
* IPv4 - ``socket.AF_INET``
* IPv6 - ``socket.AF_INET6``
* UDP - ``socket.SOCK_DGRAM``
* TCP - ``socket.SOCK_STREAM``
* Broadcast - ``socket.SO_BROADCAST``

Otwieranie połączeń
-------------------
.. literalinclude:: src/socket-communication.py
    :name: listing-socket-communication
    :language: python
    :caption: Komunikacja za pomocą socketów

Nasłuchiwanie
-------------
.. code-block:: python

    import socket

    HOST = '127.0.0.1'
    PORT = 1337

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, world')
        data = s.recv(1024)

    output = data.encode('utf-8')
    print(output)

Przekazywanie informacji
------------------------
.. code-block:: python

    import socket

    HOST = '127.0.0.1'
    PORT = 1337

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()

        with conn:
            while True:
                data = conn.recv(1024)

                if not data:
                    break

                conn.sendall(data)


``socketserver``
================

Server
------
.. code-block:: python

    import socketserver


    class MyTCPHandler(socketserver.BaseRequestHandler):
        def handle(self):
            data = self.request.recv(1024).strip()
            addr = self.client_address[0])

            print(f"From: {addr}, received: {data}"

            # just send back the same data, but upper-cased
            response = data.upper()
            self.request.sendall(response)


    if __name__ == "__main__":
        HOST, PORT = "localhost", 9999

        with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
            # Activate the server; this will keep running until you
            # interrupt the program with Ctrl-C
            server.serve_forever()

Client
------
.. code-block:: python

    import socket
    import sys

    HOST, PORT = "localhost", 9999
    data = "Hello World"


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))

        data = bytes(f'{data}\n', "utf-8")
        sock.sendall(data)

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")


    print(f"Sent:     {data}")
    print(f"Received: {received}")

Asynchronous
------------
.. code-block:: python

    import socket
    import threading
    import socketserver


    class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
        def handle(self):
            data = str(self.request.recv(1024), 'ascii')
            cur_thread = threading.current_thread()
            response = bytes(f"{cur_thread.name}: {data}", 'ascii')
            self.request.sendall(response)


    class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
        pass


    def client(ip, port, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((ip, port))
            sock.sendall(bytes(message, 'ascii'))
            response = str(sock.recv(1024), 'ascii')
            print(f"Received: {response}")


    if __name__ == "__main__":
        # Port 0 means to select an arbitrary unused port
        HOST, PORT = "localhost", 0

        with ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler) as server:
            ip, port = server.server_address

            # Start a thread with the server -- that thread will then start one
            # more thread for each request
            server_thread = threading.Thread(target=server.serve_forever)

            # Exit the server thread when the main thread terminates
            server_thread.daemon = True
            server_thread.start()
            print(f"Server loop running in thread: {server_thread.name}")

            client(ip, port, "Hello World 1")
            client(ip, port, "Hello World 2")
            client(ip, port, "Hello World 3")

            server.shutdown()



Allegro Ralph
=============
* http://allegro.tech/ralph/
* https://github.com/allegro/ralph

Ralph is full-featured Asset Management, DCIM and CMDB system for data center and back office.

Features:

- keep track of assets purchases and their life cycle
- generate flexible and accurate cost reports
- integrate with change management process using JIRA integration

It is an Open Source project provided on Apache v2.0 License.

Live demo:

- http://ralph-demo.allegro.tech/
- login: ralph
- password: ralph

