DATA = (
    5.8, 2.7, 5.1, 1.9, 'virginica',
    5.1, 3.5, 1.4, 0.2, 'setosa',
    5.7, 2.8, 4.1, 1.3, 'versicolor',
    6.3, 2.9, 5.6, 1.8, 'virginica',
    6.4, 3.2, 4.5, 1.5, 'versicolor',
    4.7, 3.2, 1.3, 0.2, 'setosa',
)

STEP = 5

features = list()
labels = list()
species = set()

for i in range(0, len(DATA), STEP):
    *measurements, kind = DATA[i:i+STEP]
    features.append(measurements)
    labels.append(kind)
    species.add(kind)

print(f'Features:\n{features}\n')
print(f'Labels:\n{labels}\n')
print(f'Species:\n{species}\n')
