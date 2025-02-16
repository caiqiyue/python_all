

#未改进版=======================，可以打印出当前类 创建了多少实例

instancecount = 0

class Person(object):
    def __init__(self) -> None:
        global instancecount
        print("计数器+1")
        instancecount += 1
        
        
    def __del__(self):
        global instancecount
        print("计数器 -1")
        
        instancecount -= 1
    
    @staticmethod
    def log():
        global instancecount
        print("当前被创建的实例个数有",instancecount)
        

p1 = Person()

p1.log()

del p1

p2 = Person()
p2.log()


#改进版=============================================================
class Animal(object):
    __count = 0
    
    def __init__(self) -> None:
        self.__class__.__count += 1
        
    def __del__(self):
        Animal.__count -= 1
        
    @classmethod
    def log(cls):
        print(cls.__count)
        
a1 = Animal()
Animal.log()

a2 = Animal()
Animal.log()

del a2

Animal.log()