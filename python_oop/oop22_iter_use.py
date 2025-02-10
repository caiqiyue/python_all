from typing import Any


class Person(object):
    def __init__(self) -> None:
        self.age = 1
        
    def __getitem__(self,item):
        self.age += 1
        if self.age >= 6:
            raise StopIteration
        else:
            return self.age

p = Person()

class Animal(object):
    def __init__(self):
        self.age = 1
    
    def __iter__(self):
        self.age = 1
        return self
    
    def __next__(self):
        self.age += 1
        if self.age >= 6:
            raise StopIteration
        else:
            return self.age
        
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.age += 1
        if self.age >= 6:
            raise StopIteration
        else:
            return self.age

#iter的第一种使用方式，调用 getitem
pt = iter(p)#iter会去p的内部，找iter,没有iter找getitem，然后根据getitem生成一个迭代器
print(pt)#<iterator object at 0x000001CA886D9550>
for i in pt:
    print(i)
    
    
# #调用  __iter__  和 __next__
a = Animal()
at = iter(a)#找到实例a内部的__iter__，iter返回的是 实例本身 所以 at还是 个实例 
print(a == at)
print(at)

for i in at:#  for i in a  --> 先是 b = iter(a) ---> 再 next(b) 赋值给 i 循环 next操作 
    print(i)
    


#iter第二种使用方式

#iter(a,4) #调用 传进去 的 a， 返回的数值 等于4 时，停止调用，且不返回4，只返回 4 之前的
"""
注意，此时的 iter（a,4） 不会再把 a转成 迭代器了，就是直接 循环调用  a ，并返回值
所以 现在 的 iter(a,4)的 写法是错误的，实例a ，可迭代，但不会被当做函数一样被调用
"""

#(1)  直接 把 实例a中的  __next__函数 传进去
al = iter(a.__next__,4)
print(al)
for item in al:
    print(item)#若 执行 a.__next__（）返回的结果 为 4 时，就停止再次调用它


#(2) 给 实例 a 添加 call 函数 ，让它可以像函数一样被调用，实例 a()  调用内部 call()，值等于4的时候，不再执行
k = iter(a,4)
for f in k:
    print(f)
