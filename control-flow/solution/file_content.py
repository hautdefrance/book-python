FILE = input('Podaj nazwę pliku: ')


try:

    with open(FILE, mode='w') as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print('File does not exists')

except PermissionError:
    print('Permission denied')
