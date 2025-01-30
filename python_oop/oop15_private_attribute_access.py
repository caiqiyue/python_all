class Animal:
    __x = 10
    def run(self):
        """
        类的内部访问  私有属性   私有属性 只有  本类的内部可以访问  其余地方都不可以访问
        """
        print(self.__x)
        print(Animal.__x)
    pass

class Dog(Animal):
    def run2(self):
        """
        子类内部访问 私有属性
        """
        print(self.__x)
        print(Dog.__x)
    pass


"""
{'__module__': '__main__', '_Animal__x': 10, 'run': <function Animal.run at 0x0000021EAB215EE0>, 
'__dict__': <attribute '__dict__' of 'Animal' objects>, '__weakref__': <attribute '__weakref__' of 'Animal' objects>,
'__doc__': None}
"""
print(Animal.__dict__)
print(Animal._Animal__x)#私有属性的特殊访问方法，也证明了  它本质上是伪私有，并不是  真私有
#print(Animal.__x)#这样是访问不了的

# #测试  类的内部访问  私有属性
# a = Animal()
# a.run()

# #子类内部访问  私有属性
# d = Dog()
# d.run2()

# #模块内部访问  私有属性
# print(Animal.__x)
# print(Dog.__x)
# print(d.__x)
# print(a.__x)


# __all__ = ["__v"]  #这句话的意思就表示   受保护属性 _v 可以被导入 ，跨模块访问的时候  ，可以 直接访问  _v


# #受保护变量   在  跨模块访问时  可以   模块._v  但不可以   直接跨模块访问 _v  了，因为受保护属性 不会被导入
# __v = 666 #只有在类的内部 __v才会被当做是私有属性
#           #在的类的外部   __v就被当作了  以 下划线为开头  的  受保护属性  不存在   模块中定义的  私有变量