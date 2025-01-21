class Money:
    age = 1
    num = 10



#再提醒一遍，在python中万物皆对象，类其实也是一种特殊的对象
Money.count = 1
print(Money.count)

print(Money.__dict__)

one = Money()
print(one.__class__)#对象one通过__class__与Money连接，可以访问到类的属性
print(one.age)
print(one.num)
print(one.count)


one.age = 2000#查找顺序，优先先从对象自己的身上去找
print(one.age)

del Money.age
print(type(one))#Money object  one是Money对象
print(Money.age)#type object 'Money'  Money 是type对象

