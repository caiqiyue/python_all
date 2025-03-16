

class Animal(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s吃饭" % self)
        
    def play(self):
        print("%s玩耍" % self)
        
    def sleep(self):
        print("%s睡觉" % self)
        




class Dog(Animal):
        
        
        
    def work(self):
        print("%s看家" % self)
        

        
    def __str__(self):
        return '小狗{}，年龄{}正在'.format(self.name,self.age)
    
    
class Cat(Animal):

        
    def work(self):
        print("%s捉老鼠" % self)
        
    def __str__(self):
        return '小猫{}，年龄{}正在'.format(self.name,self.age)
    

class Person(Animal):
    def __init__(self,name,age,pets):
        super(Person,self).__init__(name,age)
        self.pets = pets
        
    def cultivate_pets(self):
        for pet in self.pets:
            pet.sleep()
            pet.eat()
            pet.play()
        
        
    
    def make_pets_work(self):
        for pet in self.pets:
            pet.work()
        

        
    def __str__(self):
        return 'r人{}，年龄{}正在'.format(self.name,self.age)
    
    
d = Dog("小黑",1)
c = Cat('蛋蛋',2)
p = Person('xxx',12,[d,c])

p.cultivate_pets()