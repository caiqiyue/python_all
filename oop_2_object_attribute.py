class Person:
    pass


p = Person()

p.age = 18
p.sex = 'male'
print(p.age,p.sex)

#__dict__中包含此对象拥有的所有属性
print(p.__dict__)

#p.age是p中的一个变量，指向内存某一位置，存放数值18的位置
print(id(p))#2393710559632
print(id(p.age))#2393705704272
