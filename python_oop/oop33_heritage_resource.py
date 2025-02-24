

class Animal(object):
    a = 1#普通类属性
    _b = 2#受保护类属性
    __c = 3#伪私有类属性
    
    def __init__(self) -> None:#内置方法
        print('Animal init')
        
    def test1(self):#普通实例方法
        print("Animal 1")
        
    def _test2(self):#受保护的实例方法
        print("Animal 2")
        
    def __test3(self):#伪私有的实例方法
        print('Animal 3')
        

class Person(Animal):
    def test(self):
        print(self.a)#可以继承普通类属性
        print(self._b)#可以继承受保护属性
        # print(self.__c) 不可继承伪私有属性或方法
        self.test1()
        self._test2()
        # self.__test3()
        self.__init__()#内置方法也可以继承

        
"""
同样，需要注意，继承 继承的资源的使用权，而不是复制一份父类的资源到自己中
"""
p = Person()
p.test()
#子类和父类的a 是同一个地址，说明 子类只是继承了父类的资源使用权
print(id(p.a))#1797881030960
print(id(Animal.a))#1797881030960