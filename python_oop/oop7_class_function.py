def eat():
    print(1)
    print(2)

eat()

class Person:
    #这是一个实例方法
    def eat(self):
        print("eat",self)#<__main__.Person object at 0x000001A203064340>
    
    #这是一个类方法
    @classmethod
    def run(cls):
        print("run",cls)
    
    #这是一个静态方法
    @staticmethod
    def drink():
        print("drink")


# p = Person()
# p.eat()
# print(p)#<__main__.Person object at 0x0000023DA5144340>

Person.run()#<class '__main__.Person'>
print(Person)#<class '__main__.Person'>


p = Person()#静态方法实例还是类都可以调用
p.drink()
Person.drink()


#可以看到不管什么方法都存储在类中，具体点，是类的dict中，和属性一样，存在一起
print(p.__dict__)#{}
print(Person.__dict__)#{'__module__': '__main__', 'eat': <function Person.eat at 0x000002908F2358B0>, 'run': <classmethod object at 0x000002908F157460>, 'drink': <staticmethod object at 0x000002908F157310>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}



p.age = 18
p.name = 'caiqiyue'

def speak():
    print("speak")
    
p.speak = speak

print(p.__dict__)#{'age': 18, 'name': 'caiqiyue', 'speak': <function speak at 0x00000269DE8A13A0>}
#可以看到，dict是字典，存放键值对，但并没有要求，值 ， 是什么特殊的东西
#值可以是数值，字符串，也可以是函数本身（不是执行函数）等，这些东西的本质都是对象，所以说，类中创建的函数也是存放在d类的ict中