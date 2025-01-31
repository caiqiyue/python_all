class Person(object):
    
    __age = 10
    
    def setAge(self,age):
        self.__age = age
        
    def getAge(self):
        return self.__age
    
    #这就是  property的第一种使用方式  定义好函数，然后 按照  get set del doc 的顺序写到property中
    age = property(getAge,setAge)
    

p = Person()

print(p.age)

p.age = 1902#这次，并不是 创建实例属性，，而是对 类的私有属性进行设置

print(p.age)
print(p.__dict__)

#===============================================================
class Animal(object):
    def __init__(self) -> None:
        self.__count = 100
    
    
    #property的第二种用法，对于获取值 用property装饰，设置值 用 属性.setter  来装饰 
    #property的作用就是将函数和方法关联起来
    @property
    def count(self):
        return self.__count
    
    @count.setter
    def count(self,count):
        self.__count = count
        
a = Animal()
print(a.count)

a.count = 102#这样也不会 创建 实例属性 是对私有属性进行设置
print(a.count)

print(a.__dict__)
    
    
    