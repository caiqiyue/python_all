import sys



class Person(object):
    pass


p1 = Person()#创建一个Person实例对象，分配一块内存地址，变量p1引用该内存地址

print(sys.getrefcount(p1))#打印该 实例对象 被多少个变量引用（传入函数，也算引用），所以这里的引用个数 是 2



p2 = p1#等于号，即赋值  把p1的值（内存地址）赋值给p2，所以此处的 p2指向的是 Person实例对象

print(sys.getrefcount(p2))# person实例对象 有三个引用个数了

del p1#这也证明了，p2并不是指向p1，而是指向 实例对象
print(sys.getrefcount(p2))

#当 内存中的 某一对象 的被引用个数 为0，则 它的就会被系统认为是 垃圾 被回收