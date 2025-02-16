class Person:
    pass


one_person = Person()

#Person不仅作为了变量代表这个类，也是这个类的名称
print(Person.__name__)#返回：Person
abc = Person
print(abc.__name__)#类名没有变，还是Person，说明Person是变量，指向了这个叫做Person的类

# Person = 666
# print(666)#返回666，说明Person是变量，是可以被改的

print(one_person)#<__main__.Person object at 0x0000021CB1C88190>
print(one_person.__class__)#<class '__main__.Person'>
print(Person)#对象的__class__指向着Person，保证了类与对象之间的关系