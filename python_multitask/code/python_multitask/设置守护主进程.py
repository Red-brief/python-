import time
import multiprocessing


def work():
    for i in range(10):
        print("工作中...")
        time.sleep(2)


if __name__ == "__main__":
    # 创建子进程
    work_process = multiprocessing.Process(target=work)
    # 设置守护主进程，主进程退出后子进程直接销毁，不再执行子进程中的代码
    work_process.daemon = True
    work_process.start()
    # 让主进程等待 1秒钟
    time.sleep(1)
    print("主进程执行完成了")
    # 主进程会等待所有的子进程执行完成以后程序再推出
