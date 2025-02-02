class Person(object):
    
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        
    def __str__(self) -> str:
        #print(p1)  或者   str(p1)  的时候，调用的就是   __str__  这个内置方法
        #不过这个内置方法 ，主要面向用户  让用户看看到易理解的输出
        return "name:{}  age:{}".format(self.name,self.age)
    
    
    def __repr__(self) -> str:
        #这个方法和str类似，不过他主要是打印  实例的   内存地址 模块等  给开发人员看的信息
        #此外 ，使用 print(),str()的时候，会先去寻找__str__，如果没有，才会再去找repr方法
        return "xxxxx"
        
p1 = Person("caiqiyue",19)

#print 本质上也是 调用 Person  用于信息打印的 内置方法，如果你自己不重写它，它默认打印  实例的内存地址
print(p1)
#str()也是调用  __str__内置方法
s = str(p1)
print(s)

#查看实例的  本质信息  内存地址 模块等信息  repr（）或者 交互模式下  查看 p1实例  都会调用 类的中 __repr__ 这个内置函数
print(repr(p1))


#如果有很多个实例，每次都这样写很麻烦，所以希望重写  Person的  信息打印 的 内置方法  ，print（p1）的时候 直接格式化打印信息
# print(p1.age)
# print(p1.name)

import datetime

t = datetime.datetime.now()
print(t)#2025-02-02 13:56:44.236569  调用 t内置的__str__方法

print(repr(t))#datetime.datetime(2025, 2, 2, 13, 56, 44, 236569)  调用 __repr__方法，返回的是datetime对象，但是把他作为字符串打印出来

a = eval(repr(t))#2025-02-02 13:56:44.236569  eval()就是把字符串当做python代码运行，将字符串重新变成了 datetime对象，然后print()调用了__str__
print(a)

