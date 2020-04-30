import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3)

fig, ax = plt.subplots()
plt.plot(x, (x ** 2) * (x - 3), label='y = x ** 2 * (x -3)')
plt.plot(x, x ** 2, label='y = x ** 2')
plt.title('function graph')
plt.legend()
plt.grid()

plt.show(ax)
