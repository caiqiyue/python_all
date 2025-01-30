class Animal:
    x = 10
    def run(self):
        """
        类的内部访问  公有属性
        """
        print(self.x)
        print(Animal.x)
    pass

class Dog(Animal):
    def run2(self):
        """
        子类内部访问 公有属性
        """
        print(self.x)
        print(Dog.x)
    pass




#测试  类的内部访问  公有属性
a = Animal()
a.run()

#子类内部访问  公有属性
d = Dog()
d.run2()

#模块内部访问  公有属性
print(Animal.x)
print(Dog.x)
print(d.x)
print(a.x)



#公有变量
v = 666