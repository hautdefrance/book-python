DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, {'species': 'virginica'}),
    (5.1, 3.5, 1.4, 0.2, {'species': 'setosa'}),
    (5.7, 2.8, 4.1, 1.3, {'species': 'versicolor'}),
    (6.3, 2.9, 5.6, 1.8, {'species': 'virginica'}),
    (6.4, 3.2, 4.5, 1.5, {'species': 'versicolor'}),
    (4.7, 3.2, 1.3, 0.2, {'species': 'setosa'}),
    (7.0, 3.2, 4.7, 1.4, {'species': 'versicolor'}),
    (7.6, 3.0, 6.6, 2.1, {'species': 'virginica'}),
    (4.6, 3.1, 1.5, 0.2, {'species': 'setosa'}),
]

for row in DATA[1:]:
    species = row[4]['species']

    if species.startswith('v'):
        print(species)
