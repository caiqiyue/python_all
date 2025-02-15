

#普通的装饰器，使用函数描述
"""
比如现在有个 发 qq说说  的 函数
但是需要在发说说前进行验证，加入额外的逻辑流程，就可以使用  装饰器
"""



from typing import Any


def check(func):
    def inner():#实现新功能的函数，总共需要两部分  新功能代码 + 原函数
        print("验证流程")
        func()
        
    return inner

@check
def fashuoshuo():
    print("发说说")

#上面的写法，等同于
#fushuoshuo = check(fashuoshuo)
fashuoshuo()



#现在使用  类完成装饰器
class check(object):
    """
    为了能 像  fushuoshuo = check(fashuoshuo) 此时的 check是一个类 ，那么  类（）就需要 初始化方法  
    fashuoshuo()  fashuoshuo就是一个 check实例  实例()就需要 call方法
    """
    def __init__(self,func) -> None:
        self.f = func
        
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("验证流程")#新加的逻辑流程
        self.f()#执行被装饰的函数

