import matplotlib.pyplot as plt
import numpy as np

figure_1 = plt.figure(num=1)
x = np.linspace(0, 100, 101)
y_a_1 = np.linspace(30, 30, 26)
y_a_2 = np.linspace(1, 75, 75)
y_b_1 = np.linspace(50, 50, 51)
y_b_2 = np.linspace(1, 50, 50)
y_c = np.linspace(120, 120, 101)

# np.concatenate 可以将两个array矩阵(linspace生成的数据)合并
y_a = np.concatenate((y_a_1, 30 + y_a_2 * 3), axis=0)
y_b = np.concatenate((y_b_1, 50 + y_b_2 * 3), axis=0)

plt.plot(x, y_a, color='red', label='A')
plt.plot(x, y_b, color='yellow', label='B')
plt.plot(x, y_c, color='blue', label='C')

plt.grid()

plt.legend()

plt.xlabel('time/hour')
plt.ylabel('cost/yuan')

plt.xlim(1, 100)
plt.ylim(1, 200)

ticks_x = np.linspace(0, 100, 21)
ticks_y = np.linspace(0, 200, 21)
plt.xticks(ticks_x, fontsize=9)
plt.yticks(ticks_y, fontsize=9)

plt.show()