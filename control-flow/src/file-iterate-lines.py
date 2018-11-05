FILENAME = r'C:\Temp\bootfilure.txt'


with open(FILENAME, encoding='utf-8') as file:
    for line in file:
        if not line.startswith('#'):
            print(line)
