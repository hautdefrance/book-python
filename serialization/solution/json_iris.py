import json
from dataclasses import dataclass

FILENAME = '../tmp/iris.json'

@dataclass
class Iris:
    sepalLength: float
    sepalWidth: float
    petalLength: float
    petalWidth: float


class Setosa(Iris):
    pass


class Virginica(Iris):
    pass


class Versicolor(Iris):
    pass


with open(FILENAME, encoding='utf-8') as file:
    data = json.load(file)


result = []

for iris in data:
    if iris['species'] == 'setosa':
        cls = Setosa
    elif iris['species'] == 'versicolor':
        cls = Versicolor
    elif iris['species'] == 'virginica':
        cls = Virginica
    else:
        print('Not supported')


    result.append(cls(
        sepalLength=iris['sepalLength'],
        sepalWidth=iris['sepalWidth'],
        petalLength=iris['petalLength'],
        petalWidth=iris['petalWidth']
    ))

print(result)
