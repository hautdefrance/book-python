class Astronaut:
    def __init__(self, name):
        self.name = name


jose = Astronaut(name='José Jiménez')

str(jose)       # <__main__.Astronaut object at 0x01E3FDF0>
print(jose)     # <__main__.Astronaut object at 0x01E3FDF0>
