# More indentation included to distinguish this from the rest.
def server(
        host='localhost', port=443, secure=True,
        username='admin', password='admin'):
    return locals()


# Aligned with opening delimiter.
connection = server(host='localhost', port=443, secure=True,
                    username='admin', password='admin')

# Hanging indents should add a level.
connection = server(
    host='localhost', port=443, secure=True,
    username='admin', password='admin')

# The best
connection = server(
    host='localhost',
    username='admin',
    password='admin',
    port=443,
    secure=True,
)
