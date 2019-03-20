def get_measurements_function(file, species):
    measurements = []

    for line in file:
        *m, s = line.strip().split(',')
        if s == species:
            measurements.append(m)

    return measurements


def get_measurements_comprehension(file, species):
    for line in file:
        *m, s = line.strip().split(',')
        if s == species:
            yield m


with open(r'iris.csv') as file:
    next(file)
    setosa = []
    virginica = []
    versicolor = []

    for x in get_measurements_comprehension(file, 'setosa'):
        print(x)
