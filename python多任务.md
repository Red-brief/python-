# python 进程



![image-20231209202600127](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231209202600127.png)



![image-20231209202824214](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231209202824214.png)

```python
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
    sing()
    dance()
```

```python
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
```

![image-20231210141029305](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231210141029305.png)

![image-20231210141125144](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231210141125144.png)

![image-20231210141201522](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231210141201522.png)

```python 
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
```

![image-20231210144305139](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231210144305139.png)

![image-20231210144350914](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231210144350914.png)

![image-20231210144438419](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231210144438419.png)

![image-20231210145013539](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231210145013539.png)

```python
# 1. 导入进程包
# 2. 使用进程类创建进程对象
# 3. 使用进程对象启动进程执行指定的任务。
import time
import os
import multiprocessing

# 唱歌
def sing(name, num):
    print("获取唱歌进程的pid{}".format(os.getpid()))
    print("获取唱歌进程的父进程的pid{}".format(os.getppid()))
    for i in range(num):
        print("{}在唱歌...".format(name))
        time.sleep(0.5)


# 跳舞
def dance(num, name):
    print("获取跳舞进程的pid{}".format(os.getpid()))
    print("获取跳舞进程的父进程的pid{}".format(os.getppid()))
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
    print("获取主进程的pid{}".format(os.getpid()))

    print("执行程序所用的时间为：{0}".format(t2-t1))
```

![image-20231210145735635](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231210145735635.png)

![image-20231210145809477](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231210145809477.png)

![image-20231210150100660](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231210150100660.png)

```python
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

```

```python
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

```

![image-20231210151352925](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231210151352925.png)

![image-20231210211159588](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231210211159588.png)

```python
import os
import multiprocessing


def copy_file(file_name, source_dir, dest_dir):
    # 1.拼接源文件路径和目标文件路径
    source_path = source_dir + "/" + file_name
    dest_path = dest_dir + "/" + file_name
    # 2.打开源文件和目标文件
    with open(source_path, "rb") as source_file:
        with open(dest_path, "wb") as dest_file:
            # 3.循环读取源文件到目标路径
            while True:
                data = source_file.read(1024)
                if data:
                    dest_file.write(data)
                else:
                    break


if __name__ == "__main__":
    # 1. 定义源文件夹和目标文件夹
    source_dir = "C:\\Users\Administrator\Desktop\学习资料\未完成的笔记"
    dest_dir = "C:\\Users\Administrator\Desktop\\test"
    # 2.创建目标文件夹
    try:
        os.mkdir(dest_dir)
    except:
        print("目标文件夹已经存在")
    # 3. 读取源文件夹的文件列表
    file_list = os.listdir(source_dir)
    # 4. 遍历文件列表实现拷贝
    for file_name in file_list:
        # copy_file(file_name, source_dir, dest_dir)
        # 5. 使用多进程实现多任务拷贝
        sub_process = multiprocessing.Process(target=copy_file, args=(file_name, source_dir, dest_dir))
        sub_process.start()

```

# python 线程

![image-20231210215253770](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231210215253770.png)

![image-20231210215725238](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231210215725238.png)

![image-20231210215806166](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231210215806166.png)

![image-20231211202919215](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231211202919215.png)

![image-20231211203153488](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231211203153488.png)

![image-20231211203258447](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231211203258447.png)

```python'
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
```

![image-20231211205544909](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231211205544909.png)

```python
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

```

![image-20231211210254885](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231211210254885.png)

![image-20231211210957431](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231211210957431.png)

```python
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
```

![image-20231211212150343](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231211212150343.png)

```python
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
```

![image-20231211212241941](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231211212241941.png)

![image-20231211212313891](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231211212313891.png)

![image-20231211212501155](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231211212501155.png)

```python
import os
import threading


def copy_file(file_name, source_dir, dest_dir):
    # 1. 拼接源文件路径和目标文件路径
    source_path = source_dir + "/" + file_name
    dest_path = dest_dir + "/" + file_name

    # 2. 打开源文件和目标文件
    with open(source_path, "rb") as source_file:
        with open(dest_path, "wb") as dest_file:
            # 3.  循环读取源文件到目标路径
            while True:
                data = source_file.read(1024)
                if data:
                    dest_file.write(data)
                else:
                    break


if __name__ == "__main__":
    # 1.定义源文件夹 和目标文件夹
    source_dir = r"C:\Users\Administrator\Pictures\Screenshots"
    dest_dir = r"C:\Users\Administrator\Desktop\test"
    # 2. 创建目标文件夹
    try:
        os.mkdir(dest_dir)
    except:
        print("目标文件夹已经存在")
    # 3. 读取源文件夹的文件列表
    file_list = os.listdir(source_dir)
    # 4. 遍历文件列表实现拷贝
    for file_name in file_list:
        # 使用多线程实现多任务拷贝
        sub_thread = threading.Thread(target=copy_file, args=(file_name, source_dir, dest_dir))
        sub_thread.start()


```

![image-20231212195805795](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231212195805795.png)

![image-20231212195827882](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231212195827882.png)