import numpy as np
import matplotlib.pyplot as plt

# mac下label标签显示中文
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# subplots()可在一个图片中绘制一个或多个图表
fig, ax = plt.subplots()
# plot()给定的数据以有意义的方式绘制图表
"""linewidth = 3决定线条的粗细"""
ax.plot(input_values, squares, linewidth=3)
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)
# “打开Matplotlib查看器并显示绘制的图表”
plt.show()
