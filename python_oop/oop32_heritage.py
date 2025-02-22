
class Person(object):
    pass

class Father(Person):
    pass


class Mother(Person):
    pass


class Children(Father,Mother):
    pass


"""
注意 object 和 type
obejct 是 被继承
type是 创建类
"""

c = Children()
print(c.__class__)#谁创建了实例对象
print(Children.__class__)#谁创建了类对象
print(type.__class__)#谁创建了 元类
print(object.__class__)#也是有 type 实例化出来的 类对象


print(type.__bases__)#元类 创建 obejct 又继承自 object
print(Children.__bases__)#输出 这个类 继承自，哪些类
print(Father.__bases__)#python3 的新式类，继承自 object，继承了 __getattribute__，可以实现描述器；经典类则不行
print(int.__bases__)#object
print(float.__bases__)#object
print(bool.__bases__)#int