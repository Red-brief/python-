# 1.迭代器

## 1.迭代器的定义

```text
1. 当类中定义了__iter__ 和 __next__两个方法。
2.__iter__方法需要返回对象本身，即：self
3.__next__方法，返回下一个数据，如果没有数据了，则需要抛出一个StopIteration的异常
官方文档：https://docs.python.org/3/library/stdtypes.html #iterator-types
```

```python
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
```

## 2.生成器

```python
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
```

## 3.可迭代对象

```python
#如果一个类中有__iter__方法且返回一个可迭代对象，则我们称这个类创建的对象为可迭代对象。

class FOO(object):
    def __iter__(self):
        return 迭代器对象（生成器对象）
obj = FOO()
# 可迭代对象使可以使用 for 来进行循环，在循环的内部其实是先执行 __iter__方法，获取其迭代器对象，然后再在内部执行这个迭代器对象的next功能，逐步取值。

for item  in obj:
    pass
```

```python
class IT(object):
    def __inti__(self):
        self.counter = 0
     
    def __iter__(self):
        return self
    
    def __next__(self):
        self.counter += 1
        if self.counter == 3:
            raise StopIteration()
         return self.counter
class Foo(object):
    def __iter__(self):
        return IT()
    
obj = FOO() # 可迭代对象

for item in obj:
    print(item)
```

```python
# 基于可迭代对象 & 迭代器 实现：自定义 range
class IterRange(object):
    def __init__(self, num):
        self.num = num
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1

        if self.counter == self.num:
            raise StopIteration()
        return self.counter


class Xrange(object):
    def __init__(self, max_num):
        self.max_num = max_num

    def __iter__(self):
        return IterRange(self.max_num)

obj = Xrange(100)

for item in obj:
    print(item)



```

```python
class FOO(object):
    def __iter__(self):
        yield 1
        yield 2
obj = FOO()
for item in obj:
    print(item)
```

```python
# 基于可迭代对象& 生成器，实现:自定义 range
class Xrange(object):
    def __init__(self,max_num):
    	self.max_num = max_num
    def __iter__(self):
        counter = 0
        while counter < self.max_num:
            yield counter
            counter += 1
        
obj = Xrange(100)
for item in obj:
    print(item)
    
    
```

## 4.常见的数据类型

```python
v1 = list([11,22,33,44])

v1 是一个可迭代对象，因为在列表中声明了一个__iter__方法 并且返回一个可迭代对象

>>> v1 = list([11,22,33,44])
>>> dir(v1)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> v2 = v1.__iter__()
>>> dir(v2)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__length_hint__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__']
>>> v2.__next__()
11
>>> v2.__next__()
22
>>> v2.__next__()
33
>>> v2.__next__()
44
>>> v2.__next__()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    v2.__next__()
StopIteration
>>> 
```

## 5.如何判断一个对象是不是可迭代对象或者 迭代器

```python
from collections.abc import Iterator, Iterable
v1 = [11, 22, 33]
print(isinstance(v1, Iterator))  # false  ,判断是否是迭代器,判断依据是 __iter__ 和 __next__
v2 = v1.__iter__()
print(isinstance(v2, Iterator))  # True

print(isinstance(v1, Iterable))  # True， 判断依据是是否有 __iter__ 且返回迭代器对象

print(isinstance(v2, Iterable))  # True  判断依据是是否有 __iter__ 且返回迭代器对象.

```

