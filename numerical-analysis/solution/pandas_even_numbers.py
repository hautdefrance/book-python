import numpy as np
import pandas as pd


values = np.random.randint(10, 100, size=24)
indexes = list('abcdefghijklmnopqrstuvwz')
median = int(len(indexes) / 2)

series = pd.Series(values, index=indexes)
output = series[median-3:median+4]

print(output)
