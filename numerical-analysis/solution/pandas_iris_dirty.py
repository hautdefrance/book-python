import pandas as pd


FILE = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/data/iris-dirty.csv'

COLUMNS = [
    'Sepal length',
    'Sepal width',
    'Petal length',
    'Petal width',
    'Species'
]

df = pd.read_csv(FILE, skiprows=1, names=COLUMNS)

df['Species'].replace(to_replace={
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica'
}, inplace=True)

df = df.sample(frac=1.0).reset_index(drop=True)

df.head(5)
df.tail(3)

df.describe()
