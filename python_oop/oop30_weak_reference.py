import gc
import objgraph

import weakref


class Person(object):
    def __del__(self):
        print("Person实例对象，被释放")
        
    pass

class Dog(object):
    def __del__(self):
        print("Dog实例对象，被释放")

"""
python中，有 强引用 和 弱引用 。强引用 会使得  该实例对象 的引用计数器 +1 ，而弱引用 不会让实例对象的引用计数器+1

现在 在内存中 有两个实例对象 变量p 指向 Person类 实例对象 ，变量 d指向 Dog实例对象， Person实例对象内部增加 属性pet指向
Dog实例对象； Dog实例对象 内部 增加 master 属性 弱引用 Person实例对象。因此，现在 Person实例对象的引用计数器 为 1；
Dog 实例对象引用计数器 为 2

现在删除 变量p和d的引用 ，Person实例对象引用计数器为0，Dog引用计数器为1，那么Person实例对象会被删除，与此同时，Person实例对象内部的
pet属性也会被删除，那么 pet属性对实例对象Dog的引用也会被删除，所以 Dog类实例对象的引用计数器 就会为0
这两个 内存中的 实例对象就会被  引用计数器机制 回收
"""
        
        
p = Person()
d = Dog()


#使用 弱引用 解决 循环引用
p.pet = d

# p.pets = weakref.WeakValueDictionary({'dog':d1,'cat':c1}) 一对多 引用时，可以使用 字典弱引用

d.master = weakref.ref(p)#将 强引用 改为 弱 引用


del p
del d 

#手动解决循环引用的方式2 在删除前 破解循环引用

# p.pet = d
# d.master = p

# p.pet = None
# del p
# del d


print(objgraph.count("Person"))
print(objgraph.count("Dog"))