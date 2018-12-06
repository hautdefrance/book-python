from timeit import timeit


setup = """
first_name = 'José'
last_name = 'Jiménez'
"""

TEST = dict()
TEST[0] = 'name = f"{first_name} {last_name}"'
TEST[1] = 'name = "{0} {1}".format(first_name, last_name)'
TEST[2] = 'name = first_name + " " + last_name'
TEST[3] = 'name = " ".join([first_name, last_name])'


for stmt in TEST.values():
    duration = timeit(stmt, setup, number=10000)
    print(f'{duration:.5}\t{stmt}')

# 0.00071559    name = f"{first_name} {last_name}"
# 0.0026514     name = "{0} {1}".format(first_name, last_name)
# 0.001015      name = first_name + " " + last_name
# 0.0013494     name = " ".join([first_name, last_name])
