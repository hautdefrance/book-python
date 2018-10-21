class Kelvin:
    def __init__(self, temperature):
        self.temperature = temperature

    def __getattribute__(self, name):
        if name == 'value':
            raise ValueError('Field is private, cannot display')
        else:
            super().__getattribute__(name)


temp = Kelvin(273)

temp.value = 20
print(temp.value)  # ValueError: Field is private, cannot display
