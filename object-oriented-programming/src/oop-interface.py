class MLModelInterface:
    def fit(self, features, labels):
        raise NotImplementedError

    def predict(self, data):
        raise NotImplementedError


class KNeighborsClassifier(MLModelInterface):
    def fit(self, features, labels):
        pass

    def predict(self, data):
        pass


class LinearRegression(MLModelInterface):
    def fit(self, features, labels):
        pass

    def predict(self, data):
        pass

class LogisticsRegression(MLModelInterface):
    pass


# Imput to the classifier
features = [
    (5.1, 3.5, 1.4, 0.2),
    (4.9, 3.0, 1.4, 0.2),
    (4.7, 3.2, 1.3, 0.2),
    (7.0, 3.2, 4.7, 1.4),
    (6.4, 3.2, 4.5, 1.5),
    (6.9, 3.1, 4.9, 1.5),
    (6.3, 3.3, 6.0, 2.5),
    (5.8, 2.7, 5.1, 1.9),
    (7.1, 3.0, 5.9, 2.1),
]

# 0: I. setosa
# 1: I. versicolor
# 2: I. virginica
labels = [0, 0, 0, 1, 1, 1, 2, 2, 2]

to_predict = [
    (5.7, 2.8, 4.1, 1.3),
    (4.9, 2.5, 4.5, 1.7),
    (4.6, 3.4, 1.4, 0.3),
]

model = LinearRegression()
model.fit(features, labels)
model.predict(to_predict)
# [1, 2, 0]
