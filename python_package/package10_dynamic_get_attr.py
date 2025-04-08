

class MyClass(object):
    
    def __init__(self,x):
        self.x = x
        
    def my_method(self):
        pass
    
    
    
obj = MyClass(10)

#内置函数，动态获取对象的所有属性和方法
print(dir(obj))

#内置函数，动态获取对象的指定属性的值
print(getattr(obj,'x'))
print(getattr(obj,'my_method'))

#内置函数，动态的判断对象是否拥有该属性
print(hasattr(obj,'x'))
print(hasattr(obj,'y'))