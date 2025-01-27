"""
python中万物皆对象，实例是对象，类也是对象，实例由类产生，类由元类产生
"""

#由类产生的实例，通过__class__存储着创建自己的类的内存地址
num = 10#变量num指向了   10   这个对象   那么  10这个对象  是由什么创造的？
print(num.__class__)#  10 这个对象是  由  int类  创建的


school = "adas"
print(school.__class__)#   "adas"这个对象，是由   str 类创建的


#这是自定义的一个类
class Person:
    pass

p = Person()
print(p.__class__)


#类也是对象，那么它们是由谁创建的,全都是  type
print(int.__class__)
print(num.__class__.__class__)#<class 'type'>
print(Person.__class__)
print(str.__class__)

#看看元类是由什么创建的,，也是type本身
print(Person.__class__.__class__)