from enum import Enum


class Color(Enum):
    RED = '#00FF00'
    GREEN = '#00FF00'
    BLUE = '#0000FF'


print(Color.RED)        # Color.RED
print(Color.RED.name)   # RED
print(Color.RED.value)  # '#00FF00'


for color in Color:
    print(color)

# Color.RED
# Color.GREEN
# Color.BLUE


my_color = Color('#00FF00')     # <Color.GREEN: '#00FF00'>
my_color is Color.RED           # False
my_color is Color.GREEN         # True
