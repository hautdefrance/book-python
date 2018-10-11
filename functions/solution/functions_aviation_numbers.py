SPEAK = {
    '-': 'minus',
    '.': 'and',
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'tree',
    '4': 'fower',
    '5': 'fife',
    '6': 'six',
    '7': 'seven',
    '8': 'ait',
    '9': 'niner',
}

def aviation_numbers(number):
    out = []
    for char in str(number):
        out.append(SPEAK[char])

    return ' '.join(out)

out = aviation_numbers(1969)       # 'one niner six niner'
print(out)

out = aviation_numbers(31337)      # 'tree one tree tree seven'
print(out)

out = aviation_numbers(13.37)      # 'one tree and tree seven'
print(out)

out = aviation_numbers(31.337)     # 'tree one and tree tree seven'
print(out)

out = aviation_numbers(-1969)      # 'minus one niner six niner'
print(out)

out = aviation_numbers(-31.337)    # 'minus tree one and tree tree seven
print(out)

out = aviation_numbers(-49.35)     # 'minus fower niner and tree fife'
print(out)

