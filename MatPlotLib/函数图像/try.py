import matplotlib.pyplot as plt
import numpy as np
from get_prime import find_prime_2
from function import rectangular_coordinate

x = np.linspace(-100, 100, 201)
y = x * 2

plt.plot(x, y)

plt.grid()

ticks = np.linspace(-10, 10, 21)
plt.xticks(ticks)
plt.yticks(ticks)

plt.xlim(-10, 10)
plt.ylim(-10, 10)

rectangular_coordinate()
find_prime_2(1, 100)
plt.show()
