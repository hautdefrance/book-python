DATA = [
    {'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
    {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
    {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
    {'Petal length': 1.4, 'Petal width': 0.2, 'Species': 'setosa'},
    {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
    {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'},
]

unique_keys = set()

for row in DATA:
    unique_keys.update(row.keys())



unique_keys = set()

for row in DATA:
    for key in row.keys():
        unique_keys.add(key)



all_keys = list()

for row in DATA:
    for key in row.keys():
        all_keys.append(key)

unique_keys = set(all_keys)



unique_keys = list()

for row in DATA:
    for key in row.keys():
        if key not in unique_keys:
            unique_keys.append(key)
