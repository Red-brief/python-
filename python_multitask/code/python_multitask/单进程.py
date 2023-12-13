import time


# 唱歌
def sing():
    for i in range(3):
        print("唱歌...")
        time.sleep(0.5)


# 跳舞
def dance():
    for i in range(3):
        print("跳舞...")
        time.sleep(0.5)


if __name__ == '__main__':
    time1 = time.time()
    sing()
    dance()
    time2 = time.time()
    print("执行程序所用的时间为：{0}".format(time2-time1))