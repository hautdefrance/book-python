class Server:

    def __init__(self, host, user, password=None):
        self.host = host
        self.user = user
        self.password = password
        self.login()  # You should not do this way

    def login(self):
        print('Logging...')


localhost = Server(
    host='localhost',
    user='admin',
    password='admin'
)

# to jest poprawne wywołanie
localhost.login()
