import csv


FIELDNAMES = ['username', 'password', 'uid', 'gid', 'full_name', 'home', 'shell']
"""
root:x:0:0:root:/root:/bin/bash
watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash
jimenez:x:1001:1001:José Jiménez:/home/jimenez:/bin/bash
ivanovic:x:1002:1002:Иван Иванович:/home/ivanovic:/bin/bash
"""


with open(r'etc-passwd.txt') as file:
    content = csv.DictReader(file, fieldnames=FIELDNAMES, delimiter=':')

    for row in content:
        print(dict(row))

# {'username': 'root', 'password': 'x', 'uid': '0',...}
# {'username': 'bin', 'password': 'x', 'uid': '1',...}
# {'username': 'daemon', 'password': 'x', 'uid': '2',...}
# {'username': 'adm', 'password': 'x', 'uid': '3',...}
# {'username': 'shutdown', 'password': 'x', 'uid': '6',...}
# {'username': 'halt', 'password': 'x', 'uid': '7',...}
# {'username': 'nobody', 'password': 'x', 'uid': '99',...}
# {'username': 'sshd', 'password': 'x', 'uid': '74',...}
# {'username': 'peck', 'password': 'x', 'uid': '1000',...}
# {'username': 'jimenez', 'password': 'x', 'uid': '1001',...}
# {'username': 'ivanovic', 'password': 'x', 'uid': '1002',...}
