class Astronaut:
    def __init__(self, name):
        self.name = name


{1, 1, 2}
# {1, 2}

jose = Astronaut(name='Jose Jimenez')
data = {jose, jose}
len(data)
# 1

data = {Astronaut(name='Jose Jimenez'), Astronaut(name='Jose Jimenez')}
len(data)
# 2
