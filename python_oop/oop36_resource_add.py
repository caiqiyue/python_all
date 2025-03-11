



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
"""
A继承了B的所有资源，但需要注意一下，a_obj.a，是B类的a类属性，但是 a_obj.b是A自己的实例属性b
因为，a_obj = A()创建时，调用init方法，自己没有，就去找父类B的init方法，但是是A类调用B类的init方法
所以init方法中传入的self是 实例a_obj，所以就是借用B的init方法，给实例a增加了个实例属性b

资源的累加，可以让子类不仅继承父类的类属性，实例属性，实例方法，类方法，还有静态方法
同样，也可以在自身基础上新增这五种资源
不过，就是在新增实例属性的时候，会覆盖父类的init方法，从而导致，继承不了父类的实例属性
"""
print(a_obj.a)
print(a_obj.b)#由于A类有自己的init方法，导致不会去执行B类的init方法，那么实例a就不会有实例属性b 