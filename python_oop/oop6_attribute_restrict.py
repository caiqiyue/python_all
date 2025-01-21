class Person:
    __slots__ = ['age']
    

"""
前面我们说过，对象的属性可以被访问，被修改，这样的话，同一个类产生的对象，却拥有千奇百怪的属性，很不好
可以通过添加类的slots  内置私有属性，来限制其产生的对象对属性的增加
"""

p = Person()
p.age = 10

p.num = 11

Person.num = 10#就连类，也不能随意增加属性了

print(p.age)#slots限制了只能增加age属性
print(p.num)