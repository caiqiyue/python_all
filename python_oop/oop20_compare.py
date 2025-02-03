
"""
10 > 2
10和 2  本质上就是 int 这个类  创建的  两个实例对象 
那么肯定 在int这个类中 定义了  比较云算法  需要调用的内置函数

因此，我们也可以自定义 我们自己的类的比较运算
"""

class A(object):
    
    def __eq__(self, value: object) -> bool:
        #两个 实例对象 进行  == 或者 ！=  的时候 会调用这个内置函数  self就是  ==  左边的实例 ， value就是右边的实例
        #注意 ！= 也并不是 调用 __eq__函数 ， 只是  ！=  一定会返回 __eq__结果的  相反值
        #如果  有 __ne__函数 ！=  就不会去关注  __eq__函数
        print(value)
    pass

a1 = A()
a2 = A()
print(a2)#<__main__.A object at 0x000001B4FFF681C0>

#<__main__.A object at 0x000001B4FFF681C0>
a1 == a2


class Person(object):
    def __init__(self,age,height) -> None:
        self.age = age
        self.height = height
        
    def __eq__(self, value: object) -> bool:
        return self.age == value.age
    
    def __ne__(self, value: object) -> bool:
        print("如果有 __ne__  != 就会先调用这个函数")
        
    def __gt__(self,other):
        print(" 大于号  匹配的 函数")
        
    def __ge__(self,other):
        print("这是 大于等于 匹配的函数")
        
    def __lt__(self,other):
        print("这是 小于  匹配的函数")
        
    def __le__(self,other):
        print("这是 小于等于 匹配的函数")
    
"""
需要注意的时候，有时候，你只定义了 一个 小于  匹配的函数 __lt__(self,other)
但使用的时候的时候  你用了大于号 ,而且你没有定义  大于 匹配的函数
p1 < p2  --- >  __lt__(p1,p2)
p1 > p2  --- > p2 < p1 --- > __lt__(p2,p1)

这种就是 互换参数的  一种方式

而且 <=  不会同时调用 __eq__ 和  __lt__方法，他只会有自己对应的函数

"""
p1 = Person(19,180)
p2 = Person(20,180)
print(p1 == p2)
print(p1 != p2)
p1 >= p2
p1 <= p2
p1 < p2
p1 > p2