import csv

"""
    "first_name", "last_name"
    "José", "Jiménez"
    "Jan", "Twardowski"
    "Иван", "Иванович"
    "Mark", "Watney"
"""


with open(r'filename.csv') as file:
    data = csv.DictReader(file, delimiter=',', quotechar='"')

    for row in data:
        print(row['first_name'], row['last_name'])
