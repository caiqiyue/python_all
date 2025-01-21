class Money:
    pass

class Person:
    pass

class Dog:
    age = 10
    

print(Dog.__dict__)
#Dog.__dict__['age'] = 100#也就是说对象的dict可以修改访问，但是类的dict只能访问

dog = Dog()
print(dog.__dict__)
print(dog.age)#可以通过，对象去访问类的属性，但是对象的dict中不保存类的属性



one = Money()
one.age = 19
one.height = 180
#所有的属性存在dict中，dict是一个字典
print(one.__dict__)


#当然我们也可以直接操作这个字典对属性进行操作,由此我们可知其实对属性的访问就是对dict的访问
p = Person()
p.__dict__ = {'name':'kk','age':10}
print(p.age)
p.__dict__['name'] = 'cai'
print(p.name)
p.__dict__ = {'sex':"male"}
print(p.__dict__)


