import threading
import time

# 结论： 多线程之间的执行是无序的，由 cpu 调度决定
def task():
    time.sleep(1)
    # current_thread : 获取当前线程的线程对象
    thread_message = threading.current_thread()
    print(thread_message)


if __name__ == "__main__":
    for i in range(5):
        sub_thread = threading.Thread(target=task)
        sub_thread.start()