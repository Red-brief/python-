# python 装饰器

## 1.装饰器思路与构成原理

```python
"""
需求：请实现在函数执行前输入before, 执行后输出afetr
"""
def func():
    print("我是func 函数")
    value = (11,22,33,44)
    return value

result = func()
print(result)


#  思路一
def func():
    print("before")
    
    print("我是func函数")
    value = (11,22,33,44)
    
    print("after")
    return value

result = func()
print(result)

# 思路二
def func():
    print("我是func函数")
    value = (11,22,33,44)
    return value

def outer(origin):
    def inner():
        print("before")
        result = origin()  # 调用原来的func函数
        print("after")
        return result
    return inner

#  执行outer() 函数 返回 inner 函数
func = outer(func)    
result = func()
print(result)

```

## 2.python 中的特殊语法@ 符号实现装饰器

```python
"""
python中支持特殊语法，在某个函数上方使用
@函数名
def xxx():
	pass
python 内部会自动执行 函数名(xxx), 执行完之后，再将结果赋值给 xxx
xxx = 函数名(xxx)

"""

def outer(origin):
    def inner():
        print("before")
        res = origin()  #调用原来的func 函数
        print("after")
        return res
    return inner
@outer # func = outer(func)
def func():
    print("我是func函数")
    value = (11,22,33,44)
    return value

result = func()
print(result)
```

## 3.在多个函数执行前或者执行后添加同样的功能

```python
"""
在多个函数执行前加上 before，执行后加上afetr
"""
# 思路一， 直接在函数里面添加相关的语句
def func1():
    print("before")
    print("我是func1函数")
    print("after")
    value = (11,22,33,44)
    return value

def func2():
    print("before")
    print("我是func2函数")
    print("after")
    value = (11,22,33,44)
    return value

def func3():
    print("before")
    print("我是func3函数")
    print("after")
    value = (11,22,33,44)
    return  value

func1()
func2()
func3()


# 思路二

def outer(origin):
    def inner():
        print("before")
        result = origin()  # 调用原来的func 函数
        print("after")
        return result
    return inner

@outer
def func1():
    print("我是func1函数")
    value = (11,22,33,44)
    return value
@outer
def func2():
    print("我是func2函数")
    value = (11,22,33,44)
    return value
@outer
def func3():
    print("我是func3函数")
    value = (11,22,33,44)
    return value

func1()
func2()
func3()
```

## 4.支持装饰有任意个值参数和键值对参数的函数

```python
def outer(origin):
    def inner(*args, **kwargs):
        print("before")
        result = origin(*args, **kwargws)  # 调用原来的func 函数
        print("after")
        return result
    return inner

@outer
def func1():
    print("我是func1函数")
    value = (11,22,33,44)
    return value
@outer
def func2():
    print("我是func2函数")
    value = (11,22,33,44)
    return value
@outer
def func3():
    print("我是func3函数")
    value = (11,22,33,44)
    return value

func1(a1)
func2(a2,a3)
func3(name="xxx")
```

## 5.总结

```python
# 实现原理： 基于@语法和函数闭包，将原函数封装在闭包中，然后将函数赋值为一个新的函数（内层函数),执行函数时再在内层函数中执行闭包中的原函数。
# 实现效果：可以在不改变原函数内部代码 和调用方式的前提下，实现在函数执行和执行扩展功能。
#适用场景： 多个函数系统统一在执行前后自定义一些功能。

# 装饰器示例

def outer(origin):
    def inner(*args,**kwargs):
        # 执行前
        res = origin(*args, **kwargs)  # 调用原来的func 函数
        # 执行后
        return res
    return inner

@outer
def func():
    pass
func()

```



## 6.扩展

```python
from flask import Flask

app = Flask(__name__)


def auth(func):
    def inner(*args, **kwargs):
        # 判断用户是否已经登录，已登录继续往下走，未登录则返回登录页面
        res = func(*args,**kwargs)  # 执行原函数
        return res
    return inner


@auth
def index():
    return "首页"


@auth
def info():
    return "用户中心"


@auth
def order():
    return "订单中心"


def login():
    return "登录界面"


app.add_url_rule("/index/",view_func=index)
app.add_url_rule("/info/",view_func=info)
app.add_url_rule("/order/",view_func=order)
app.add_url_rule("/login/",view_func=login)

app.run()


```

### functools  扩展

```python
import functools


def auth(func):
    @functools.wraps(func)  # inner.__name__ = admin.__name__    inner.__doc__ = admin.__doc__
    def inner(*args, **kwargs):
        """This inner function for __name__ test"""
        res = func(*args,**kwargs)  # 执行原函数
        return res
    return inner


@auth
def admin():
    """ This a admin function for __doc__  test"""
    print(123)


def rbac():
    print("rbac")


# 函数名 + （）
admin()

# 被装饰器装饰前
# print(admin.__name__)  # "admin"
# print(admin.__doc__)   # 获取函数的注释
# rbac()


#被装饰器装饰后
# print(admin.__name__)   # 返回的函数名变成了 inner
# print(admin.__doc__)    # 返回的注释内容也变成了 inner 里的

# 需求： 如果我用装饰器装饰了某个函数，但是我还是想在打印 函数名.__name__  或者 函数名.__doc__ 时, 仍然 打印被装饰器装饰前的内容
# 那么就可以在 装饰器 函数里面使用 functools.wraps(func)

print(admin.__name__)
print(admin.__doc__)



# 最后的装饰的写法

import functools


def outer(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        # 函数执行前
        res = func(*args, **kwargs)  # 执行原函数
        return res
    return inner 
```