import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

p = 0.31  # 触发概率
I = 200000  # 蒙特卡洛模拟次数


def single_loop():  # 蒙特卡洛的单次随机事件
    k = 0  # 触发次数 k
    for i in range(0, t):  # 使用导弹次数 t
        if k > 2:
            break
        for ii in range(1, 5):
            if k > 2:
                break
            a = random.random()
            if a > p:
                break
            else:
                k = k + 1
    return k


for t in range(1, 21):  # 获得导弹次数 t -> 1~20，每次循环都是一个蒙特卡洛
    x = [0] * I  # 定义一个空的数组
    K = 0  # 总触发次数
    full = 0  # 满触发次数
    for i in range(0, I):
        x[i] += single_loop()
        K += x[i]
        if single_loop() == 3:  # 触发次数达到上限
            full += 1

    # 每一种单局导弹获取次数下，都做一张 触发次数 的概率分布图
    fig, ax = plt.subplots()
    ax.hist(x, bins=5, density=0, histtype='bar', facecolor='red', alpha=1, rwidth=0.4)
    plt.xticks(np.arange(0, 4, 1))
    plt.yticks(np.arange(0, 120000, 20000))
    ax.set_title('pdf-missile' + str(t))
    fig.subplots_adjust(hspace=0.4)
    plt.show()
    # 打印平均值
    print(t, K / I, full / I)
