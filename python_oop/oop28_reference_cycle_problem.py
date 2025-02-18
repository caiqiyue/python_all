


"""
内存管理机制：引用计数器归零，则删除 内存中真正的实例对象

但是现在存在  内存泄露的问题，他可能是由  循环引用   导致的

比如，有两个实例对象，Person实例对象，被P引用 ； Dog实例对象，被d引用
此时，两个实例对象的 引用计数器都是 1

现在，p实例增加 属性pet，指向 实例d
d实例增加属性 master 指向 实例p
现在，的话，两个实例对象的引用计数都为2
如果 删除 变量d和p，那么两个实例对象 的引用计数 都-1，都变为了1，但不是 0（内部的属性互相引用），不会被系统当做垃圾
但此时，你没有  变量指向这两个 内存中的 实例对象 ，它又不会被 垃圾回收，
就出现了 内存泄露的问题



"""

import objgraph
class Person:
    pass

class Dog:
    pass
#objgraph.count('类名')可以跟踪 ，该类所创建的实例个数

p = Person()
d = Dog()

print(objgraph.count('Person'))#1
print(objgraph.count('Dog'))#1

p.pet = d
d.master = p

del p
del d

print(objgraph.count('Person'))#1，因为两个实例对象互相引用，所以引用计数器还是1，不会被销毁，只是没有变量指向他们，无法对他们操作
print(objgraph.count('Dog'))#1

#但是垃圾回收机制，会去解决这样的 循环引用的问题


