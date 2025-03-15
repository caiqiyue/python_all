


def checkLogin(func):
    print("xxxxxx")
    def inner():
        print("登录验证..................")
        func()
    return inner


@checkLogin
def fashuoshuo():
    print("fashuoshuo")
"""
@checklogin 的时候， 就等同于 直接执行了 fashuoshuo = checkLogin(fashuoshuo),这就是装饰器的执行时间，立即执行 一@就执行了
"""    
# fashuoshuo = checkLogin(fashuoshuo)
# fashuoshuo()

@checkLogin
def fatupian():
    print("fatupian")

# fatupian()

"""
功能代码要和业务逻辑代码分开
"""
boundindex = 1
if boundindex == 1:
    print('登录验证')#在业务逻辑代码中加入 登录代码，复用性太差，代码冗余
    fashuoshuo()
else:
    fatupian()