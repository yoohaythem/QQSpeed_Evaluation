import numpy.random as random
import time
import math

start = time.time()
p = [0.47, 0.425, 0.13, 0.075, 0.04, 0.015, 0.01, 0.01]  # 官方公布的打造概率
I = 200000  # 蒙特卡洛模拟次数
K = 0


def single_loop():  # 蒙特卡洛的单次随机事件
    k = 0  # 消耗宠物能源数量
    for i in range(0, 8):  # 打造进度数
        while True:  # 死循环
            k = k + 1
            a = random.random()
            if a < p[i]:  # 循环出口
                break
    return 9 * math.ceil(k / 10)  # 十连抽向上取整


for i in range(0, I):
    K += single_loop()
print(K / I)

end = time.time()
print("运行时间:%.2f秒" % (end - start))
