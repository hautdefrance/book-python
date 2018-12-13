FILE = r'/tmp/my-file.txt'

try:
    with open(FILE) as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print('File does not exist')

except PermissionError:
    print('Permission denied')
