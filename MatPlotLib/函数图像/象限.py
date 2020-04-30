import matplotlib.pyplot as plt
import numpy as np
from function import *

x = np.linspace(-10, 10, 21)
y1 = -x + 3
y2 = x + 3
y3 = -x - 3
y4 = x - 3

plt.plot(x, y1, label="k < 0, b > 0")
plt.plot(x, y2, label="k > 0, b > 0")
plt.plot(x, y3, label="k < 0, b < 0")
plt.plot(x, y4, label="k > 0, b < 0")

plt.legend()

rectangular_coordinate()

set_tick(-10, 10, 21)

plt.xlim(-10, 10)
plt.ylim(-10, 10)

plt.title("y = kx + b")

plt.show()