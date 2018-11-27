ETC_GROUPS = r'etc-group.txt'
ETC_SHADOW = r'etc-shadow.txt'
ETC_PASSWD = r'etc-passwd.txt'
ALGORITHMS = {
    '1': 'MD5',
    '2a': 'Blowfish',
    '2y': 'Blowfish',
    '5': 'SHA-256',
    '6': 'SHA-512',
}

output_groups = {}
output_shadow = {}
output_passwd = {}
output = []

try:
    with open(ETC_GROUPS, encoding='utf-8') as file:
        etc_groups = file.readlines()

except FileNotFoundError:
    print('File does not exist')

except PermissionError:
    print('Permission denied')


try:
    with open(ETC_SHADOW, encoding='utf-8') as file:
        etc_shadow = file.readlines()

except FileNotFoundError:
    print('File does not exist')

except PermissionError:
    print('Permission denied')


try:
    with open(ETC_PASSWD, encoding='utf-8') as file:
        etc_passwd = file.readlines()

except FileNotFoundError:
    print('File does not exist')

except PermissionError:
    print('Permission denied')


for line in etc_groups:
    line = line.strip()

    if not line or line.startswith('#'):
        continue

    record = line.split(':')
    groupname = record[0]
    members = record[3].split(',')

    if members == ['']:
        continue

    for member in members:
        if member not in output_groups.keys():
            output_groups[member] = set()

        output_groups[member].add(groupname)


for line in etc_shadow:
    line = line.strip()

    if not line or line.startswith('#'):
        continue

    record = line.split(':')
    username = record[0]
    password = record[1]
    last_change = record[2]

    if password.startswith('$'):
        locked = False
        password = password.split('$')
        password_algorithm = ALGORITHMS[password[1]]
        password_salt = password[2]
        password_password = password[3]
    else:
        locked = True
        password_algorithm = None
        password_salt = None
        password_password = None

    output_shadow[username] = {
        'password': password_password,
        'salt': password_salt,
        'algorithm': password_algorithm,
        'last_change': last_change,
        'locked': locked,
    }


for line in etc_passwd:
    line = line.strip()

    if not line or line.startswith('#'):
        continue

    record = line.split(':')
    username = record[0]

    output_passwd[username] = {
        'password': record[1],
        'uid': int(record[2]),
        'gid': int(record[3]),
        'gecos': record[4],
        'home': record[5],
        'shell': record[6],
    }

for user in output_passwd:
    passwd = output_passwd[user]

    if passwd['uid'] < 1000:
        continue

    groups = output_groups[user]
    shadow = output_shadow[user]

    output.append({
        'login': user,
        'uid': passwd['uid'],
        'gid': passwd['gid'],
        'home': passwd['home'],
        'shell': passwd['shell'],
        'algorithm': shadow['algorithm'],
        'password': shadow['password'],
        'groups': groups,
        'last_changed': shadow['last_change'],
        'locked': shadow['locked'],
    })


from pprint import pprint
pprint(output)
