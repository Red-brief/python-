import time
import threading


def work():
    for i in range(10):
        print("工作...")
        time.sleep(0.2)


if __name__ == "__main__":
    # sub_thread = threading.Thread(target=work)
    # sub_thread.start()

    # 主线程结束不想等待子线程结束再结束，可以设置守护主线程
    # sub_thread = threading.Thread(target=work, daemon=True)
    # sub_thread.start()

    sub_thread = threading.Thread(target=work)
    # 线程对象.setDaemon(True) ,这样也可以吧线程设置为守护线程
    sub_thread.setDaemon(True)
    sub_thread.start()

    # 主线程等待1s,后结束
    time.sleep(1)
    print("主线程结束了")

# 主线程会等待所有的子线程执行结束后再结束