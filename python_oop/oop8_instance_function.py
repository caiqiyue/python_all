class Person:
    def eat(self,food):
        print("eat",food,self)#self  <__main__.Person object at 0x000001BC8BBF8190> 是一个person对象
        
    def drink(xxx):
        print(xxx)
        
    def run():
        print("run")
        
p = Person()
p.eat("米饭")#使用实例调用实例方法的时候，它会自动的将实例传到实例方法的第一个参数self中，不需要手动传递
print(p)#<__main__.Person object at 0x000001BC8BBF8190>



print(Person.__dict__)#既然，任何方法都存储在类中，那么在dict应该都能找到它
print(Person.eat)#并且能想  Person.age  一样访问属性，一样访问方法   Person.eat  <function Person.eat at 0x0000022187E513A0>


#这样的本质就是   取出 eat 函数   把它当做  eat(形参1，形参2) 一样正常使用
Person.eat(123,'abc')#此时的，self就变成了 123   也就是说self自动传递的时候一定是实例，手动传递的时候可以是其他的    eat abc 123

func = Person.eat

func("asda",321)#eat 321 asda   此时可以认为，就是把实例方法中的函数取出来，当做一个普通函数使用，而非类中创建的方法

print(p)
p.drink()#<__main__.Person object at 0x000001D932A67310>
#说明  实例方法中要求你传递实例的形参self，其实不一定非得叫做self，改成其他的也可以，就是第一个参数传递实例就是实例方法

p.run()#这个就会报错，因为实例调用方法时，会自动把自己传递进去，如果此时的方法中没有形参接受，就会报错