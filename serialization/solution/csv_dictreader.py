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

    # rows, count, *species = list(data)[0]
    # species_dict = {i: str(element) for i, element in enumerate(species)}

    next(data)
    data.__next__()
    # data = list(data)[1:]

    for row in data:
        row = dict(row)
        index = int(row['Species'])
        row['Species'] = SPECIES[index]
        print(row)
