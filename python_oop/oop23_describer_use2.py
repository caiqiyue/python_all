


class Age(object):
    """
    age属性的描述器
    对p.age  访问 实例p的 age属性，就会被转化为访问Age类内部的__get__方法
    但是需要注意一点，这样定义的数据描述器，使用类访问数据描述器时，只能触发 __get__方法
    
    
    新式类，实例访问 数据描述器 都可以调用；  类访问 数据描述器 只有get可以调用（必须数据描述器，和 该属性所属的类 都是新式类）
    经典类  实例访问和类访问 数据描述器  都不会生效
    
    
    此外，如果 描述器可以被具体分为 两类  资料描述器 和 非资料描述
    资料描述器  就是  实现了 get,set
    非资料描述器  仅仅实现了  get
    
    就会遇到一个 现实问题 当 类属性 和 实例属性 名字一样时， 类属性指向了一个 描述器
    
    也就是说  当描述器 和 某一普通属性  重名时 ，是否 有调用  优先级
    
    资料描述器 > 实例属性 > 非资料描述器
    """
    def __get__(self,instance,onwer):
        print("资料描述器的get")
        
    def __set__(self,instance,value):
        print("资料描述器的set")
        
    def __delete__(self,instance):
        print("资料描述器的delete")




class Name(object):
    
    def __get__(self,instance,owner):
        print("非资料描述器的get")


class Person(object):
    age = Age()#类属性，指向一个描述器（实现了 get,set 是 资料描述器）
    name = Name()
    
    
    def __init__(self) -> None:
        self.age = 10  #一个 普通 的 实例属性
        self.name = 'cas'
    
    
p = Person()
p.age = 1
print(p.age)
del p.age
print("==========================================================")
Person.age = 1
print(Person.age)#使用类 来访问数据描述器的时候，只能调用__get__方法
del Person.age

p1 = Person()

p1.age = 19#资料描述器 优先级 高于 实例属性，此处 不是给 实例的属性赋值，而是通过实例访问 类变量age ，触发了描述器的 set
print(p1.age)
print(p1.__dict__)
"""
set
set
get
None
{}
首先，创建 p1实例时，执行init函数，self.age = 10,此时的age是资料描述器 优先级高于实例属性，
所以 这里的 self.age 不会被当做实例属性初始化，而是当做 用实例访问类变量 ，那么就触发了 描述器的 set方法
这就是第一个set

"""


p1.name = 'dw'
print(p1.name)
print(p1.__dict__)
"""
dw
{'name': 'dw'}
name指向的是 非资料描述器  优先级 低于 实例属性 
所以 init中的 self.name 是 对实例属性初始化 而非 通过实例访问 类变量 触发描述器的 set
"""