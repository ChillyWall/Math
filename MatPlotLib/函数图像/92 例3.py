import matplotlib.pyplot as plt
import numpy as np
from function import rectangular_coordinate as rect_coor

x = np.linspace(-50, 50, 101)
y_1 = -0.5 * x
y_2 = 2 * x

plt.figure("Page 92 of math book, example 3")
plt.plot(x, y_1, color='blue', linestyle='--')
plt.plot(x, y_1 + 1, color='blue')
plt.plot(x, y_2, color='red', linestyle='--')
plt.plot(x, y_2 - 1, color='red')

plt.xlim(-3, 3)
plt.ylim(-3, 3)

ticks = np.linspace(-3, 3, 7)
plt.xticks(ticks)
plt.yticks(ticks)

rect_coor()

plt.show()
