class Celsius:
    def __get__(self, instance, owner):
        celsius = instance.kelvin - 273.15
        return round(celsius, 2)

    def __set__(self, instance, celsius):
        kelvin = celsius + 273.15
        instance.kelvin = round(kelvin, 2)

    def __delete__(self, instance):
        instance.kelvin = 0


class Fahrenheit:
    def __get__(self, instance, owner):
        celsius = instance.kelvin - 273.15
        fahrenheit = celsius * 9/5 + 32
        return round(fahrenheit, 2)

    def __set__(self, instance, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        kelvin = celsius + 273.15
        instance.kelvin = round(kelvin, 2)

    def __delete__(self, instance):
        instance.kelvin = 0


class Temperature:
    kelvin = 0
    celsius = Celsius()
    fahrenheit = Fahrenheit()


temp = Temperature()

temp.kelvin = 273.15
print(f'K: {temp.kelvin}')      # 273.15
print(f'C: {temp.celsius}')     # 0.0
print(f'F: {temp.fahrenheit}')  # 32.0

print()

temp.fahrenheit = 100
print(f'K: {temp.kelvin}')      # 310.93
print(f'C: {temp.celsius}')     # 37.78
print(f'F: {temp.fahrenheit}')  # 100.0

print()

temp.celsius = 100
print(f'K: {temp.kelvin}')      # 373.15
print(f'C: {temp.celsius}')     # 100.0
print(f'F: {temp.fahrenheit}')  # 212.0

print()

del temp.celsius
print(f'K: {temp.kelvin}')      # 0
print(f'C: {temp.celsius}')     # -273.15
print(f'F: {temp.fahrenheit}')  # -459.67
