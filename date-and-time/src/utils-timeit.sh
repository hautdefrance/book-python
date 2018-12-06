python3 -m timeit -n100000 -r100 --setup='name="Jose Jimenez"' 'out = f"My name... {name}"'
# 100000 loops, best of 100: 55.9 nsec per loop

python3 -m timeit -n100000 -r100 --setup='name="Jose Jimenez"' 'out = "My name... {name}".format(name=name)'
# 100000 loops, best of 100: 327 nsec per loop

python3 -m timeit -n100000 -r100 --setup='name="Jose Jimenez"' 'out = "My name... %s" % name'
# 100000 loops, best of 100: 124 nsec per loop
