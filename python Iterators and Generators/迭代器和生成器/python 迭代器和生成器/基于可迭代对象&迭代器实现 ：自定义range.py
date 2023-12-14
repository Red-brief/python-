# # 基于可迭代对象 & 迭代器 实现：自定义 range
# class IterRange(object):
#     def __init__(self, num):
#         self.num = num
#         self.counter = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.counter += 1
#
#         if self.counter == self.num:
#             raise StopIteration()
#         return self.counter
#
#
# class Xrange(object):
#     def __init__(self, max_num):
#         self.max_num = max_num
#
#     def __iter__(self):
#         return IterRange(self.max_num)
#
# obj = Xrange(100)
#
# for item in obj:
#     print(item)
#
#

# # 基于可迭代对象& 生成器，实现:自定义 range
# class Xrange(object):
#     def __init__(self, max_num):
#         self.max_num = max_num
#
#     def __iter__(self):
#         counter = 0
#         while counter < self.max_num:
#             yield counter
#             counter += 1
#
#
# obj = Xrange(100)
# for item in obj:
#     print(item)

from collections.abc import Iterator, Iterable
v1 = [11, 22, 33]
print(isinstance(v1, Iterator))  # false  ,判断是否是迭代器,判断依据是 __iter__ 和 __next__
v2 = v1.__iter__()
print(isinstance(v2, Iterator))  # True

print(isinstance(v1, Iterable))  # True， 判断依据是是否有 __iter__ 且返回迭代器对象

print(isinstance(v2, Iterable))  # True  判断依据是是否有 __iter__ 且返回迭代器对象.
