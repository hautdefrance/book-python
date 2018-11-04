class Server:

    def __init__(self, host, username, password=None):
        self.host = host
        self.username = username
        self.password = password
        self.connect()    # Better ask user to ``connect()`` explicitly

    def connect(self):
        print(f'Logging to {self.host} using: {self.username}:{self.password}')


localhost = Server(
    host='localhost',
    username='admin',
    password='admin'
)

# This is better
localhost.connect()
