

import abc

class Animal(object,metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def jiao(self):
        pass
    
    
    @abc.abstractclassmethod
    def test(cls):
        pass
    
    
class Dog(Animal):
    def jiao(self):
        print("wangwang")
        
        
    @classmethod
    def test(cls):
        print("Dog")
        
        
d = Dog()
d.jiao()
d.test()