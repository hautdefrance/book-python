def increment_population():
    Astronaut.population += 1

def decrement_population():
    Astronaut.population -= 1


class Astronaut:
    population = 0

    def __init__(self, name):
        self.name = name
        increment_population()

    def __del__(self):
        decrement_population()


jose = Astronaut('José Jiménez')
print(Astronaut.population)  # 1

ivan = Astronaut('Иван Иванович')
print(Astronaut.population)  # 2

# ----------------

class Astronaut:
    population = 0

    def __init__(self, name):
        self.name = name
        Astronaut.increment_population()

    def __del__(self):
        decrement_population()

    @staticmethod
    def increment_population():
        Astronaut.population += 1

    @staticmethod
    def decrement_population():
        Astronaut.population -= 1


jose = Astronaut('José Jiménez')
print(Astronaut.population)  # 1

ivan = Astronaut('Иван Иванович')
print(Astronaut.population)  # 2

del ivan
print(Astronaut.population)  # 1
