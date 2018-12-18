import csv

DATA = [
    {'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
    {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
    {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
    {'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
    {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
    {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'},
]

fieldnames = set()

for row in DATA:
    fieldnames.update(row.keys())


with open(r'../data/iris.csv', mode='w') as file:
    writer = csv.DictWriter(
        f=file,
        fieldnames=fieldnames,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator='\n')

    writer.writeheader()

    for row in DATA:
        writer.writerow(row)
