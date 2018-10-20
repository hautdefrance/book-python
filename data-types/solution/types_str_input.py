name = input('Type your name: ')

text = f"""'''My name... "{name}".\n\tI\'m an \"""astronaut!\"""'''"""

print(text)
# '''My name... "José Jiménez".
# 	I'm an """astronaut!"""'''


output = text.replace(' ', '_').replace('\t', '_')
output = output.upper()

print(output)
# '''MY_NAME_"JOSÉ_JIMÉNEZ".
# _I'M_AN_"""ASTRONAUT!"""'''
