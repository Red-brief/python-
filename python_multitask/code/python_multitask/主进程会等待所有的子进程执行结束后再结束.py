import time
import multiprocessing


def work():
    for i in range(10):
        print("工作中...")
        time.sleep(2)


if __name__ == "__main__":
    # 创建子进程
    work_process = multiprocessing.Process(target=work)
    work_process.start()
    # 让主进程等待 1分钟
    time.sleep(1)
    print("主进程执行完成了")
    # 主进程会等待所有的子进程执行完成以后程序再推出
