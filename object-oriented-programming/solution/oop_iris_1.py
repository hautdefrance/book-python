class Iris:
    def __init__(self):
        self.sepal_length = float()
        self.sepal_width = float()
        self.petal_length = float()
        self.petal_width = float()
        self.species = str()

    def total(self):
        return self.sepal_length \
               + self.sepal_width \
               + self.petal_length \
               + self.petal_width

    def average(self):
        return self.total() / 4
