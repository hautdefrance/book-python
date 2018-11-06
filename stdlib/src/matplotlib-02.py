import matplotlib.pyplot as plt
import numpy as np

y = np.arange(0.0, 2.0, 0.01)
x = 1 + np.sin(2 * np.pi * y)

fig, ax = plt.subplots()

ax.plot(y, x)
ax.grid()
ax.set(
    xlabel='time (s)',
    ylabel='voltage (mV)',
    title='Voltage in Time')

plt.show()
