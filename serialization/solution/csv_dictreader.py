import csv


FILENAME = 'iris.csv'
FIELDNAMES = [
    'Sepal length',
    'Sepal width',
    'Petal length',
    'Petal width',
    'Species',
]


with open(FILENAME, encoding='utf-8') as file:
    data = csv.DictReader(
        file,
        fieldnames=FIELDNAMES,
        delimiter=',',
        quoting=csv.QUOTE_NONE)

    for row in data:
        print(dict(row))
