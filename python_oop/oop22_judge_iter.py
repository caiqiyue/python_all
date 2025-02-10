import collections

class MyIterator(object):
    def __init__(self) -> None:
        self.age = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.age > 6:
            raise StopIteration("越界")
        self.age += 1
        return self.age
    
    

myiter = MyIterator()

for i in myiter:
    print(i)
    
print(isinstance(myiter,collections.Iterator))#判断是否是迭代器，迭代器必须包含 __next__  和  __iter__

print(isinstance(myiter,collections.Iterable))#判断是否是 可迭代对象  只需要包含 __iter__,且一定可以 被 for in 遍历

"""
但是可以被 for in 的 不一定是 可迭代对象 ，因为 只要含有 __getitem__ 也可以被 for in 遍历 ，但它不是可迭代对象

所以通常来说，想要让自定义的类，可以被 for in遍历 ，有两种方法  __iter__ 和 __next__     第二种就是 __getitem__
"""






