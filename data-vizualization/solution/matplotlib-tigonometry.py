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
from numpy import arange, sin, pi, cos

t = arange(0.0, 1.0, 0.01)

fig = figure(1)

ax1 = fig.add_subplot(211)
ax1.plot(t, sin(2*pi*t))
ax1.grid(True)
ax1.set_ylim((-2, 2))
ax1.set_ylabel('Value')
ax1.set_title('sin')

for label in ax1.get_xticklabels():
    label.set_color('r')


ax2 = fig.add_subplot(212)
ax2.plot(t, cos(2*2*pi*t))
ax2.grid(True)
ax2.set_ylim((-2, 2))

l = ax2.set_xlabel('cos')
l.set_color('g')
l.set_fontsize('large')
