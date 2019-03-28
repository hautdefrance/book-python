import sys


FILE = '../assignment/etc-passwd.txt'


def function(lines):
    accounts = []

    for line in lines:
        if line.isspace() or line.startswith('#'):
            continue

        username, _, uid, *_ = line.split(':')

        if int(uid) < 1000:
            accounts.append(username)

    return accounts


def generator(lines):
    for line in lines:
        if line.isspace() or line.startswith('#'):
            continue

        username, _, uid, *_ = line.split(':')

        if int(uid) < 1000:
            yield username


if __name__ == '__main__':
    with open(FILE) as file:
        lines = file.readlines()

    fn = function(lines)
    gene = generator(lines)

    print(f'Function: {sys.getsizeof(fn)}')
    print(f'Generator: {sys.getsizeof(gene)}')
