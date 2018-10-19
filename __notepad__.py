import csv


FILENAME = 'serialization/solution/iris-dataset.csv'

FIELDNAMES = [
    'Sepal length',
    'Sepal width',
    'Petal length',
    'Petal width',
    'Species']


with open(FILENAME, encoding='utf-8') as file:
    data = csv.DictReader(
        file,
        fieldnames=FIELDNAMES,
        delimiter=',',
        quotechar='"')

    next(data)

    for row in data:
        print(row)
