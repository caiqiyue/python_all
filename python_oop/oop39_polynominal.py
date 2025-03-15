

class Animal(object):
    def jiao(self):
        pass
    
    
    
class Dog(Animal):
    def jiao(self):
        print("wangwang")
        
        
class Cat(Animal):
    def jiao(self):
        return print("miaomiao")
    
def test(obj):
    """
    python 是一个动态数据类型
    同一个 a ,a= 10就是int类型
    a = 'abc' 就是字符串类型
    a = true就是布尔类型
    所以相对来说，不关心a是什么类型，更关心a具有哪些属性和行为
    这个test(obj)，不关心obj是什么类型，只关心obj有没有jiao()这个方法
    
    而多态大部分是在静态类型语言中去实现的，比如java
    test(Animal obj)  这样的话既可以传入Dog类，又可以传入Cat类，使用父类中定义好的方法，这就是多态
    所以相比之下，python中就不存在真正意义上的多态，也不需要
    """
    obj.jiao()
    

d = Dog()
c = Cat()

test(d)

