import sys


FILE = '../assignment/etc-passwd.txt'


def function(lines):
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
    with open(FILE) as file:
        lines = file.readlines()

    fn = function(lines)
    gene = generator(lines)

    print(f'Function: {sys.getsizeof(fn)}')
    print(f'Generator: {sys.getsizeof(gene)}')
