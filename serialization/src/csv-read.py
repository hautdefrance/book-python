import csv

FILE = r'../data/iris.csv'
"""
sepal_length,sepal_width,petal_length,petal_width,species
5.4,3.9,1.3,0.4,setosa
5.9,3.0,5.1,1.8,virginica
6.0,3.4,4.5,1.6,versicolor
7.3,2.9,6.3,1.8,virginica
5.6,2.5,3.9,1.1,versicolor
5.4,3.9,1.3,0.4,setosa
"""


with open(FILE) as file:
    data = csv.DictReader(file, delimiter=',', quotechar='"')

    for line in data:
        print(dict(line))

# {'sepal_length': '5.4', 'sepal_width': '3.9', 'petal_length': '1.3', 'petal_width': '0.4', 'species': 'setosa'}
# {'sepal_length': '5.9', 'sepal_width': '3.0', 'petal_length': '5.1', 'petal_width': '1.8', 'species': 'virginica'}
# {'sepal_length': '6.0', 'sepal_width': '3.4', 'petal_length': '4.5', 'petal_width': '1.6', 'species': 'versicolor'}
# {'sepal_length': '7.3', 'sepal_width': '2.9', 'petal_length': '6.3', 'petal_width': '1.8', 'species': 'virginica'}
# ...
