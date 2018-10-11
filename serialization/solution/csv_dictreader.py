import csv


FILENAME = 'iris-dataset.csv'

FIELDNAMES = [
    'Sepal length',
    'Sepal width',
    'Petal length',
    'Petal width',
    'Species']

SPECIES = {
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica'}


with open(FILENAME, encoding='utf-8') as file:
    data = csv.DictReader(
        file,
        fieldnames=FIELDNAMES,
        delimiter=',',
        quotechar='"')

    for row in list(data)[1:]:
        row = dict(row)
        index = int(row['Species'])
        row['Species'] = SPECIES[index]
        print(row)
