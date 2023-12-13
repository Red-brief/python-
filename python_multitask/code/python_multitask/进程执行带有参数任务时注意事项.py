# 1. 导入进程包
# 2. 使用进程类创建进程对象
# 3. 使用进程对象启动进程执行指定的任务。
import time
import multiprocessing

# 唱歌
def sing(name, num):
    for i in range(num):
        print("{}在唱歌...".format(name))
        time.sleep(0.5)


# 跳舞
def dance(num, name):
    for i in range(num):
        print("{}在跳舞...".format(name))
        time.sleep(0.5)


if __name__ == "__main__":
    t1 = time.time()
    # 注意元组只存在一个元素的时候，要在元组的末尾加上一个 逗号
    '''
    args: 使用元组方式给指定任务传参
        传递多个参数，元组的元素顺序就是任务的参数顺序
    kwargs : 使用字典方式给指定任务传参
            key 名 就是参数的名字
    '''
    task1 = multiprocessing.Process(target=sing, args=("小明", 5))
    task2 = multiprocessing.Process(target=dance, kwargs={"num": 6, "name": "小花"})
    task1.start()
    task2.start()
    t2 = time.time()

    print("执行程序所用的时间为：{0}".format(t2-t1))