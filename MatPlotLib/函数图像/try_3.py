import matplotlib.pyplot as plt
import numpy as np


t = 1
a = 100
b = 6 * 10 ** -4
x = 100
y = a + a * b
final_1 = [y]
while True:
    y = y + y * b
    final_1.append(y)
    t = t + 1
    if t == x:
        break

numbers_x = list(range(1, 101))
final_2 = []
correct_times = 0
for x in numbers_x:
    final = a + x * a * b + a * b ** x + 3 * (x - 2) * a * b ** 2
    final_2.append(final)
    if final in final_1:
        correct_times = correct_times + 1
print(final_1)
print(final_2)
print(correct_times)
