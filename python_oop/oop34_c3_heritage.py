
"""
自从python2.3之后，资源继承顺序的MRO原则就产生了 C3  算法
了解即可吧，算法过程看看笔记
"""
import inspect

# class D(object):
#     pass

# class B(D):
#     pass

# class C(D):
#     pass


# class A(B,C):
#     pass

# print(inspect.getmro(A))#打印资源继承顺序


#存在问题的资源继承，看看C3算法能否检测出来

class D(object):
    pass

class C(D):
    pass

class B(C):
    pass

class A(C,B):#A继承C，这条继承关系 是冗余的
    pass

print(inspect.getmro(A))#继承顺序有问题



