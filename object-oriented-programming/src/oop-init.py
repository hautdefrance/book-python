class Server:
    def __init__(self, host, user, password=None):
        self.host = host
        self.user = user
        self.password = password


connection = Server(
    host='localhost',
    user='admin',
    password='admin'
)

connection.__dict__
# {'host': 'localhost', 'user': 'admin', 'password': 'admin'}
