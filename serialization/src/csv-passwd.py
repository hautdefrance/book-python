import csv

FILENAME = r'etc-passwd.txt'
"""
root:x:0:0:root:/root:/bin/bash
watney:x:1000:1000:Mark Watney:/home/watney:/bin/bash
jimenez:x:1001:1001:José Jiménez:/home/jimenez:/bin/bash
ivanovic:x:1002:1002:Иван Иванович:/home/ivanovic:/bin/bash
"""

with open(FILENAME, encoding='utf-8') as file:
    fieldnames = ['username', 'password', 'uid', 'gid', 'full_name', 'home', 'shell']
    content = csv.DictReader(file, fieldnames=fieldnames, delimiter=':')

    for row in content:
        username = row['username']
        full_name = row['full_name']
        home = row['home']

        print(f'{username} -> {full_name} with HOME="{home}" ')

# root -> root with HOME="/root"
# watney -> Mark Watney with HOME="/home/watney"
# jimenez -> José Jiménez with HOME="/home/jimenez"
# ivanovic -> Иван Иванович with HOME="/home/ivanovic"
