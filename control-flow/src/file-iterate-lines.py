FILE = r'/tmp/my-file.txt'


with open(FILE) as file:
    for line in file:
        print(line)
