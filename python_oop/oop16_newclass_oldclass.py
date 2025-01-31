class Person:
    pass


#以后最好都这样写
class Animal(object):
    pass


#查看  person类  的 基类还是 父类 
print(Person.__bases__)#(<class 'object'>,)，说明它是新式类 python2，要手动继承于object，python3自动继承于object

