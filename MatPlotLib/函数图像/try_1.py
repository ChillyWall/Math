import matplotlib.pyplot as plt
import numpy as np
import random

x = np.linspace(-50, 50, 10000)

fig, ax = plt.subplots()
ax.plot(x, x * 3 - 2, label='x')
ax.set_title('function')
ax.set_xlabel('x')
ax.set_ylabel('y')
figure = ax.gac()
ax.legend()
ax.grid()

plt.show(ax)
