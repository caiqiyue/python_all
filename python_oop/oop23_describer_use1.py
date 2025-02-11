class Person(object):
    def __init__(self) -> None:
        self.__age = 1
    
    def get_age(self):
        return self.__age
    
    def set_age(self,value):
        if value >= 0:
            self.__age = value
    
    def del_age(self):
        del self.__age
        
    age = property(get_age,set_age,del_age)#此时的age属性就是  数据描述器
    
    
class Dog(object):
    def __init__(self) -> None:
        self.__age = 10
    """
    此时的age也是一个  数据描述器
    """
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if value>=0:
            self.__age = value
    @age.deleter
    def age(self):
        del self.__age
        

p = Person()

print(p.age)

p.age = 100

print(p.age)
