#创建类对象



__metaclass__ = xxxx  #模块级别的指定元类

class Person:
    __metaclass__ = xxxx #子类没有元类，先往其父类中找元类

#调用底层的创建逻辑
class Student(Person):#Person又是变量，又是类名称  也可以 class Person(__metaclass__ = xxx)指名元类
    # __metaclass__ = xxxx 指名创建Person类对象的 元类  不一定非得是type元类，也可以是自定义的
    count = 1
    def run(self):
        print("run")
print(Student)
        

#使用元类 去创建类对象
def run(self):
    print(self)
xxx = type("Animal",(),{"count":1,"run":run})#第一个参数是 类的名称(并不是声名了一个变量指向了animal类)   第二个参数 是 元组  里面都是父类  第三个参数是 字典 里面存储 属性 方法


print(xxx)#xxx只是变量指向animal这个类
print(xxx.count)
dog = xxx()
print(dog)
dog.run()#<__main__.Animal object at 0x000001BC1A1594F0>