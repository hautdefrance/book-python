class Bear(object):
    def sound(self):
        print('Groarrr')


class Dog(object):
    def sound(self):
        print('Woof woof!')


def makeSound(animal):
    animal.sound()


koala = Bear()
hart = Dog()

makeSound(koala)
makeSound(hart)
