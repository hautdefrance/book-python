FILENAME = r'C:\Temp\bootfilure.txt'

try:
    with open(FILENAME, mode='r', encoding='utf-8') as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print('File does not exist')

except PermissionError:
    print('Permission denied')
