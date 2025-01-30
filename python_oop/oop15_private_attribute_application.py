class Person:
    def __init__(self) -> None:
        self.__age = 10#私有属性
        
    def setAge(self,age):
        """
        私有属性（除了强行访问）只能在类的内部访问
        想要外部访问它，只能提供两个函数，起到数据保护作用
        """
        
        #起到数据保护的作用
        if isinstance(age,int) and 0 < age < 200:
            self.__age = age
        else:
            print("数据有问题")
        
    def getAge(self):
        return self.__age
        
        
        
        
p = Person()

p.__age = -1#可以看出来，这个并不是访问  私有属性age，因为根本不能这样访问，所以这是添加实例属性的语句  只不过 名称看上去像私有属性一样

print(p.__dict__)#{'_Person__age': 10, '__age': -1}


p.setAge(19)
print(p.getAge())