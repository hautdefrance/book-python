from datetime import date
from pprint import pprint

ETC_SHADOW = '../assignment/etc-shadow.txt'
ETC_PASSWD = '../assignment/etc-passwd.txt'
ETC_GROUP = '../assignment/etc-group.txt'

users = list()
groups = dict()
passwords = dict()

ALGORITHMS = {
    '1': 'MD5',
    '2a': 'Blowfish',
    '2y': 'Blowfish',
    '5': 'SHA-256',
    '6': 'SHA-512',
}


def is_clean(line):
    if line.isspace() or line.startswith('#'):
        return False
    else:
        return True


with open(ETC_GROUP) as group:
    for line in group:
        if is_clean(line):
            groupname, password, gid, members = line.split(':')

            for user in members.split(','):
                user = user.strip()

                if not user:
                    continue

                if user not in groups.keys():
                    groups[user] = [groupname]
                else:
                    groups[user].append(groupname)


with open(ETC_SHADOW) as shadow:
    for line in shadow:
        if is_clean(line):
            username, password, lastchanged, *_ = line.split(':')
            lastchanged = date.fromtimestamp(int(lastchanged))

            if password in ('*', '!', '!!'):
                locked = True
                algorithm = None
                salt = None
                password = None
            else:
                locked = False
                _, algorithm, salt, password = password.split('$')
                algorithm = ALGORITHMS[algorithm]

            passwords[username] = {
                'algorithm': algorithm,
                'password': password,
                'locked': locked,
                'salt': salt,
                'lastchanged': lastchanged,
            }


with open(ETC_PASSWD, encoding='utf-8') as passwd:
    for line in passwd:
        if is_clean(line):
            username, _, uid, gid, fullname, home, shell = line.split(':')

            if int(uid) >= 1000:
                p = passwords.get(username, dict())
                g = groups.get(username, list())
                users.append({
                    'login': username,
                    'uid': uid,
                    'gid': gid,
                    'home': home,
                    'shell': shell,
                    'password': p.get('password'),
                    'algorithm': p.get('algorithm'),
                    'locked': p.get('locked'),
                    'salt': p.get('salt'),
                    'lastchanged': p.get('lastchanged'),
                    'groups': g,
                })


pprint(users)
