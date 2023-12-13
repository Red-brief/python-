import threading
import time


def dance():
    for i in range(3):
        print("正在跳舞")
        time.sleep(3)



def sing():
    for i in range(3):
        print("正在唱歌")
        time.sleep(3)


if __name__ == "__main__":
    # 创建子线程
    sing_thread = threading.Thread(target=sing)
    # 创建子线程
    dance_thread = threading.Thread(target=dance)
    # 启动线程
    sing_thread.start()
    dance_thread.start()


