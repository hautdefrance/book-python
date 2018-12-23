




"."

"@gmail-com"

"@[a-z]+\.[a-z]{3}"

"@[a-z]+.[a-z]{3}"





# ## Zadanie 2
#
# DATA = [
#     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
#     (5.8, 2.7, 5.1, 1.9, {'species': 'virginica'}),
#     (5.1, 3.5, 1.4, 0.2, {'species': 'setosa'}),
#     (5.7, 2.8, 4.1, 1.3, {'species': 'versicolor'}),
#     (6.3, 2.9, 5.6, 1.8, {'species': 'virginica'}),
#     (6.4, 3.2, 4.5, 1.5, {'species': 'versicolor'}),
#     (4.7, 3.2, 1.3, 0.2, {'species': 'setosa'}),
#     (7.0, 3.2, 4.7, 1.4, {'species': 'versicolor'}),
#     (7.6, 3.0, 6.6, 2.1, {'species': 'virginica'}),
#     (4.9, 3.0, 1.4, 0.2, {'species': 'setosa'}),
#     (4.6, 3.1, 1.5, 0.2, {'species': 'setosa'}),
# ]
#
# gatunki = set()
#
# for row in DATA[1:]:
#     gatunek = row[4]['species']
#     if gatunek.startswith('v'):
#         gatunki.add(gatunek)

## Zadanie 3
#
# DATA = [
#     {
#         "sepalLength": 5.0, "sepalWidth": 3.6,
#         "petalLength": 1.4, "petalWidth": 0.2,
#         "species": "setosa"},
#
#     {
#         "sepalLength": 4.9, "sepalWidth": 3.1,
#         "petalLength": 1.5, "petalWidth": 0.1,
#         "species": "setosa"},
#
#     {
#         "sepalLength": 4.9, "sepalWidth": 3.0,
#         "petalLength": 1.4, "petalWidth": 0.2,
#         "species": "setosa"},
# ]
#
# print('<table>')
# header = DATA[0].keys()
#
# print('<tr>')
# for th in header:
#     print(f'<th>{th}</th>')
# print('</tr>')
#
# for slownik in DATA:
#     print('<tr>')
#     for key in header:
#         print(f'<td>{slownik[key]}</td>')
#     print('</tr>')
#
# print('</table>')
