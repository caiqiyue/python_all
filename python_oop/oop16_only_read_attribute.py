class Person:
    __age = 10#把age设置为只读属性，先设置为私有属性，并提供一个访问接口，使它只能读取不能修改
    
    def getAge(self):
        return self.__age
    

p = Person()
print(p.getAge())

"""
上面也是设置 只读属性  的方法
但是，有弊端，第一  本来是 p.age就可以访问属性，现在变成了  p.ageAge()
第二是  p.age = 1任然会运行成功，因为  这是新创建一个实例属性，而非访问类中的私有属性，但会让人误以为这是在访问类中的私有属性
"""


class Animal:
    __age = 10
    
    
    #这样 可以 使用  访问属性的方式  来 方法，而且  也不能  p.age = 1这样赋值了 
    @property
    def age(self):
        return self.__age
a = Animal()
print(a.age)