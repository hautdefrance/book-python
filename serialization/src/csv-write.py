import csv


DATA = [
    {'sepal_length': 5.4, 'sepal_width': 3.9, 'petal_length': 1.3, 'petal_width': 0.4, 'species': 'setosa'},
    {'sepal_length': 5.9, 'sepal_width': 3.0, 'petal_length': 5.1, 'petal_width': 1.8, 'species': 'virginica'},
    {'sepal_length': 6.0, 'sepal_width': 3.4, 'petal_length': 4.5, 'petal_width': 1.6, 'species': 'versicolor'},
    {'sepal_length': 7.3, 'sepal_width': 2.9, 'petal_length': 6.3, 'petal_width': 1.8, 'species': 'virginica'},
    {'sepal_length': 5.6, 'sepal_width': 2.5, 'petal_length': 3.9, 'petal_width': 1.1, 'species': 'versicolor'},
    {'sepal_length': 5.4, 'sepal_width': 3.9, 'petal_length': 1.3, 'petal_width': 0.4, 'species': 'setosa'},
]


with open(r'filename.csv', mode='w') as file:
    writer = csv.DictWriter(
        f=file,
        fieldnames=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'],
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator='\n')

    writer.writeheader()

    for row in DATA:
        writer.writerow(row)
