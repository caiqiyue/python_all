
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
        
class A(B,C):
    age = 'a'
    def test(self):
        print("a")
        
print(A.mro())
print(A.age)