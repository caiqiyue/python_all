



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
    # def __init__(self):
    #     self.e = 1
        
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
"""
print(a_obj.a)
print(a_obj.b)