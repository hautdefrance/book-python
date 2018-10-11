class Astronaut:
    """
    Nowy astronauta
    """

    def __init__(self, name):
        self.name = name

    def say_hello(self, lang='en'):
        """
        wyświetla przywitanie w zalezności od języka

        >>> Astronaut(name='José Jiménez').say_hello(lang='es')
        ¡hola José Jiménez!

        >>> Astronaut(name='Иван Иванович').say_hello(lang='ru')
        здраствуйте Иван Иванович!
        """
        if lang == 'en':
            print(f'hello {self.first_name}')
        elif lang == 'es':
            print(f'¡hola {self.first_name}!')
        elif lang == 'ru':
            print(f'здраствуйте {self.first_name}!')
        else:
            print(f'witaj {self.first_name}!')


astronaut = Astronaut(name='José Jiménez')

help(astronaut)
print(astronaut.say_hello.__doc__)