class Animal:
    _x = 10
    def run(self):
        """
        类的内部访问  受保护属性
        """
        print(self._x)
        print(Animal._x)
    pass

class Dog(Animal):
    def run2(self):
        """
        子类内部访问 受保护属性
        """
        print(self._x)
        print(Dog._x)
    pass




#测试  类的内部访问  受保护属性
a = Animal()
a.run()

#子类内部访问  受保护属性
d = Dog()
d.run2()

#模块内部访问  受保护属性
print(Animal._x)
print(Dog._x)
print(d._x)
print(a._x)


__all__ = ["_v"]  #这句话的意思就表示   受保护属性 _v 可以被导入 ，跨模块访问的时候  ，可以 直接访问  _v


#受保护变量   在  跨模块访问时  可以   模块._v  但不可以   直接跨模块访问 _v  了，因为受保护属性 不会被导入
_v = 666 