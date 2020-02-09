# _*_ coding: utf-8 _*_
# 绘制随机漫步图

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 程序处于活动状态，则不断地模拟随机漫步数
while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=4)
    plt.show()

    keep_running = input("Make another walk?y/n: ")
    if keep_running == 'n':
        break