
import gc



gc.disable()#关闭垃圾回收机制
gc.enable()#开启垃圾回收机制

print(gc.isenabled())#判断垃圾回收机制是否开启

print(gc.get_threshold())

"""
垃圾回收机制，是一个耗时耗力的机制，所以并不会每次都触发。只要达到一定阈值的时候，才会触发

对于循环引用来说，它不一定会被立即解决，也只有在触发垃圾回收时，才会解决该问题
那么就需要手动触发垃圾回收
"""

import objgraph

class Person(object):
    pass

class Dog(object):
    pass

p = Person()
d = Dog()

#循环引用  master 和 pet 虽然也 指向 内存中的实例对象 ，但是 当 p 和 d 被删除之后，无法通过 master 和 pet 访问 实例对象，称为 不可到达引用
p.pet = d  
d.master = p

# p 和 d指向 两个 内存中的 实例对象 称为  可到达引用
del p
del d
#gc.disable() 而且手动触发垃圾回收，不管垃圾回收机制 是否开启
gc.collect()#如果不手动触发，垃圾回收机制，那么 两个实例对象 的引用计数 都是 1， collect()就是 解决循环引用问题之后，回收这两个实例对象

#collect(generation) ，可以手动输入 第几代  输入 0，就是 0代回收  1就是 0，1代回收 2，就是 0，1，2代回收


print(objgraph.count("Person"))
print(objgraph.count("Dog"))


