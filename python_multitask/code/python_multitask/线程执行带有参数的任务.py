import time
import threading


def sing(num):
    for i in range(num):
        print("正在唱歌")


def dance(num):
    for i in range(num):
        print("正在跳舞")


if __name__ == "__main__":
    # 创建子线程
    sub_thread = threading.Thread(target=sing, args=(5,))
    sub_thread2 = threading.Thread(target=dance, kwargs={"num": 3})
    sub_thread.start()
    sub_thread2.start()
