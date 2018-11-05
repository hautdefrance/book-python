FILENAME = input('Podaj nazwę pliku: ')


try:

    with open(FILENAME, mode='w') as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print('File does not exists')

except PermissionError:
    print('Permission denied')
