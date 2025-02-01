
class Animal(object):
    pass

class Person(Animal):
    """
    类的描述信息
    """
    
    age = 10
    
    def run(self):
        print("run")
        
        

print(Person.__dict__)
print(Person.__bases__)#父类，继承于哪个类
print(Person.__doc__)
print(Person.__name__)
print(Person.__module__)#<class '__main__.Animal'> 可以看到 这个 main.Animal  这也是导致模块调包的时候产生的一些问题   这个需要到  模块和包  知识的时候 才知道
print(Person.__class__)#创造它的是什么类

p = Person()

print(p.__dict__)
print(p.__class__)