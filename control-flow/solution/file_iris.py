FILE = r'../assignments/iris.csv'

X = []
y = []


with open(FILE) as file:
    for line in file.readlines()[1:]:
        line = line.strip().split(',')

        features = tuple(float(x) for x in line[0:4])
        label = line[4]

        X.append(features)
        y.append(label)


print(X)
print(y)
