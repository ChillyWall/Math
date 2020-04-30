import matplotlib.pyplot as plt
import numpy as np

# num=设置图像的编号, figsize=设置图像尺寸
plt.figure(num=1)

# np.linspace()用来生成范围内的数字, 以及个数
x = np.linspace(-100, 100, 20000)
y1 = x ** 2
y2 = x ** 2 * (x - 3)

# plt.plot()用来画线, 第一个是横坐标第二个是纵坐标.
# 使用color=设置颜色,
# label=设置名称,
# linestyle=设置线的形式,'--'是虚线
# linewidth=用来设置线的粗细
plt.plot(x, y1, color='red', label='x ** 2', linewidth=5.0)
plt.plot(x, y2, label='x ** 2 * (x - 3)', linestyle='--')

# plt.xlim() 用来设置横轴的显示范围
# plt.ylim() 用来设置纵轴的显示范围
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# plt.xticks() 用来设置横轴的刻度范围和个数
# plt.yticks() 用来设置纵轴的刻度范围和个数
ticks = np.linspace(-10, 10, 21)
plt.xticks(ticks)
plt.yticks(ticks)

# plt.legend() 显示线的名字(label)
plt.legend()

# plt.grid() 显示坐标刻度
plt.grid()


# plt.gac 读取图像的参数到变量中
ax = plt.gca()

# .spines[] 选择边框, 所有位置:top, bottom, left, right
# .set_color() 设置颜色
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# .xaxis 设置横轴的数据
# .set_ticks_position() 移动坐标刻度的位置
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# .spines[]设置边框
# .set_position 设置边框. 纵轴是x=0, 横轴是y=0.所有位置属性:outward, axes, data
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

# plt.show() 显示图表
plt.show()
