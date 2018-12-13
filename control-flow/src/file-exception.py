try:
    with open(r'/tmp/iris.csv') as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print('File does not exist')

except PermissionError:
    print('Permission denied')
