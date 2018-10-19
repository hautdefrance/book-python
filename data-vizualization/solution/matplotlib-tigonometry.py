import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

x1 = np.arange(0.0, 1.0, 0.01)
y1 = np.sin(2 * np.pi * x1)
plt.plot(x1, y1)

x2 = np.arange(0.0, 1.0, 0.01)
y2 = np.cos(2 * np.pi * x2)
plt.plot(x2, y2)




from matplotlib.pyplot import figure


x = np.arange(0.0, 1.0, 0.01)

fig = figure(1)

ax1 = fig.add_subplot(211)
ax1.plot(x, np.sin(2 * np.pi * x))
ax1.grid(True)
ax1.set_ylabel('Wartość funkcji')
ax1.set_title('sin')

for label in ax1.get_xticklabels():
    label.set_color('r')


ax2 = fig.add_subplot(212)
ax2.plot(x, np.cos(2 * np.pi * x))
ax2.grid(True)
ax1.set_ylabel('Wartość funkcji')

label = ax2.set_xlabel('cos')
label.set_color('g')
label.set_fontsize('large')

