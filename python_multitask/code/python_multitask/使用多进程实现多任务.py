# 1. 导入进程包
# 2. 使用进程类创建进程对象
# 3. 使用进程对象启动进程执行指定的任务。
import time
import multiprocessing

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


if __name__ == "__main__":
    t1 = time.time()
    task1 = multiprocessing.Process(target=sing)
    task2 = multiprocessing.Process(target=dance)
    task1.start()
    task2.start()
    t2 = time.time()

    print("执行程序所用的时间为：{0}".format(t2-t1))