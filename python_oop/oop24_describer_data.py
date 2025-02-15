




class Age(object):
    def __get__(self,instance,owner):
        print("get",self,instance,owner)
#get <__main__.Age object at 0x000001D7E7D0E370> <__main__.Person object at 0x000001D7E7D0E850> <class '__main__.Person'>
#self是age实例  instance是 person实例 owner是person类
        # return self.v
        return instance.v 
        
    def __set__(self,instance,value):
        print("set",self,instance,value)
        #set <__main__.Age object at 0x000001D7E7D0E370> <__main__.Person object at 0x000001D7E7D0E850> 10
        #self是age实例  instance 是 person实例 value就是外部传入的值
        # self.v = value
        instance.v = value
        
    def __delete__(self,instance):
        print("del",self,instance)
        del instance.v
        
        
class Person(object):
    age = Age()#类变量，被所有实例共享
    
    
    
p1 = Person()
p1.age = 10#p.age 通过实例p访问搭配Person的类变量age，age指向age实例，调用Age类中的set方法，是实例p访问的age，所以instance是实例p，但age本身又是Age类产生的对象，所以self是age
print(p1.age)


p2 = Person()#<__main__.Age object at 0x000001CED6B5E370>
p2.age = 12
print(p2.age)

print(p1.age)#p1实例和p2实例共享 类变量 age ,即共享了同样一个，描述器 Age(),所以数据的修改会出现问题，p1.age被修改成p2的age值了


"""
所以   真正  的 age属性值，还是应该绑定在 Person对象上，而非 age对象上，把 self.v 改成 instance.v即可
"""
    
