
"""
说是资源的覆盖，其实本质上还是 资源的继承顺序导致的使用顺序罢了

"""

class D(object):
    age = 'd'
    def test(self):
        print("D")
        
class B(D):
    age = 'b'
    def test(self):
        print("B")
        
        
class C(D):
    age = 'c'
    def test(self):
        print("C")
        
    def test2(self):
        print(self)
        
    @classmethod
    def test4(cls):
        print(cls)
        
class A(B,C):
    age = 'a'
    def test(self):
        print("a")
        
# print(A.mro())
a = A()
print(A.test4())#此时的test4是继承自 C类的 类方法  但是是 A类调用的 ，所以传入的cls还是A  <class '__main__.A'>
print(a.test2())#<__main__.A object at 0x00000201354EE850>