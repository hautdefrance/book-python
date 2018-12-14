'https://raw.githubusercontent.com/AstroMatt/book-python/master/database/data/iris.csv'


def print_iris(sepal_length, sepal_width, *args, **kwargs):
    print(locals())


with open(r'../data/iris.csv') as file:
    for line in file.readlines()[1:]:
        *features, labels = line.strip().split(',')

        d = {'label': labels}
        print_iris(*features, **d)
