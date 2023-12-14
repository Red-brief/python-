# 创建 生成器函数
def func():
    yield 1
    yield 2


# 创建生成器对象（内部使根据生成器类generator创建的对象），生成器类的内部也声明了，__iter__, __next__ 方法
obj1 = func()
v1 = next(obj1)
print(v1)

v2 = next(obj1)
print(v2)

v3 = next(obj1)
print(v3)

obj2 = func()

for item in obj2:
    print(item)

# 如果按照 迭代器的规则来看，其实生成器类 也是一种特殊的迭代器类