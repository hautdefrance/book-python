import math
import random
from matplotlib import pyplot as plt


x1 = [x*0.01 for x in range(0,628)]
y1 = [math.sin(x*0.01)+random.gauss(0, 0.1) for x in range(0,628)]
plt.plot(x1, y1)


x2 = [x*0.5 for x in range(0,round(63/5))]
y2 = [math.cos(x*0.5) for x in range(0,round(63/5))]
plt.plot(x2, y2, 'o-')


plt.show()