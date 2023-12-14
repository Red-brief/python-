# 创建迭代器类型
class IT(object):
    def __init__(self):
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == 3:
            raise StopIteration()
        return self.counter


# 根据类实例化创建一个迭代器对象
obj1 = IT()
# v1 = obj1.__next__()
# v2 = obj1.__next__()
# v3 = obj1.__next__()  # 抛出异常
v1 = next(obj1)
print(v1)

v2 = next(obj1)
print(v2)

v3 = next(obj1)
print(v3)

obj2 = IT()
for item in obj2:  # for 循环 首先会执行 迭代器对象 的 __iter__ 方法并获取返回值，一直去反复的执行 next(对象）
    print(item)

# 迭代器 对象支持 通过 next 取值，如果取值结束则自动抛出StopIteration
# for 循环内部在循环时，先执行__iter__方法，获取一个迭代器对象，然后不断执行的next 取值（有异常StopIteration则中止循环）