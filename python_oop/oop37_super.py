



class B(object):
    a = 1
    def __init__(self):
        self.b = 10
        
    def t1(self):
        print("t1")
        
    @classmethod
    def t2(cls):
        print("t2")
    
    @staticmethod
    def t3():
        print("t3")
        
        
class A(B):
    v = 1
    
    def __init__(self):
        """
        如果子类不仅想继承父类的实例属性，还想新增自己的实例属性，那就得在自己的init方法执行前，执行父类的init方法
        """
        # self.__init__() 这样会陷入循环调用，错误
        # b = B() b.init() 这样传入的self是实例b，而非实例a，那么就是给实例b新增实例属性了
        B.__init__(self)#使用类去调用init方法，给self ---> 实例a，继承父类的实例属性
        #但是这样的写法，有问题，父类名称修改，子类要动代码很麻烦；对于菱形继承，会重复调用父类、爷类的init方法
        #此外，在经典类中，没有super，只能这样使用
        self.p = 10
        
    def tt1(self):
        print("tt1")
        
    @classmethod
    def tt2(cls):
        print("tt2")
        
    @staticmethod
    def tt3():
        print("tt3")
        
a_obj = A()
print(a_obj.a)
print(a_obj.b)#由于A类有自己的init方法，导致不会去执行B类的init方法，那么实例a就不会有实例属性b 