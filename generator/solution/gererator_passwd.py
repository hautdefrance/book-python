import sys


FILENAME = '../assignment/etc-passwd.txt'


def comprahension(lines):
    accounts = []

    for line in lines:
        if line.isspace() or line.startswith('#'):
            continue

        uid = int(line.split(':')[2])
        username = str(line.split(':')[0])

        if uid < 1000:
            accounts.append(username)

    return accounts


def generator(lines):
    for line in lines:
        if line.isspace() or line.startswith('#'):
            continue

        uid = int(line.split(':')[2])
        username = str(line.split(':')[0])

        if uid < 1000:
            yield username


if __name__ == '__main__':
    with open(FILENAME, encoding='utf-8') as file:
        lines = file.readlines()

    print('Comprahension:', sys.getsizeof(comprahension(lines)))
    print('Generator:', sys.getsizeof(generator(lines)))
