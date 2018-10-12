class Kelvin:
    def __init__(self, initial_temperature):
        self.temperature = initial_temperature

    def __setattr__(self, name, new_value):
        if name == 'value' and new_value < 0.0:
            raise ValueError('Temperature cannot be negative')
        else:
            super().__setattr__(name, new_value)


temp = Kelvin(273)

temp.value = 20
print(temp.value)  # 20

temp.value = -10
print(temp.value)  # ValueError: Temperature cannot be negative
