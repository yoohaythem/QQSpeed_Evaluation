import numpy.random as random
import time
import math

start = time.time()

p = [0.88, 0.525, 0.403, 0.225, 0.12, 0.055, 0.03, 0.02, 0.01, 0.004, 0.002, 0.001]  # 官方公布的打造概率
I = 20000  # 蒙特卡洛模拟次数
K = 0


def single_loop():  # 蒙特卡洛的单次随机事件
    k = 0  # 消耗祈愿卡数量
    for i in range(0, 12):  # 打造进度数
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
