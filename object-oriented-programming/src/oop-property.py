class Celsius:
    def __init__(self, value=0):
        self._value = value

    @property
    def temperature(self):
        print('Getting value')
        return self._value

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError('Temperature below -273 is not possible')
        print('Setting value')
        self._value = value


body = Celsius(36.6)

body.temperature
body.temperature = 34     # Setting value
body.temperature = -1000  # ValueError: Temperature below -273 is not possible
