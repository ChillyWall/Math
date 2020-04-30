import matplotlib.pyplot as plt
import numpy as np
from function import *


x = np.linspace(-10, 10, 21)
y_1 = 2 * x - 4
y_2 = -2 * x + 2

plt.plot(x, y_1, label='y_1')
plt.plot(x, y_2, label='y_2')

set_tick(-10, 10, 21)

rectangular_coordinate()

plt.xlim(-10, 10)
plt.ylim(-10, 10)

plt.show()