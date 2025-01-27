class Person:
    age = 10
    def run(self):
        """
        实例方法访问类属性，访问实例属性
        """
        print(self.age)
        print(self)
        print(self.num)
        
    @classmethod
    def eat(cls):
        print(cls)
        print(cls.age)
        #print(cls.num) 类方法不可以访问实例属性
        
    @staticmethod
    def speak():
        """
        本质上静态方法的出现就是考虑到这个方法内部不会用到类和实例
        """
        print(Person.age)
    
p = Person()
p.num = 11
#调用实例方法去访问类属性和实例属性
p.run()
#调用类方法，去访问实例属性和类属性，但实例属性不能访问
p.eat()
Person.eat()
#调用静态方法去访问类属性
p.speak()



#类属性访问
print(Person.age)
print(p.age)

#实例属性访问
print(p.num)
# print(Person.num) 不可以通过类去访问实例属性
