def hello():
    print('hello')


class Astronaut:
    def say_name(self):
        print(self.first_name)


jose = Astronaut()
jose.first_name = 'José Jiménez'
print(jose.first_name)
# 'José Jiménez'

jose.say_hello = hello
jose.say_hello()
# hello

jose.say_ehlo = lambda: print('ehlo')
jose.say_ehlo()
# ehlo

jose.say_name()
# José Jiménez

Astronaut.say_name = lambda self: print(f'My name is... {self.first_name}')
jose.say_name()
# My name is... José Jiménez
