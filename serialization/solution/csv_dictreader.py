import csv


FIELDNAMES = [
    'Sepal length',
    'Sepal width',
    'Petal length',
    'Petal width',
    'Species',
]


with open(r'../data/iris.csv') as file:
    data = csv.DictReader(
        f=file,
        fieldnames=FIELDNAMES,
        delimiter=',',
        quoting=csv.QUOTE_NONE)

    for row in data:
        print(dict(row))
