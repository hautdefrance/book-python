FILENAME = r'C:\Temp\bootfilure.txt'


with open(FILENAME, encoding='utf-8') as file:
    selected_lines = file.readlines()[1:30]
