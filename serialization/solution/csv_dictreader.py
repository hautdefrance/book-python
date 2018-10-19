import csv


FILENAME = 'iris-dataset.csv'

FIELDNAMES = [
    'Sepal length',
    'Sepal width',
    'Petal length',
    'Petal width',
    'Species']


with open(FILENAME, encoding='utf-8') as file:
    species = file.readline().strip().split(',')[2:]
    species_dict = {i: element for i, element in enumerate(species)}

    data = csv.DictReader(
        file,
        fieldnames=FIELDNAMES,
        delimiter=',',
        quotechar='"')

    next(data)

    for row in data:
        row = dict(row)
        index = int(row['Species'])
        row['Species'] = species_dict[index]
        print(row)
