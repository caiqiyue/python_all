class Person:
    age = 10
    
    
p = Person()

print(p.age)#10,因为对象没有age属性，显然它会访问类的age属性
print(Person.age)#10


#p.age = 15 一定是新增p对象的age属性，只有在查询时，才有对象能访问到类的属性，新增时，没有这一规律

p.age += 5 #注意这其实并不是修改操作   p.age = p.age + 5   等式右边的p.age是访问到了类的age属性，等式左边则是为对象p添加了age属性

print(p.age)#15
print(Person.age)#10
