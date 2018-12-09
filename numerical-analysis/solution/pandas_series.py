import pandas as pd


values = [x for x in range(0, 20) if x % 2 == 0]

s = pd.Series(values)


s ** 2
s + 5
