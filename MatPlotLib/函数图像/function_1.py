import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-100, 100, 201)
y1 = -0.1 * x
y2 = x / 2
y3 = 2 * x ** 2
y4 = np.sqrt(4 * x)

fig, axs = plt.subplots(2, 2)

axs[0][0].plot(x, y1)

axs[0][1].plot(x, y2)

axs[1][0].plot(x, y3)

axs[1][1].plot(x, y4)

plt.show()
